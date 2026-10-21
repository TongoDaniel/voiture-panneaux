"""Régénère docs/ETAPES.md à partir de outils/etapes.json."""
import json, pathlib
racine = pathlib.Path(__file__).resolve().parent.parent
etapes = json.loads((racine / "outils" / "etapes.json").read_text(encoding="utf-8"))
lignes = ["# Étapes", "",
          "Une étape = une fonction obtenue + un test. Coche la case quand le test passe.",
          "Colonnes : **L** = voiture de Lein, **J** = voiture de Jephte, **É** = équipe (une seule fois).", ""]
phase = None
for e in etapes:
    if e["phase"] != phase:
        phase = e["phase"]
        lignes += ["", f"## {phase} · {e['phaseNom']}", "", "| L | J | É | Étape | Test |", "| --- | --- | --- | --- | --- |"]
    v = e["portee"] == "V"
    cases = ("☐", "☐", "") if v else ("", "", "☐")
    lignes.append(f"| {cases[0]} | {cases[1]} | {cases[2]} | **{e['id']}** {e['titre']} | {e['test']} |")
(racine / "docs" / "ETAPES.md").write_text("\n".join(lignes) + "\n", encoding="utf-8")
print(len(etapes), "étapes écrites")
