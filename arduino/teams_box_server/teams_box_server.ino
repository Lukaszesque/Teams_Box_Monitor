#include <WiFi.h>
#include <WebServer.h>

//WiFi credentials
const char* ssid     = ""; //Your Wifi ssid
const char* password = ""; //Your Wifi password

//LED pins
const int PIN_ONLINE = 21;
const int PIN_CALL   = 22;
const int PIN_MIC    = 18;
const int PIN_CAMERA = 19;

// Heartbeat Watchdog
unsigned long lastHeartbeat = 0;
const unsigned long WATCHDOG_TIMEOUT = 3000; 

WebServer server(80);

void handleHeartbeat() {
  lastHeartbeat = millis();
  server.send(200, "text/plain", "OK");
 }

void handleUpdate() {
 bool call   = server.arg("call")   == "1";
 bool mic    = server.arg("mic")    == "1";
 bool camera = server.arg("camera") == "1";

 Serial.printf("[update] call=%d mic=%d camera=%d\n", call, mic, camera);

 digitalWrite(PIN_CALL,   call   ? HIGH : LOW);
 digitalWrite(PIN_MIC,    mic    ? HIGH : LOW);
 digitalWrite(PIN_CAMERA, camera ? HIGH : LOW);

 server.send(200, "text/plain", "ok");
 }




void setup() {
  Serial.begin(115200);

  pinMode(PIN_ONLINE, OUTPUT);
  pinMode(PIN_CALL,   OUTPUT);
  pinMode(PIN_MIC,    OUTPUT);
  pinMode(PIN_CAMERA, OUTPUT);

  //Connect to WiFi
  Serial.printf("Connection to %s", ssid);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
    }

  Serial.println(" connected!");
  Serial.print("IP address:");
  Serial.println(WiFi.localIP());

  //Register endpoints
  server.on("/heartbeat", handleHeartbeat);
  server.on("/update",    handleUpdate);
  server.begin();

  lastHeartbeat = millis();
  Serial.println("Server started!");
}

void loop() {
  server.handleClient();

  //Heartbeat check
  if (millis() - lastHeartbeat > WATCHDOG_TIMEOUT) {
    digitalWrite(PIN_ONLINE, LOW);
    } else {
    digitalWrite(PIN_ONLINE, HIGH);
    }

}
