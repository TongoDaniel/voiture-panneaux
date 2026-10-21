# Étapes

Une étape = une fonction obtenue + un test. Coche la case quand le test passe.
Colonnes : **L** = voiture de Lein, **J** = voiture de Jephte, **É** = équipe (une seule fois).


## P0 · Cadrage

| L | J | É | Étape | Test |
| --- | --- | --- | --- | --- |
|  |  | ☐ | **P0-01** Mail de présentation envoyé au tuteur | Le mail apparaît dans tes messages envoyés. |
|  |  | ☐ | **P0-02** Date de rendu connue | La date est écrite dans docs/cadrage.md. |
|  |  | ☐ | **P0-03** Livrables et critères de notation connus | La liste est écrite dans docs/cadrage.md. |
|  |  | ☐ | **P0-04** Dépôt cloné par Lein | Lein a poussé un commit visible sur GitHub. |
|  |  | ☐ | **P0-05** Dépôt cloné par Jephte | Jephte a poussé un commit visible sur GitHub. |
|  |  | ☐ | **P0-06** Créneau de point hebdo fixé | Un rendez-vous récurrent est dans vos deux agendas. |
|  |  | ☐ | **P0-07** Réaction de chaque panneau définie | docs/perimetre.md dit quoi faire pour STOP, 30, gauche, droite. |
|  |  | ☐ | **P0-08** Architecture choisie (Freenove ESP32-WROVER CAM seule) | Le choix et la raison sont dans docs/perimetre.md. |

## P1 · Matériel et alimentation

| L | J | É | Étape | Test |
| --- | --- | --- | --- | --- |
| ☐ | ☐ |  | **P1-01** Inventaire de la voiture vérifié | Chaque pièce de la liste du README est cochée comme présente. |
| ☐ | ☐ |  | **P1-02** Batterie LiPo chargée | Le multimètre lit entre 8,3 et 8,4 V après charge équilibrée. |
| ☐ | ☐ |  | **P1-03** Connecteur XT60 et interrupteur câblés sur la batterie | Interrupteur sur ON : tension présente en sortie ; sur OFF : 0 V. |
| ☐ | ☐ |  | **P1-04** Buck LM2596 réglé à 5,0 V | Le multimètre lit 5,0 V (±0,1) en sortie, sans rien de branché. |
| ☐ | ☐ |  | **P1-05** Châssis monté | Les 4 moteurs sont fixés et chaque roue tourne librement à la main. |

## P2 · Moteurs

