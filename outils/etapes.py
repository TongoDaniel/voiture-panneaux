# Source unique des étapes : (id, titre, test, portée) ; portée "V" = à faire sur chaque voiture, "E" = une fois pour l'équipe
PHASES = [
("P0","Cadrage", [
 ("Mail de présentation envoyé au tuteur","Le mail apparaît dans tes messages envoyés.","E"),
 ("Date de rendu connue","La date est écrite dans docs/cadrage.md.","E"),
 ("Livrables et critères de notation connus","La liste est écrite dans docs/cadrage.md.","E"),
 ("Dépôt cloné par Lein","Lein a poussé un commit visible sur GitHub.","E"),
 ("Dépôt cloné par Jephte","Jephte a poussé un commit visible sur GitHub.","E"),
 ("Créneau de point hebdo fixé","Un rendez-vous récurrent est dans vos deux agendas.","E"),
 ("Réaction de chaque panneau définie","docs/perimetre.md dit quoi faire pour STOP, 30, gauche, droite.","E"),
 ("Architecture choisie (S3-CAM seule ou caméra + ESP32)","Le choix et la raison sont dans docs/perimetre.md.","E"),
]),
("P1","Matériel et alimentation", [
 ("Inventaire de la voiture vérifié","Chaque pièce de la liste du README est cochée comme présente.","V"),
 ("Batterie LiPo chargée","Le multimètre lit entre 8,3 et 8,4 V après charge équilibrée.","V"),
 ("Connecteur XT60 et interrupteur câblés sur la batterie","Interrupteur sur ON : tension présente en sortie ; sur OFF : 0 V.","V"),
 ("Buck LM2596 réglé à 5,0 V","Le multimètre lit 5,0 V (±0,1) en sortie, sans rien de branché.","V"),
 ("Châssis monté","Les 4 moteurs sont fixés et chaque roue tourne librement à la main.","V"),
]),
("P2","Moteurs", [
 ("Arduino IDE installé et carte Uno reconnue","L'exemple Blink fait clignoter la LED de la carte.","V"),
 ("L298N alimenté par la batterie","La LED du L298N s'allume quand tu bascules l'interrupteur.","V"),
 ("Arduino alimenté sans USB","L'Arduino s'allume sur batterie seule (VIN ou 5 V du L298N).","V"),
 ("Côté gauche avance","Roues en l'air, les 2 roues gauches tournent vers l'avant.","V"),
 ("Côté gauche recule","Les 2 roues gauches tournent vers l'arrière.","V"),
 ("Côté droit avance","Les 2 roues droites tournent vers l'avant.","V"),
 ("Côté droit recule","Les 2 roues droites tournent vers l'arrière.","V"),
 ("Vitesse réglable par PWM","Trois valeurs de analogWrite donnent trois vitesses distinctes à l'oreille et à l'œil.","V"),
 ("Fonction avancer()","Un appel fait avancer les 4 roues 2 s puis stop.","V"),
 ("Fonction reculer()","Un appel fait reculer les 4 roues 2 s puis stop.","V"),
 ("Fonction tournerGauche()","Roues gauches en arrière, droites en avant : la voiture pivote à gauche.","V"),
 ("Fonction tournerDroite()","La voiture pivote à droite sur place.","V"),
 ("Fonction stop()","Les 4 roues s'arrêtent immédiatement.","V"),
 ("Ligne droite au sol","Sur 2 m, la voiture dévie de moins de 20 cm (sinon corriger le PWM d'un côté).","V"),
 ("Commande par le moniteur série USB","Taper F, B, L, R, S dans le moniteur série déclenche le bon mouvement.","V"),
]),
("P3","Liaison ESP32 et Arduino", [
 ("Cartes ESP32 installées dans l'IDE","Un sketch qui écrit « hello » toutes les secondes s'affiche dans le moniteur série de l'ESP32.","V"),
 ("Diviseur de tension monté (1 kΩ / 2 kΩ)","Avec 5 V en entrée, le multimètre lit environ 3,3 V au point milieu.","V"),
 ("GND communs Arduino, L298N, ESP32","Le multimètre en mode continuité bipe entre les trois GND.","V"),
 ("ESP32 envoie un message à l'Arduino","Le moniteur de l'Arduino affiche « PING » reçu de l'ESP32.","V"),
 ("Arduino répond à l'ESP32","Le moniteur de l'ESP32 affiche « PONG ».","V"),
 ("Protocole de commande lu par l'Arduino","Une chaîne comme F150 est découpée en lettre F et vitesse 150 (affichées).","V"),
 ("Commande ESP32 qui fait bouger la voiture","F150 tapé côté ESP32 fait avancer la voiture.","V"),
 ("Watchdog sur l'Arduino","Sans nouvelle commande pendant 500 ms, la voiture s'arrête seule.","V"),
]),
("P4","Pilotage Wi-Fi depuis le PC", [
 ("Point d'accès Wi-Fi propre à la voiture","Le PC voit et rejoint le réseau (TNG_Car_L pour Lein, TNG_Car_J pour Jephte).","V"),
 ("ESP32 répond au PC","Un ping vers 192.168.4.1 répond, ou une page « ok » s'affiche dans le navigateur.","V"),
 ("Script Python qui envoie une commande","python envoyer.py F150 fait avancer la voiture.","V"),
 ("Pilotage au clavier","Les flèches du clavier pilotent la voiture, relâcher = stop.","V"),
 ("Arrêt sur perte du Wi-Fi","Tu coupes le Wi-Fi du PC en roulant : la voiture s'arrête en moins d'1 s.","V"),
 ("Deux voitures en même temps","Les deux voitures roulent dans la même pièce sans se brouiller (canaux Wi-Fi différents).","E"),
]),
("P5","Caméra", [
 ("Caméra alimentée par le buck 5 V","Le moniteur série ne montre aucun redémarrage en boucle pendant 2 min.","V"),
 ("Image de la caméra dans le navigateur","L'exemple CameraWebServer affiche une image nette.","V"),
 ("Flux lu par Python et OpenCV","Une fenêtre OpenCV affiche le flux en direct.","V"),
 ("Fps et délai mesurés","Les deux chiffres sont notés dans docs/mesures.md (filmer un chronomètre).","V"),
 ("Caméra fixée sur la voiture","Hauteur et angle ne bougent plus quand la voiture roule.","V"),
 ("Flux et commandes en même temps","Tu pilotes au clavier tout en voyant le flux, sans coupure.","V"),
]),
("P6","Bases de l'IA", [
 ("Environnement Python prêt (venv, ultralytics, opencv)","import ultralytics, cv2 ne donne aucune erreur.","E"),
 ("YOLOv8n pré-entraîné sur une photo","Une photo avec une personne ressort avec une boîte « person ».","E"),
 ("YOLOv8n pré-entraîné sur la webcam","Une tasse ou une personne est détectée en direct.","E"),
 ("YOLOv8n pré-entraîné sur le flux de la voiture","La détection marche aussi sur l'image de la voiture.","V"),
 ("Fiche des concepts IA","docs/concepts.md explique train/val/test, précision, rappel, IoU, mAP, surapprentissage, et chacun l'explique sans notes.","E"),
]),
("P7","Données", [
 ("Panneaux imprimés et montés","8 panneaux (4 classes × 2 tailles) sur papier mat et carton, qui tiennent debout.","E"),
 ("Script de capture d'images","Une touche enregistre une image horodatée dans un dossier de session.","E"),
 ("Session de capture n°1","Au moins 30 images par classe, prises avec ta voiture, décor et lumière notés.","V"),
 ("Session de capture n°2","Au moins 30 images par classe, autre décor ou autre lumière.","V"),
 ("Images sans panneau","Au moins 40 images de décor vide avec ta voiture.","V"),
 ("Projet d'annotation créé (Roboflow ou CVAT)","Les 4 classes existent et les deux comptes y ont accès.","E"),
 ("Images de Lein annotées","Chaque image de Lein a ses boîtes, ou est marquée « vide ».","E"),
 ("Images de Jephte annotées","Chaque image de Jephte a ses boîtes, ou est marquée « vide ».","E"),
 ("Contrôle de 20 annotations au hasard","Aucune boîte fausse ou oubliée sur les 20.","E"),
 ("Découpage train / val / test par session","Aucune session n'apparaît dans deux jeux à la fois.","E"),
 ("Export au format YOLOv8","Le dossier contient data.yaml et le tableau des effectifs par classe est dans docs/donnees.md.","E"),
]),
("P8","Entraînement et évaluation", [
 ("Notebook Colab qui charge le jeu de données","Le notebook affiche le nombre d'images par jeu, GPU actif.","E"),
 ("Entraînement court sans erreur","5 epochs se terminent et produisent un best.pt.","E"),
 ("Entraînement complet v1","best.pt v1 sauvegardé avec ses paramètres notés.","E"),
 ("Courbes d'apprentissage lues","La perte de validation ne remonte pas en fin d'entraînement (sinon surapprentissage).","E"),
 ("Scores sur le jeu de test","mAP50, précision et rappel par classe notés dans docs/resultats.md.","E"),
 ("Matrice de confusion analysée","Les confusions principales sont listées avec un exemple d'image.","E"),
 ("Images ajoutées pour les erreurs","Une nouvelle session cible les cas ratés.","E"),
 ("Entraînement v2","mAP50 de v2 supérieure à v1 sur le même jeu de test (viser > 0,85).","E"),
]),
("P9","Intégration temps réel", [
 ("Modèle entraîné sur le flux de la voiture","Les 4 panneaux sont reconnus en direct, boîtes affichées.","V"),
 ("Filtre de confiance minimale","En dessous du seuil (ex. 0,6), rien n'est pris en compte.","E"),
 ("Filtre 3 images d'affilée","Un panneau vu sur une seule image ne déclenche rien.","E"),
 ("Seuil de distance par taille de boîte","Un panneau lointain est ignoré, proche il est pris en compte.","E"),
 ("Machine à états de décision","À l'arrêt, le script affiche ROULE, RALENTI, ARRET ou VIRAGE selon le panneau montré.","E"),
 ("Délai de réarmement","Le même panneau ne déclenche pas deux fois en moins de 3 s.","E"),
 ("Commandes envoyées, roues en l'air","Chaque panneau montré déclenche le bon mouvement des roues.","V"),
 ("Latence de la boucle mesurée","Image → commande reçue en moins de 300 ms, chiffre noté.","V"),
 ("Arrêt au STOP au sol","À vitesse réduite, la voiture s'arrête avant le panneau STOP.","V"),
 ("Ralentissement au 30","La voiture ralentit à la vue du 30 puis reprend.","V"),
 ("Virage à gauche sur la flèche","La voiture tourne à gauche et repart.","V"),
 ("Virage à droite sur la flèche","La voiture tourne à droite et repart.","V"),
 ("Parcours complet","30 → flèche → STOP sur le circuit au scotch, sans intervention.","V"),
]),
("P10","Mesures et rendu", [
 ("10 passages mesurés","Taux de réussite chiffré et causes d'échec notés dans docs/resultats.md.","V"),
 ("Câblage et caméra fixés proprement","On secoue la voiture : rien ne se débranche.","V"),
 ("README de lancement","Quelqu'un d'extérieur relance une voiture avec le seul README.","E"),
 ("Vidéo de démo","Une vidéo montre un parcours complet de chaque voiture.","E"),
 ("Rapport rédigé","Le rapport couvre architecture, cycle IA, résultats et limites.","E"),
 ("Diaporama prêt","Le diaporama tient dans le temps imparti.","E"),
 ("Soutenance répétée","Une répétition chronométrée faite à deux.","E"),
]),
]

def etapes():
    out=[]
    for pid,pname,items in PHASES:
        for i,(t,test,s) in enumerate(items,1):
            out.append(dict(id=f"{pid}-{i:02d}",phase=pid,phaseNom=pname,titre=t,test=test,portee=s))
    return out
if __name__=="__main__":
    import json,sys
    e=etapes(); print(len(e), sum(x['portee']=='V' for x in e))
    json.dump(e,open(sys.argv[1],"w"),ensure_ascii=False,indent=1)
