const int ledPin=13;
int ledstate=LOW;
long previousTime=0;
long interval=60000; //un minuto

void setup() {
  pinMode(ledPin, OUTPUT);
}
void loop()
{
  unsigned long currenTime=millis();
  if(currentTime-previousTime>interval)
    {
    //imprimir en terminal la hora
    previousTime=currenTime;
    if (leadState==LOW)
     leadstate=HIGH;
    else
     leadstate=LOW;
    digita;write(ledPind,ledState); 
     
    }
}
