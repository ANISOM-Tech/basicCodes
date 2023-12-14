int x;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(13, OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.println("Hello MAC!!!!!!!!!!");
  while (!Serial.available());
  x = Serial.readString().toInt();
  Serial.println(x);
  if (x == 1){
    digitalWrite(13, HIGH);
  }else{
    digitalWrite(13, LOW);
  }
  Serial.flush();
  delay(100);

}
