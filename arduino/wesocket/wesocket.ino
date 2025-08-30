/*

Este Codigo fue creado por el Ingeniero Edgar Danilo Morillo Gordillo.
por lo tanto todos los derechos por ley nacional e internacional son 100% del creador y autor 
hasta que se firme un documento legalmente diciendo que los derechos son de otra persona o entidad institucional

para mas informacion, trabajos y colaboraciones comunicarse por correo o por Github
https://github.com/Edgar-Danilo/Mesa-Sismica

ingmoriot@gmail.com

*/
//#include <AsyncTCP.h>
//#include <ESPAsyncWebServer.h>
//#include <WebSerial.h>
#include <WiFi.h>
#include <ArduinoWebsockets.h>
#include <ArduinoJson.h>

using namespace websockets;
const char* ssid = "Redmi Note 13";           // Cambia por el nombre de tu red WiFi
const char* password = "123456789"; 
//const char* websocket_server = "10.173.203.247"; // Cambia por la IP de tu PC

#define LED 2

String mensaje = "";
WebsocketsClient client;

JsonDocument doc;


void onMessageCallback(WebsocketsMessage message) {
  Serial.print("Mensaje recibido: ");
  Serial.println(message.data());
  mensaje = message.data();
  
}


void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);

  Serial.print("Conectando a WiFi");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nConectado a WiFi");

  // Conectar al servidor WebSocket
  while (!client.connect("10.195.118.247", 8765, "/")){
    Serial.println("No se pudo conectar al servidor WebSocket conectando .............");
    }
  Serial.println("COnectado a wesocket");
  client.onMessage(onMessageCallback);
}

void loop() {
  
  client.poll();  // Mantiene la conexión viva
  int numero = random(0, 101);

  //String comando = Serial.readStringUntil('\n'); // Lee la orden
  //comando.trim(); // Quita espacios o saltos de línea
  //int valor = comando.toInt(); // Convierte a núme
  //prender_led(valor*10);
  //analogWrite(ledPin, map(comando.toInt(),0,100,0,255));
  //doc["distancia_ejex"] = random(0,20);
  doc["distancia_ejex"] = mensaje;
  doc["aceleracion_ejex"] = random(0,20);
  doc["aceleracion_ejey"] = random(20,50);
  doc["aceleracion_ejez"] = random(50,100);

  String output;
  serializeJson(doc, output);

  //Serial.println(output);
  
  
  // Convertir a String para enviarlo
  client.send(output);
  delay(10);
}