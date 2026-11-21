// ============================================================
//  moteurs.ino — SQUELETTE à compléter (étapes P2-04 à P2-15)
//  Arduino Uno + L298N, voiture 4WD
//
//  Principe : chaque fonction correspond à une étape de docs/ETAPES.md.
//  Remplis-les une par une, dans l'ordre, et teste chaque fonction
//  seule (roues en l'air) avant de passer à la suivante.
//
//  Le squelette compile tel quel : les fonctions vides ne font rien.
// ============================================================

// ---------- Brochage (README, section « L298N vers Arduino ») ----------
// Hypothèse : moteur A (ENA, IN1, IN2) = côté GAUCHE,
//             moteur B (ENB, IN3, IN4) = côté DROIT.
// Si c'est l'inverse sur ta voiture, échange les fils moteurs
// sur le bornier du L298N plutôt que de modifier le code.
const int ENA = 5;   // PWM vitesse côté gauche
const int IN1 = 4;
const int IN2 = 7;
const int IN3 = 8;
const int IN4 = 9;
const int ENB = 6;   // PWM vitesse côté droit

// Rappel : retire les jumpers ENA/ENB du L298N, sinon le PWM ne sert à rien.

// ---------- Réglages ----------
// TODO (P2-08) : choisis une vitesse de départ entre 0 et 255.
// Indice : en dessous d'environ 80 à 100, les moteurs peuvent bourdonner sans tourner.
int vitesseGauche = 0;
int vitesseDroite = 0;
// P2-14 : si la voiture dévie, tu corrigeras l'une des deux valeurs ci-dessus.


// ============================================================
//  1. Un côté, un sens (P2-04 à P2-07)
// ============================================================

// P2-04 — Les 2 roues gauches tournent vers l'avant.
void gaucheAvant() {
  // TODO
  // Indice : un pont en H choisit le sens avec deux entrées opposées.
  // IN1 et IN2 ne doivent jamais avoir la même valeur pour tourner.
  // Fonction utile : digitalWrite(broche, HIGH ou LOW).
}

// P2-05 — Les 2 roues gauches tournent vers l'arrière.
void gaucheArriere() {
  // TODO
  // Indice : c'est gaucheAvant() avec IN1 et IN2 inversés.
}

// P2-06 — Les 2 roues droites tournent vers l'avant.
void droiteAvant() {
  // TODO
  // Indice : même logique avec IN3 et IN4.
  // Si les roues tournent à l'envers, inverse HIGH/LOW ici (pas les fils).
}

// P2-07 — Les 2 roues droites tournent vers l'arrière.
void droiteArriere() {
  // TODO
}


// ============================================================
//  2. Vitesse (P2-08)
// ============================================================

// Applique une vitesse (0 à 255) à chaque côté.
void reglerVitesse(int gauche, int droite) {
  // TODO
  // Indice : analogWrite(broche, valeur) sur ENA et ENB.
  // Test P2-08 : essaie 100, 180, 255 et écoute la différence.
}


// ============================================================
//  3. Mouvements de la voiture (P2-09 à P2-13)
//  Indice général : chaque mouvement = une fonction de la partie 1
//  pour la gauche + une pour la droite + reglerVitesse().
// ============================================================

// P2-13 — Les 4 roues s'arrêtent immédiatement.
// (Écrite en premier : tu en as besoin pour tester les autres.)
void stop() {
  // TODO
  // Indice : deux façons de faire. Mettre la vitesse à 0 (roue libre),
  // ou mettre IN1 = IN2 (et IN3 = IN4) avec ENA/ENB actifs (freinage).
  // Essaie les deux et note la différence.
}

// P2-09 — Avancer.
void avancer() {
  // TODO
}

// P2-10 — Reculer.
void reculer() {
  // TODO
}

// P2-11 — Pivoter à gauche sur place.
void tournerGauche() {
  // TODO
  // Indice : roues gauches en arrière, roues droites en avant.
}

// P2-12 — Pivoter à droite sur place.
void tournerDroite() {
  // TODO
}


// ============================================================
//  4. Commande par le moniteur série (P2-15)
// ============================================================

// Exécute la commande reçue : F, B, L, R ou S.
void executerCommande(char c) {
  // TODO
  // Indice : un switch (c) { case 'F': ... break; ... }
  // Pense au cas par défaut : une lettre inconnue ne doit rien faire.
}


// ============================================================
//  setup / loop
// ============================================================

void setup() {
  Serial.begin(9600);

  // TODO : déclarer les 6 broches en sortie.
  // Indice : pinMode(broche, OUTPUT);

  stop();   // la voiture démarre toujours à l'arrêt
  Serial.println("Moteurs prets. Commandes : F B L R S");
}

void loop() {
  // --- Pendant P2-04 à P2-13 : tester une fonction à la fois ---
  // Exemple de test P2-09 (décommente quand avancer() est écrite) :
  // avancer();
  // delay(2000);
  // stop();
  // delay(3000);

  // --- À partir de P2-15 : lire le moniteur série ---
  // TODO
  // Indice : if (Serial.available() > 0) { char c = Serial.read(); ... }
  // Dans le moniteur série, choisis « Pas de fin de ligne »,
  // sinon les caractères \r et \n arrivent aussi.
}
