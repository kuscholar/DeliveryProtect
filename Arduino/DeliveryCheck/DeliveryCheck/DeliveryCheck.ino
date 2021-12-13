#include <SPI.h>
#include <Ethernet.h>
#define THRESHOLD 150

unsigned char fsr = 0;
int check_pressure = 0;
int action = 0; // action 0 represents package delivered
// action 1 represents package taken
boolean is_delivered = true;
boolean email_sent = false; // delivered email sent
boolean email_sent2 = false; // taken email sent
byte mac[] = { 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xEE }; //arduino mac
char server[] = "192.168.1.6"; // 1.6 is raspberry (server)
IPAddress ip(192,168,1,2); // 1.7 is Arduino IP
EthernetClient client;

void setup() {
  Serial.begin(9600);
  Ethernet.begin(mac, ip);
  pinMode(fsr, INPUT);
}

void loop() {
  check_pressure = analogRead(fsr);
  if(check_pressure > 20)
    Serial.println(check_pressure);
  if (!action){
    if(check_pressure >= THRESHOLD){
      if(!email_sent) {
        notify_parcel();
        email_sent2 = false;
        Serial.println("press");
      }
      email_sent = true;
      action = 1;
    }
  }
  else{
    if(check_pressure < THRESHOLD){
      if(!email_sent2) {
        notify_parcel();
        email_sent = false;
        Serial.println("release");
      }
      email_sent2 = true;
      action = 0;
    }
  }
}

void notify_parcel() {
  //String data = "{\"room\":";
  //data += room;
  //data += "}";
  String data = "";
  data += action;
  if (client.connect(server, 8081)) {
    Serial.println("connected");
    client.println("POST / HTTP/1.1");
    client.println("Host: 192.168.1.6");
    client.println("Content-Type: application/json;charset=utf-8");
    client.print("Content-Length: ");
    client.println(data.length());
    client.println();
    client.println(data);
    client.println("Connection: close");
    client.println();
  }
  else {
    Serial.println("connection failed");
  }
}
