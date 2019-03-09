void setup() {
        Serial.begin(115200);     // opens serial port, sets baudrate to 9600 bps
}

void loop() {
  
            // sends data only when data is recieved
        if (Serial.available() > 0) {
                // read the incoming byte:
                incomingByte = Serial.read();

                Serial.print("Received: ");
                Serial.println(incomingByte, DEC);
        }
}
