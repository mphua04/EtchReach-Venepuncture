import random
import bluepy.btle as btle
import time

# TODO change if needed, need to match the ones in the esp32
NUS_SERVICE_UUID = '6e400001-b5a3-f393-e0a9-e50e24dcca9e'
UART_TX_UUID = "6e400002-b5a3-f393-e0a9-e50e24dcca9e" #Nordic NUS characteristic for TX
UART_RX_UUID = "6e400003-b5a3-f393-e0a9-e50e24dcca9e" #Nordic NUS characteristic for RX
 
 
class ReadDelegate(btle.DefaultDelegate):
    def handleNotification(self, cHandle, data):
        # print(cHandle)
        print(">>", data.decode("utf-8"))
 
 
p = btle.Peripheral("") # TODO need to input MAC address of esp32
p.withDelegate(ReadDelegate())
 
s = p.getServiceByUUID(NUS_SERVICE_UUID)
c = s.getCharacteristics()
for a in c:
    print(a)
 
time.sleep(0.5)
while True:
    p.waitForNotifications(0.200)
    if random.randint(0, 10) > 8:
        d = time.asctime()
        print(c[1].write(bytes(d+"\n", "utf-8")))
    time.sleep(0.1)
 
p.disconnect()


