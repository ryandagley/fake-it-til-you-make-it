int state = HIGH;
int reading;
int previous = LOW;

long time = 0;
long debounce = 200;

void setup() {
  // put your setup code here, to run once:
    pinMode(3,OUTPUT);
    pinMode(4,OUTPUT);
    pinMode(5,OUTPUT);
    pinMode(2,INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:

    reading = digitalRead(2);
  if (reading == HIGH && previous == LOW && millis() - time > debounce) {
  // the button is not pressed
    if (state == HIGH){
      digitalWrite(3, HIGH);
      digitalWrite(4, LOW);
      digitalWrite(5, LOW); //green LED
      state = LOW;}
    else
      { state = HIGH;
      digitalWrite(3, LOW);
      digitalWrite(4, HIGH);  //red LED
      digitalWrite(5, HIGH); } //red LED

    time = millis();
  }
  
  previous = reading;
}
