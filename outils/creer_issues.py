"""Crée les labels, une issue par étape (deux pour les étapes « voiture ») et le GitHub Project.

Prérequis : GitHub CLI installé et connecté avec le droit « project » :
    gh auth login
    gh auth refresh -s project
Lancement depuis la racine du dépôt :
    python outils/creer_issues.py            # crée tout
    python outils/creer_issues.py --essai    # affiche sans rien créer
Le script peut être relancé : il ne recrée pas une issue dont le titre existe déjà,
mais l'ajoute au Project si elle n'y est pas.
"""
import json, pathlib, subprocess, sys

DEPOT = "TongoDaniel/voiture-panneaux"
PROPRIO = "TongoDaniel"
TITRE_PROJET = "Voiture panneaux"
ESSAI = "--essai" in sys.argv
racine = pathlib.Path(__file__).resolve().parent.parent
etapes = json.loads((racine / "outils" / "etapes.json").read_text(encoding="utf-8"))

def gh(*args, capture=False):
    if ESSAI and not capture:
        print("gh", " ".join(args)); return ""
    r = subprocess.run(["gh", *args], text=True, capture_output=True)
    if r.returncode != 0 and "already exists" not in r.stderr:
        print("Erreur :", r.stderr.strip())
    return r.stdout.strip()

labels = {"voiture-L": "1c5aa6", "voiture-J": "8e44ad", "equipe": "2f7d4f"}
for e in etapes:
    labels.setdefault(e["phase"], "d9ddd9")
for nom, couleur in labels.items():
    gh("label", "create", nom, "--repo", DEPOT, "--color", couleur, "--force")

existantes = {}
if not ESSAI:
    sortie = gh("issue", "list", "--repo", DEPOT, "--state", "all", "--limit", "500", "--json", "title,url", capture=True)
    existantes = {i["title"]: i["url"] for i in json.loads(sortie or "[]")}

projet = None
if not ESSAI:
    liste = json.loads(gh("project", "list", "--owner", PROPRIO, "--format", "json", capture=True) or '{"projects":[]}')
    projet = next((p["number"] for p in liste.get("projects", []) if p["title"] == TITRE_PROJET), None)
    if projet is None:
        cree = json.loads(gh("project", "create", "--owner", PROPRIO, "--title", TITRE_PROJET, "--format", "json", capture=True) or "{}")
        projet = cree.get("number")
        gh("project", "link", str(projet), "--owner", PROPRIO, "--repo", DEPOT)

for e in etapes:
    variantes = [("L", "voiture-L"), ("J", "voiture-J")] if e["portee"] == "V" else [("É", "equipe")]
    for code, label in variantes:
        titre = f"[{e['id']}·{code}] {e['titre']}"
        if titre in existantes:
            # Issue déjà créée : on s'assure seulement qu'elle est dans le Project.
            if projet:
                gh("project", "item-add", str(projet), "--owner", PROPRIO, "--url", existantes[titre])
            continue
        corps = (f"**Phase :** {e['phase']} · {e['phaseNom']}\n\n"
                 f"**Fonction obtenue :** {e['titre']}\n\n"
                 f"**Test de validation :** {e['test']}\n\n"
                 "Fermer l'issue quand le test passe.")
        url = gh("issue", "create", "--repo", DEPOT, "--title", titre, "--body", corps,
                 "--label", label, "--label", e["phase"], capture=not ESSAI)
        if ESSAI:
            continue
        print(titre, "→", url)
        if projet and url:
            gh("project", "item-add", str(projet), "--owner", PROPRIO, "--url", url)
print("Terminé.")
