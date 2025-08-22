
void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);

}

void loop() {
  // put your main code here, to run repeatedly:
  String json_data = "{\"ac_eje_x\":\"" + String(random(1,10)) + "\",\"ac_eje_y\":\"" + String(random(11,20)) + "\" ,\"ac_eje_z\":\"" + String(random(21,30)) + "\"}";

  Serial.println(json_data);  
  delay(50);
}
