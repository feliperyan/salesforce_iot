#include "rdm630.h"
#include <SoftwareSerial.h>


rdm630 rfid(2, 0);  //TX-pin of RDM630 connected to Arduino pin 6

void setup()
{
    Serial.begin(9600);  // start serial to PC
    rfid.begin();
}

void loop()
{
    byte data[6];
    byte length;

    if(rfid.available()){
        rfid.getData(data,length);
        Serial.println("Data valid");
        for(int i=0;i<length;i++){
            Serial.print(data[i],HEX);
        }
        Serial.println();
        delay(1000);
        Serial.flush();
    }
}