| L | J | É | Étape | Test |
| --- | --- | --- | --- | --- |
| ☐ | ☐ |  | **P2-01** Arduino IDE installé et carte Uno reconnue | L'exemple Blink fait clignoter la LED de la carte. |
| ☐ | ☐ |  | **P2-02** L298N alimenté par la batterie | La LED du L298N s'allume quand tu bascules l'interrupteur. |
| ☐ | ☐ |  | **P2-03** Arduino alimenté sans USB | L'Arduino s'allume sur batterie seule (VIN ou 5 V du L298N). |
| ☐ | ☐ |  | **P2-04** Côté gauche avance | Roues en l'air, les 2 roues gauches tournent vers l'avant. |
| ☐ | ☐ |  | **P2-05** Côté gauche recule | Les 2 roues gauches tournent vers l'arrière. |
| ☐ | ☐ |  | **P2-06** Côté droit avance | Les 2 roues droites tournent vers l'avant. |
| ☐ | ☐ |  | **P2-07** Côté droit recule | Les 2 roues droites tournent vers l'arrière. |
| ☐ | ☐ |  | **P2-08** Vitesse réglable par PWM | Trois valeurs de analogWrite donnent trois vitesses distinctes à l'oreille et à l'œil. |
| ☐ | ☐ |  | **P2-09** Fonction avancer() | Un appel fait avancer les 4 roues 2 s puis stop. |
| ☐ | ☐ |  | **P2-10** Fonction reculer() | Un appel fait reculer les 4 roues 2 s puis stop. |
| ☐ | ☐ |  | **P2-11** Fonction tournerGauche() | Roues gauches en arrière, droites en avant : la voiture pivote à gauche. |
| ☐ | ☐ |  | **P2-12** Fonction tournerDroite() | La voiture pivote à droite sur place. |
| ☐ | ☐ |  | **P2-13** Fonction stop() | Les 4 roues s'arrêtent immédiatement. |
| ☐ | ☐ |  | **P2-14** Ligne droite au sol | Sur 2 m, la voiture dévie de moins de 20 cm (sinon corriger le PWM d'un côté). |
| ☐ | ☐ |  | **P2-15** Commande par le moniteur série USB | Taper F, B, L, R, S dans le moniteur série déclenche le bon mouvement. |

## P3 · Liaison ESP32 et Arduino

| L | J | É | Étape | Test |
| --- | --- | --- | --- | --- |
| ☐ | ☐ |  | **P3-01** Carte ESP32-WROVER CAM programmable depuis l'IDE | Carte « ESP32 Wrover Module » choisie, PSRAM activée : un sketch qui écrit « hello » chaque seconde s'affiche dans le moniteur série (USB-C). |
| ☐ | ☐ |  | **P3-02** Diviseur de tension monté (1 kΩ / 2 kΩ) | Avec 5 V sur la broche D3 de l'Uno, le multimètre lit environ 3,3 V au point milieu, relié au GPIO 13 de l'ESP32. |
| ☐ | ☐ |  | **P3-03** GND communs Arduino, L298N, ESP32 | Le multimètre en mode continuité bipe entre les trois GND. |
| ☐ | ☐ |  | **P3-04** ESP32 envoie un message à l'Arduino | Serial2 sur GPIO 14 (TX) et 13 (RX) : le moniteur de l'Arduino affiche « PING » reçu sur D2. |
| ☐ | ☐ |  | **P3-05** Arduino répond à l'ESP32 | Le moniteur de l'ESP32 affiche « PONG ». |
| ☐ | ☐ |  | **P3-06** Protocole de commande lu par l'Arduino | Une chaîne comme F150 est découpée en lettre F et vitesse 150 (affichées). |
| ☐ | ☐ |  | **P3-07** Commande ESP32 qui fait bouger la voiture | F150 tapé côté ESP32 fait avancer la voiture. |
| ☐ | ☐ |  | **P3-08** Watchdog sur l'Arduino | Sans nouvelle commande pendant 500 ms, la voiture s'arrête seule. |

## P4 · Pilotage Wi-Fi depuis le PC

| L | J | É | Étape | Test |
| --- | --- | --- | --- | --- |
| ☐ | ☐ |  | **P4-01** Point d'accès Wi-Fi propre à la voiture | Le PC voit et rejoint le réseau (TNG_Car_L pour Lein, TNG_Car_J pour Jephte). |
| ☐ | ☐ |  | **P4-02** ESP32 répond au PC | Un ping vers 192.168.4.1 répond, ou une page « ok » s'affiche dans le navigateur. |
| ☐ | ☐ |  | **P4-03** Script Python qui envoie une commande | python envoyer.py F150 fait avancer la voiture. |
| ☐ | ☐ |  | **P4-04** Pilotage au clavier | Les flèches du clavier pilotent la voiture, relâcher = stop. |
| ☐ | ☐ |  | **P4-05** Arrêt sur perte du Wi-Fi | Tu coupes le Wi-Fi du PC en roulant : la voiture s'arrête en moins d'1 s. |
|  |  | ☐ | **P4-06** Deux voitures en même temps | Les deux voitures roulent dans la même pièce sans se brouiller (canaux Wi-Fi différents). |

## P5 · Caméra

| L | J | É | Étape | Test |
| --- | --- | --- | --- | --- |
| ☐ | ☐ |  | **P5-01** Carte caméra alimentée par le buck 5 V | Buck branché sur la broche 5V de la carte, sans USB : aucun redémarrage en boucle pendant 2 min. |
| ☐ | ☐ |  | **P5-02** Image de la caméra dans le navigateur | L'exemple CameraWebServer avec CAMERA_MODEL_WROVER_KIT affiche une image nette. |
| ☐ | ☐ |  | **P5-03** Capteur de la caméra identifié | Le modèle (OV2640, OV3660, GC0308…) et s'il fait du JPEG matériel sont notés dans docs/mesures.md. |
| ☐ | ☐ |  | **P5-04** Flux lu par Python et OpenCV | Une fenêtre OpenCV affiche le flux en direct. |
| ☐ | ☐ |  | **P5-05** Fps et délai mesurés | Les deux chiffres sont notés dans docs/mesures.md (filmer un chronomètre). |
| ☐ | ☐ |  | **P5-06** Caméra fixée sur la voiture | Hauteur et angle ne bougent plus quand la voiture roule. |
| ☐ | ☐ |  | **P5-07** Flux et commandes en même temps | La même carte diffuse le flux et relaie les commandes : tu pilotes au clavier en voyant le flux, sans coupure. |

## P6 · Bases de l'IA

| L | J | É | Étape | Test |
| --- | --- | --- | --- | --- |
|  |  | ☐ | **P6-01** Environnement Python prêt (venv, ultralytics, opencv) | import ultralytics, cv2 ne donne aucune erreur. |
|  |  | ☐ | **P6-02** YOLOv8n pré-entraîné sur une photo | Une photo avec une personne ressort avec une boîte « person ». |
|  |  | ☐ | **P6-03** YOLOv8n pré-entraîné sur la webcam | Une tasse ou une personne est détectée en direct. |
| ☐ | ☐ |  | **P6-04** YOLOv8n pré-entraîné sur le flux de la voiture | La détection marche aussi sur l'image de la voiture. |
|  |  | ☐ | **P6-05** Fiche des concepts IA | docs/concepts.md explique train/val/test, précision, rappel, IoU, mAP, surapprentissage, et chacun l'explique sans notes. |

## P7 · Données

| L | J | É | Étape | Test |
| --- | --- | --- | --- | --- |
|  |  | ☐ | **P7-01** Panneaux imprimés et montés | 8 panneaux (4 classes × 2 tailles) sur papier mat et carton, qui tiennent debout. |
|  |  | ☐ | **P7-02** Script de capture d'images | Une touche enregistre une image horodatée dans un dossier de session. |
| ☐ | ☐ |  | **P7-03** Session de capture n°1 | Au moins 30 images par classe, prises avec ta voiture, décor et lumière notés. |
| ☐ | ☐ |  | **P7-04** Session de capture n°2 | Au moins 30 images par classe, autre décor ou autre lumière. |
| ☐ | ☐ |  | **P7-05** Images sans panneau | Au moins 40 images de décor vide avec ta voiture. |
|  |  | ☐ | **P7-06** Projet d'annotation créé (Roboflow ou CVAT) | Les 4 classes existent et les deux comptes y ont accès. |
|  |  | ☐ | **P7-07** Images de Lein annotées | Chaque image de Lein a ses boîtes, ou est marquée « vide ». |
|  |  | ☐ | **P7-08** Images de Jephte annotées | Chaque image de Jephte a ses boîtes, ou est marquée « vide ». |
|  |  | ☐ | **P7-09** Contrôle de 20 annotations au hasard | Aucune boîte fausse ou oubliée sur les 20. |
|  |  | ☐ | **P7-10** Découpage train / val / test par session | Aucune session n'apparaît dans deux jeux à la fois. |
|  |  | ☐ | **P7-11** Export au format YOLOv8 | Le dossier contient data.yaml et le tableau des effectifs par classe est dans docs/donnees.md. |

## P8 · Entraînement et évaluation

| L | J | É | Étape | Test |
| --- | --- | --- | --- | --- |
|  |  | ☐ | **P8-01** Notebook Colab qui charge le jeu de données | Le notebook affiche le nombre d'images par jeu, GPU actif. |
|  |  | ☐ | **P8-02** Entraînement court sans erreur | 5 epochs se terminent et produisent un best.pt. |
|  |  | ☐ | **P8-03** Entraînement complet v1 | best.pt v1 sauvegardé avec ses paramètres notés. |
|  |  | ☐ | **P8-04** Courbes d'apprentissage lues | La perte de validation ne remonte pas en fin d'entraînement (sinon surapprentissage). |
|  |  | ☐ | **P8-05** Scores sur le jeu de test | mAP50, précision et rappel par classe notés dans docs/resultats.md. |
|  |  | ☐ | **P8-06** Matrice de confusion analysée | Les confusions principales sont listées avec un exemple d'image. |
|  |  | ☐ | **P8-07** Images ajoutées pour les erreurs | Une nouvelle session cible les cas ratés. |
|  |  | ☐ | **P8-08** Entraînement v2 | mAP50 de v2 supérieure à v1 sur le même jeu de test (viser > 0,85). |

## P9 · Intégration temps réel

| L | J | É | Étape | Test |
| --- | --- | --- | --- | --- |
| ☐ | ☐ |  | **P9-01** Modèle entraîné sur le flux de la voiture | Les 4 panneaux sont reconnus en direct, boîtes affichées. |
|  |  | ☐ | **P9-02** Filtre de confiance minimale | En dessous du seuil (ex. 0,6), rien n'est pris en compte. |
|  |  | ☐ | **P9-03** Filtre 3 images d'affilée | Un panneau vu sur une seule image ne déclenche rien. |
|  |  | ☐ | **P9-04** Seuil de distance par taille de boîte | Un panneau lointain est ignoré, proche il est pris en compte. |
|  |  | ☐ | **P9-05** Machine à états de décision | À l'arrêt, le script affiche ROULE, RALENTI, ARRET ou VIRAGE selon le panneau montré. |
|  |  | ☐ | **P9-06** Délai de réarmement | Le même panneau ne déclenche pas deux fois en moins de 3 s. |
| ☐ | ☐ |  | **P9-07** Commandes envoyées, roues en l'air | Chaque panneau montré déclenche le bon mouvement des roues. |
| ☐ | ☐ |  | **P9-08** Latence de la boucle mesurée | Image → commande reçue en moins de 300 ms, chiffre noté. |
| ☐ | ☐ |  | **P9-09** Arrêt au STOP au sol | À vitesse réduite, la voiture s'arrête avant le panneau STOP. |
| ☐ | ☐ |  | **P9-10** Ralentissement au 30 | La voiture ralentit à la vue du 30 puis reprend. |
| ☐ | ☐ |  | **P9-11** Virage à gauche sur la flèche | La voiture tourne à gauche et repart. |
| ☐ | ☐ |  | **P9-12** Virage à droite sur la flèche | La voiture tourne à droite et repart. |
| ☐ | ☐ |  | **P9-13** Parcours complet | 30 → flèche → STOP sur le circuit au scotch, sans intervention. |

## P10 · Mesures et rendu

| L | J | É | Étape | Test |
| --- | --- | --- | --- | --- |
| ☐ | ☐ |  | **P10-01** 10 passages mesurés | Taux de réussite chiffré et causes d'échec notés dans docs/resultats.md. |
| ☐ | ☐ |  | **P10-02** Câblage et caméra fixés proprement | On secoue la voiture : rien ne se débranche. |
|  |  | ☐ | **P10-03** README de lancement | Quelqu'un d'extérieur relance une voiture avec le seul README. |
|  |  | ☐ | **P10-04** Vidéo de démo | Une vidéo montre un parcours complet de chaque voiture. |
|  |  | ☐ | **P10-05** Rapport rédigé | Le rapport couvre architecture, cycle IA, résultats et limites. |
|  |  | ☐ | **P10-06** Diaporama prêt | Le diaporama tient dans le temps imparti. |
|  |  | ☐ | **P10-07** Soutenance répétée | Une répétition chronométrée faite à deux. |
