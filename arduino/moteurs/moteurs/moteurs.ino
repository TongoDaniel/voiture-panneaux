const int ENA = 5;   // PWM vitesse côté gauche
const int IN1 = 4;
const int IN2 = 7;
const int IN3 = 8;
const int IN4 = 9;
const int ENB = 6;   // PWM vitesse côté droit

int vitesseGauche = 180;
int vitesseDroite = 180;

// P2-04 — Les 2 roues gauches tournent vers l'avant.
void gaucheAvant() {
  // un pont en H choisit le sens avec deux entrées opposées.
  // IN1 et IN2 ne doivent jamais avoir la même valeur pour tourner.
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, HIGH);
}

// P2-05 — Les 2 roues gauches tournent vers l'arrière.
void gaucheArriere() {
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
}

// P2-06 — Les 2 roues droites tournent vers l'avant.
void droiteAvant() {
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, HIGH);
}

// P2-07 — Les 2 roues droites tournent vers l'arrière.
void droiteArriere() {
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);
}

// Applique une vitesse (0 à 255) à chaque côté.
void reglerVitesse(int gauche, int droite) {
  // Test P2-08 : essaie 100, 180, 255 et écoute la différence.
  analogWrite(ENA, gauche);
  analogWrite(ENB, droite);
}

// P2-13 — Les 4 roues s'arrêtent immédiatement.
void stop() {
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, LOW);
  
  // analogWrite(ENA, 0);
  // analogWrite(ENB, 0);
}

// P2-09 — Avancer.
void avancer() {
  gaucheAvant();
  droiteAvant();
}

// P2-10 — Reculer.
void reculer() {
  gaucheArriere();
  droiteArriere();
}

// P2-11 — Pivoter à gauche sur place.
void tournerGauche() {
  gaucheArriere();
  droiteAvant();
}

// P2-12 — Pivoter à droite sur place.
void tournerDroite() {
  gaucheAvant();
  droiteArriere();
}


void setup() {
  Serial.begin(9600);

  pinMode(ENA, OUTPUT);
  pinMode(ENB, OUTPUT);
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);

}

void loop() {
  // reglerVitesse(255, 255);
  // Serial.println("Gauche");
  // tournerGauche();
  // delay(5000);

  // reglerVitesse(180, 180);
  // Serial.println("Droite");
  // tournerDroite();
  // delay(5000);
}