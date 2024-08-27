from RF24 
import *from time 
import sleep
# Setup radio and GPIO pins

radio = RF24(22, 0)  # CE is connected to GPIO 22, CSN to CE0 (GPIO 8)
address = [b"00001"]  # Must match the address in the transmitterradio.begin()
radio.setPALevel(RF24.PA_MIN)
radio.setDataRate(RF24.RF24_250KBPS)
radio.openReadingPipe(1, address[0])
radio.startListening()

while True:
    if radio.available():        
        received_payload = radio.read(radio.getDynamicPayloadSize())
        data1 = received_payload[0]        
        data2 = chr(received_payload[1])
        print(f"Data1: {data1}, Data2: {data2}")    
    else:
        print("No data received")    
sleep(1)