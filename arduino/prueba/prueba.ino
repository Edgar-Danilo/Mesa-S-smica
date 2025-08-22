
#include <ArduinoJson.h>




int ledPin = 13;
String opcion = "";
int valor;

void setup() {
  // put your setup code here, to run once:
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
}



void loop() {
  JsonDocument doc;
  // put your main code here, to run repeatedly:
  //doc["distancia_ejex"] = random(0,100);
  //doc["distancia_ejex"] = random(0,20);


  if (Serial.available() > 0) {
    String comando = Serial.readStringUntil('\n'); // Lee la orden
    comando.trim(); // Quita espacios o saltos de línea
    
    if (comando == "mover_mesa") {
      opcion = comando;
      
      while (opcion == "mover_mesa"){
        

        if (Serial.available() > 0) {
          //delay(50);
          
          String comando = Serial.readStringUntil('\n'); // Lee la orden
          comando.trim(); // Quita espacios o saltos de línea
          //int valor = comando.toInt(); // Convierte a núme
          //prender_led(valor*10);
          //analogWrite(ledPin, map(comando.toInt(),0,100,0,255));
          doc["distancia_ejex"] = map(comando.toInt(),0,100,-15,15);
          doc["aceleracion_ejex"] = random(0,20);
          doc["aceleracion_ejey"] = random(20,50);
          doc["aceleracion_ejez"] = random(50,100);

          String output;
          serializeJson(doc, output);

          Serial.println(output);
          //delay(50);

          if (comando == "salir"){
            opcion = comando;
          }
        }
      }
    }





    if (comando == "reproducir_sismo") {
      opcion = comando;
      
      while (opcion == "reproducir_sismo"){
        prender_led(500);

        if (Serial.available() > 0) {
          String comando = Serial.readStringUntil('\n'); // Lee la orden
          comando.trim(); // Quita espacios o saltos de línea
          if (comando == "salir"){
            opcion = comando;
          }
        }
      }
    }



    if (comando == "crear_sismo") {
      opcion = comando;
      
      while (opcion == "crear_sismo"){
        prender_led(900);

        if (Serial.available() > 0) {
          String comando = Serial.readStringUntil('\n'); // Lee la orden
          comando.trim(); // Quita espacios o saltos de línea
          if (comando == "salir"){
            opcion = comando;
          }
        }
      }
    }
    

  }
}

void prender_led(int valor){
  digitalWrite(ledPin, HIGH);
  delay(valor);
  digitalWrite(ledPin, LOW);
  delay(valor);
}

/*
    if (comando == "mover_mesa") {
      //digitalWrite(ledPin, HIGH);
      opcion = comando;
      
      
      while (opcion == "mover_mesa"){
        digitalWrite(ledPin, HIGH);
        //prender_led(250)
            //String comando = Serial.readStringUntil('\n'); // Lee la orden
            //comando.trim(); // Quita espacios o saltos de línea
            if (Serial.available() > 0) {
            String comando = Serial.readStringUntil('\n'); // Lee la orden
            comando.trim(); // Quita espacios o saltos de línea
            valor = comando.toInt(); // Convierte a número
            digitalWrite(ledPin, HIGH);
            //doc["distancia_ejex"] = valor;

            //prender_led(valor);
            if (comando == "salir"){
              opcion = comando;
            }
            delay(100);

          //int valor = comando.toInt(); // Convierte a núme
        }
        //prender_led(valor);
        
            
          doc["aceleracion_ejex"] = random(0,20);
          doc["aceleracion_ejey"] = random(20,50);
          doc["aceleracion_ejez"] = random(50,100);

          String output;
          serializeJson(doc, output);

          Serial.println(output);

          //Serial.println(valor);        // Envía dato por Serial
          delay(100);

          int valor;

          prender_led(valor*10);


      } 
    }*/
