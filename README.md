# DeliveryProtect
This project builds a delivery protection and notification system, based on integration of Arduino Uno and Raspberry Pi 4. The codes are written in C and Python. 
The setup of the system requires:

1. Arduino Uno with Ethernet Sheild
2. Raspberry Pi 4 (or other available versions)
3. A router
4. A force sensor
5. A bread board
6. A 10K ohm resistor
7. jumper wires
8. Two cameras with USB connections (I used web cams)

## Work flow
1. Setup the hardware system referring to the picture and the report.
2. Upload the DeliveryCheck.ino script to the Arduino Board.
3. Run python webservice.py in Raspberry Pi terminal window.
4. Place an item on the force sensor, an email with picture should be sent to the receiver email address; when it is taken, another email with picture will be sent.

### Demo setup
<img src = "https://github.com/kuscholar/DeliveryProtect/blob/498b877c8568a44f29d20fc1520d0a3c96791e8f/Setup.jpg">
