// =====================================================================
//  moteurs.ino — Pilotage des 4 moteurs via le L298N (étapes P2)
//  Commandes à taper dans le moniteur série (9600 bauds) :
//    F = avancer   B = reculer   L = pivoter gauche   R = pivoter droite
//    S = stop      1 / 2 / 3 = vitesse lente / moyenne / max
//    T = séquence de test (chaque mouvement 2 s, puis stop)
// =====================================================================

// --- Broches L298N -> Arduino (voir README) ---------------------------
const int ENA = 5;   // PWM : vitesse côté gauche  (broche marquée ~)
const int IN1 = 4;   // sens côté gauche
const int IN2 = 7;   // sens côté gauche
const int IN3 = 8;   // sens côté droit
const int IN4 = 9;   // sens côté droit
const int ENB = 6;   // PWM : vitesse côté droit   (broche marquée ~)

// --- Vitesses (0 = arrêt, 255 = plein régime) -------------------------
// Si la voiture dévie en ligne droite (P2-14), baisse le côté le plus rapide.
int vitesseGauche = 180;
int vitesseDroite = 180;

// --- Sens de chaque côté ----------------------------------------------
// Un pont en H choisit le sens avec deux entrées opposées :
//   IN1=LOW, IN2=HIGH -> un sens ; IN1=HIGH, IN2=LOW -> l'autre sens.
// Si une roue tourne à l'envers, inverse les deux fils de CE moteur
// sur le bornier du L298N (OUT1/OUT2 ou OUT3/OUT4), pas le code.

// P2-04
void gaucheAvant()   { digitalWrite(IN1, LOW);  digitalWrite(IN2, HIGH); }
// P2-05
void gaucheArriere() { digitalWrite(IN1, HIGH); digitalWrite(IN2, LOW);  }
// P2-06
void droiteAvant()   { digitalWrite(IN3, LOW);  digitalWrite(IN4, HIGH); }
// P2-07
void droiteArriere() { digitalWrite(IN3, HIGH); digitalWrite(IN4, LOW);  }

// P2-08 — envoie la vitesse au L298N. Sans cet appel, ENA/ENB restent
// à 0 et les moteurs ne tournent pas (jumpers ENA/ENB retirés).
void appliquerVitesse() {
  analogWrite(ENA, vitesseGauche);
  analogWrite(ENB, vitesseDroite);
}

// P2-09
void avancer()       { appliquerVitesse(); gaucheAvant();   droiteAvant();   }
// P2-10
void reculer()       { appliquerVitesse(); gaucheArriere(); droiteArriere(); }
// P2-11 — gauche en arrière, droite en avant : pivote à gauche
void tournerGauche() { appliquerVitesse(); gaucheArriere(); droiteAvant();   }
// P2-12
void tournerDroite() { appliquerVitesse(); gaucheAvant();   droiteArriere(); }

// P2-13 — coupe le sens ET la vitesse : arrêt immédiat
void stop() {
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, LOW);
  analogWrite(ENA, 0);
  analogWrite(ENB, 0);
}

// Séquence pour valider P2-09 à P2-12 d'un coup
void sequenceTest() {
  Serial.println("Avancer 2 s");        avancer();       delay(2000); stop(); delay(1000);
  Serial.println("Reculer 2 s");        reculer();       delay(2000); stop(); delay(1000);
  Serial.println("Pivot gauche 2 s");   tournerGauche(); delay(2000); stop(); delay(1000);
  Serial.println("Pivot droite 2 s");   tournerDroite(); delay(2000); stop();
  Serial.println("Fin du test");
}

void reglerVitesse(int v) {
  vitesseGauche = v;
  vitesseDroite = v;
  Serial.print("Vitesse = ");
  Serial.println(v);
}

// P2-15 — traduit une lettre en mouvement
void executer(char c) {
  switch (c) {
    case 'F': Serial.println("Avancer");      avancer();       break;
    case 'B': Serial.println("Reculer");      reculer();       break;
    case 'L': Serial.println("Pivot gauche"); tournerGauche(); break;
    case 'R': Serial.println("Pivot droite"); tournerDroite(); break;
    case 'S': Serial.println("Stop");         stop();          break;
    case '1': reglerVitesse(100); break;
    case '2': reglerVitesse(180); break;
    case '3': reglerVitesse(255); break;
    case 'T': sequenceTest();     break;
    default:
      Serial.print("Commande inconnue : ");
      Serial.println(c);
  }
}

void setup() {
  pinMode(ENA, OUTPUT);
  pinMode(ENB, OUTPUT);
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);
  stop();                       // sécurité : rien ne bouge au démarrage

  Serial.begin(9600);
  Serial.println("Pret. F B L R S, 1 2 3 (vitesse), T (test)");
}

void loop() {
  if (Serial.available() > 0) {
    char c = Serial.read();
    if (c == '\n' || c == '\r' || c == ' ') return;  // ignore les fins de ligne
    executer(toupper(c));                            // f ou F, pareil
  }
}
