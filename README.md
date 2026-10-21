# Voiture qui lit les panneaux

Projet de 4A, Ingénierie Logiciel et IA, Polytech Dijon. Binôme : Daniel (Lein) TONGO et Jephte JOMO. Rendu visé : fin janvier 2027.

Chacun construit **sa propre voiture**. Les deux voitures partagent le même code et le même modèle d'IA. Chaque voiture roule sur un circuit, reconnaît 4 panneaux imprimés (STOP, 30, flèche gauche, flèche droite) et réagit seule.

## Architecture

Chaque voiture a une seule carte Wi-Fi : la **Freenove ESP32-WROVER CAM**. Elle filme, envoie le flux au PC, reçoit les commandes et les transmet à l'Arduino en série.

```
Freenove ESP32-WROVER CAM ──Wi-Fi (flux vidéo)──► PC (Python, OpenCV, YOLOv8n)
          ▲                                          │ détection → décision
          └──────────Wi-Fi (commandes)───────────────┘
          │
          └──UART (GPIO 14/13)──► Arduino Uno ──► L298N ──► 4 moteurs
               (diviseur 5 V → 3,3 V sur le TX de l'Uno)
```

L'Arduino ne fait aucune IA : il exécute des commandes. L'inférence tourne sur le PC. La caméra occupe la plupart des GPIO de l'ESP32 : les moteurs restent donc sur l'Uno.

| Voiture | Réseau Wi-Fi | Responsable |
| --- | --- | --- |
| Voiture L | `TNG_Car_L` (192.168.4.1) | Lein |
| Voiture J | `TNG_Car_J` (192.168.4.1) | Jephte |

Utiliser deux canaux Wi-Fi différents (par exemple 1 et 11) pour que les voitures ne se brouillent pas.

## Suivre l'avancement

- La liste des 92 étapes est dans [docs/ETAPES.md](docs/ETAPES.md). Une étape donne **une seule fonction**, avec un test qui dit quand elle marche. On ne passe à la suivante que quand le test passe.
- Les étapes « voiture » se font sur chaque voiture, les étapes « équipe » une seule fois.
- Les mêmes étapes existent en issues GitHub, regroupées dans le GitHub Project du dépôt (voir [outils/README.md](outils/README.md)).

## Organisation du dépôt

| Dossier | Contenu |
| --- | --- |
| `arduino/` | Sketchs de l'Arduino Uno (moteurs, liaison série, watchdog) |
| `esp32/` | Sketchs de l'ESP32 (Wi-Fi, caméra, relais des commandes) |
| `pc/` | Scripts Python (pilotage, capture, détection, décision) et notebooks Colab |
| `docs/` | Cadrage, périmètre, concepts IA, mesures, résultats |
| `outils/` | Liste des étapes et script de création des issues |

Les images et les poids de modèle (`*.pt`) ne vont pas dans Git : ils restent sur Roboflow ou Google Drive.

## Matériel par voiture

| Pièce | Rôle | Point d'attention |
| --- | --- | --- |
| Châssis 4WD, 4 moteurs DC | Base mécanique | Bien serrer les fils moteurs |
| Arduino Uno R3 | Commande des moteurs | 5 V max par pin |
| L298N | Pont en H | Batterie sur la borne 12 V, jamais sur 5 V ; retirer les jumpers ENA/ENB |
| Freenove ESP32-WROVER CAM (module ESP32-WROVER-E avec PSRAM, USB-C, programmateur intégré) + carte d'extension GPIO Freenove | Caméra, Wi-Fi, relais des commandes vers l'Uno | Pins en 3,3 V ; aucun adaptateur USB-série nécessaire |
| LiPo 2S 7,4 V, 1000 à 1500 mAh, XT60 | Énergie | Chargeur équilibré, jamais sous 3,3 V par élément |
| Buck LM2596 réglé à 5,0 V | Alimente la carte caméra par sa broche 5V | Régler au multimètre avant de brancher |
| Interrupteur, XT60, dupont, résistances 1 kΩ et 2 kΩ | Câblage, diviseur | Relier tous les GND |

## Brochage (proposition)

### L298N vers Arduino

| L298N | Arduino |
| --- | --- |
| ENA | 5 (PWM) |
| IN1 | 4 |
| IN2 | 7 |
| IN3 | 8 |
| IN4 | 9 |
| ENB | 6 (PWM) |

### Liaison série Uno ↔ ESP32-WROVER CAM

| Arduino Uno | ESP32-WROVER CAM | Remarque |
| --- | --- | --- |
| D2 (RX, SoftwareSerial) | GPIO 14 (TX de Serial2) | 3,3 V suffit pour l'Uno |
| D3 (TX, SoftwareSerial) | GPIO 13 (RX de Serial2) | **Par le diviseur 1 kΩ / 2 kΩ** |
| GND | GND | Masse commune obligatoire |

Alimentation de la carte caméra : sortie du buck 5,0 V sur la broche **5V**, GND sur **GND**. L'USB-C sert seulement à programmer.

### Réglages de l'IDE Arduino pour la caméra

- Carte : « ESP32 Wrover Module », PSRAM activée, schéma de partition « Huge APP ».
- Exemple de départ : `CameraWebServer`, avec `#define CAMERA_MODEL_WROVER_KIT`.

### GPIO à ne pas utiliser sur la WROVER CAM

- Pris par la caméra : 4, 5, 18, 19, 21, 22, 23, 25, 26, 27, 34, 35, 36, 39.
- Pris par la PSRAM : 16, 17.
- 1 et 3 : port USB (moniteur série).
- 0, 2, 12, 15 : broches de démarrage, à éviter ou à laisser libres au boot.
- Libres et sûres : **13, 14, 32, 33**.
