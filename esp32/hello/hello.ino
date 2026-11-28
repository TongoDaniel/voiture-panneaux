//hello.ino : étape P3-01
void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);

}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.print("hello, PSRAM libre : ");
  Serial.print(ESP.getFreePsram());
  Serial.print(" octects");
  delay(1000);

}
