# Plan

| Phase | Contenu | Période indicative |
| --- | --- | --- |
| P0 | Cadrage | 21 → 26 oct |
| P1 | Matériel et alimentation | 27 oct → 2 nov |
| P2 | Moteurs | 27 oct → 9 nov |
| P3 | Liaison ESP32 et Arduino | 3 → 9 nov |
| P4 | Pilotage Wi-Fi depuis le PC | 3 → 9 nov |
| P5 | Caméra | 3 → 16 nov |
| P6 | Bases de l'IA (en parallèle de P1 à P5) | 27 oct → 9 nov |
| P7 | Données | 10 → 30 nov |
| P8 | Entraînement et évaluation | 1 → 20 déc |
| P9 | Intégration temps réel | 21 déc → 17 jan |
| P10 | Mesures et rendu | 18 → 24 jan |
| Marge | Corrections, répétition | 25 → 31 jan |

Règles :

- Une étape = une fonction + un test. On coche quand le test passe.
- Chacun avance sur sa voiture ; les étapes « équipe » sont réparties au point hebdo.
- Le jeu de données mélange les images des deux voitures : le modèle sera plus robuste.
- Pas de nouvelle fonction après le 24 janvier.

## Pièges connus

- L'ESP32 ne tolère pas le 5 V : diviseur de tension sur le TX de l'Arduino.
- GND communs entre Arduino, L298N et ESP32 : première cause de bugs.
- Une caméra qui manque de courant redémarre en boucle : buck 5 V dédié sur la broche 5V de la carte.
- Sur la WROVER CAM, seuls les GPIO 13, 14, 32 et 33 sont vraiment libres (voir le README). Ne jamais utiliser 16 et 17 (PSRAM).
- Si le capteur n'a pas de JPEG matériel (cas du GC0308), il faut convertir les images avec `frame2jpg()` (`img_converters.h`).
- L'augmentation `fliplr` de YOLO transforme une flèche gauche en flèche droite : la mettre à 0.
- Le PC peut rebasculer sur le Wi-Fi de la maison : « Oublier le réseau » puis se reconnecter.
