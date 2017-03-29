//----Begin Code (copy from here)----
//Includes:
#include <DHT.h> //Please make sure you search for, and install the DHT11 library.
//Refer to the section on installing libraries for assistance.
//Variables:
DHT dht(7, DHT11); //Initialize the object for the sensor. Pin 7 in this case, and a DHT11 sensor.©Tyson Popynick 2016 for Aus Electronics Direct37 – in – 1 Sensor Kit
void setup() {
// put your setup code here, to run once:
Serial.begin(9600);
//Serial.println("Temp and Humidity (DHT11) demo by Tyson Popynick, please freely edit and use this code for anypurpose.\nprot3us1@gmail.com\n\n");
dht.begin(); //Begin communication with sensor
}
void loop() {
float humidity = dht.readHumidity();
//Read and store the humidity from the sensor
float temperature = dht.readTemperature(); //Read and store the temperature from the sensor (Celcius)
if (isnan(humidity) || isnan(temperature)) { //isnan means is not a number. If the data is coming back corrupt this should catch it
Serial.println("Error reading");
return; //This will return to the start of the loop without executing the code below.
}
float heatIndex = dht.computeHeatIndex(temperature,humidity,false); //Read and store the heat index from the sensor
//Serial.print("H");
//Serial.print(humidity);
Serial.print("\n");
Serial.print(temperature);
//Serial.print(" Heat Index: ");
//Serial.println(heatIndex); //Print all the values to the serial monitor
delay(2000);
//Wait 2 seconds so we arent scrolling the serial screen too fast.
}
//----End Code (copy to here)----
