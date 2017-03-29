//----Begin Code (copy from here)----
//Includes:
#include <OneWire.h>
//includes the functions needed to communicate with the 1-wire protocol
#include <DallasTemperature.h> //includes conversion functions from F to C etc, as well as the actual code to talk to the sensor.
//Variables:
OneWire oneWire(7); //Set the One Wire Data bus on pin 7.
DallasTemperature sensor(&oneWire); //This is passing a reference to the sensor object. This isnt commonly needed.

void setup() {
// put your setup code here, to run once:
Serial.begin(9600);
sensor.begin(); //Begin talking to the sensor
}

void loop() {
sensor.requestTemperatures(); //Request temperatures from the sensor
Serial.print(sensor.getTempCByIndex(0)); //populate the temperature reading.
Serial.println();     //Temperatura en °C
//print "Temp: "
delay(60000); //en milisegundos. 1000milisegundos=1seg
}
//----End Code (copy to here)----
