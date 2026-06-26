//Basic Demonstration Code//

#define BLYNK_TEMPLATE_ID "YourTemplateID"
#define BLYNK_TEMPLATE_NAME "Temperature and Humidity Monitor"
#define BLYNK_AUTH_TOKEN "VwggdwB8p2iYRjWPHVE3cE96qWGCZI4X"
#define BLYNK_PRINT Serial
#include <WiFi.h>
#include <BlynkSimpleEsp32.h>
#include <DHT.h>
char auth[] = BLYNK_AUTH_TOKEN;
char ssid[] = "HONOR 90 Lite";
char pass[] = "56678709";
BlynkTimer timer;
#define DHTPIN 27
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);
void sendSensor()
{
float h = dht.readHumidity();
float t = dht.readTemperature();
if (isnan(h) || isnan(t)) {
Serial.println("Failed to read from DHT sensor!");
return;
}
Blynk.virtualWrite(V0, t);
Blynk.virtualWrite(V1, h);
Serial.print("Temperature : ");
Serial.print(t);
Serial.print(" Humidity : ");
Serial.println(h);
}
void setup()
{
Serial.begin(115200);
Blynk.begin(auth, ssid, pass);
dht.begin();
timer.setInterval(2000L, sendSensor); // FIXED
}
void loop()
{
Blynk.run();
timer.run();
}
