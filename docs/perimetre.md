# Périmètre

## Architecture choisie

**Freenove ESP32-WROVER CAM seule** sur chaque voiture (décidé le 21 octobre 2026). Raison : une seule carte filme, émet le Wi-Fi et relaie les commandes à l'Uno en UART ; pas de second ESP32 à câbler ni d'adaptateur USB-série, et la PSRAM du module WROVER-E garde un flux fluide. Les moteurs restent sur l'Uno, car la caméra occupe la plupart des GPIO de l'ESP32.

## Réaction à chaque panneau

| Panneau | Réaction |
| --- | --- |
| STOP | |
| 30 | |
| Flèche gauche | |
| Flèche droite | |

## Hors périmètre

- 
