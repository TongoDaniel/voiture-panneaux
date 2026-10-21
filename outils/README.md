# Outils

- `etapes.json` : la liste des étapes, source unique. `etapes.py` l'a générée.
- `generer_etapes_md.py` : régénère `docs/ETAPES.md` après une modification de `etapes.json`.
- `creer_issues.py` : crée une issue par étape (une par voiture pour les étapes « voiture »), les labels `voiture-L`, `voiture-J`, `equipe`, `P0` à `P10`, et le GitHub Project « Voiture panneaux » qui les regroupe.

## Créer les issues et le Project

```
gh auth login
gh auth refresh -s project
python outils/creer_issues.py --essai   # pour voir ce qui sera créé
python outils/creer_issues.py
```

Dans le Project, ajouter une vue « Board » groupée par label (`voiture-L`, `voiture-J`, `equipe`) pour voir chaque voiture séparément. Fermer une issue la coche.
