# Import SDK packages
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import serial
from rpi_lcd import LCD
from time import sleep

# Get serial to fetch data from arduino
ser = serial.Serial('/dev/ttyUSB0', 9600)
lcd = LCD()

def customCallback(client, userdata, message):
	print("Received a new message: ")
	print(message.payload)
	print("from topic: ")
	print(message.topic)
	print("--------------\n\n")
	
host = "YOUR HOST NAME"
rootCAPath = "rootca.pem"
certificatePath = "certificate.pem.crt"
privateKeyPath = "private.pem.key"

my_rpi = AWSIoTMQTTClient("basicPubSub")
my_rpi.configureEndpoint(host, 8883)
my_rpi.configureCredentials(rootCAPath, privateKeyPath, certificatePath)

my_rpi.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
my_rpi.configureDrainingFrequency(2)  # Draining: 2 Hz
my_rpi.configureConnectDisconnectTimeout(10)  # 10 sec
my_rpi.configureMQTTOperationTimeout(5)  # 5 sec

# Connect and subscribe to AWS IoT
my_rpi.connect()
my_rpi.subscribe("smartgarden/readings", 1, customCallback)
lcd.text("  SMART GARDEN  ", 1)
lcd.text("* Welcome back *", 2)
sleep(2)
lcd.clear()

# Publish to the same topic in a loop forever
loopCount = 0
while True:
	temp = float(ser.readline())
	hum = float(ser.readline())
	soil = int(ser.readline())
	light = int(ser.readline())

	lcd.text('Humidity: {:.2f}%'.format(hum), 1)
	lcd.text('Temp: {:.2f} C'.format(temp), 2)
	sleep(2)
	lcd.clear()

	lcd.text('Moisture: {:d}'.format(soil), 1)
	lcd.text('Light Level: {:d} C'.format(light), 2)
	sleep(2)
	lcd.clear()

	loopCount = loopCount+1
	message = {}
	message["id"] = "id_smartgarden"
	import datetime as datetime
	now = datetime.datetime.now()
	message["datetimeid"] = now.isoformat()      
	message["temperature"] = temp
	message["humidity"] = hum
	message["moisture"] = soil
	message["light"] = light
	import json
	my_rpi.publish("smartgarden/readings", json.dumps(message), 1)