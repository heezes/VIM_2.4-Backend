'''AIzaSyCa6J78wyGq8_e9lLkR4PY3vsKIu183WaQ'''
import gmplot
import webbrowser
import csv
import Tkinter
import paho.mqtt.client as mqtt
import time
import ssl 
import json

'''
MQTT_PORT = 8883
MQTT_KEEPALIVE_INTERVAL = 30
MQTT_TOPIC = "VIM_2.4_4/publish/data"

MQTT_HOST = "*********.iot.ap-southeast-1.amazonaws.com"
CA_ROOT_CERT_FILE = "root.crt"
THING_CERT_FILE = "certificate.pem.crt"
THING_PRIVATE_KEY = "private.pem.key"

# Define on connect event function
# We shall subscribe to our Topic in this function
def on_connect(self, mosq, obj, rc):
    mqttc.subscribe(MQTT_TOPIC, 0)

# Define on_message event function. 
# This function will be invoked every time,
# a new message arrives for the subscribed topic 
def on_message(mosq, obj, msg):
	#print "Topic: " + str(msg.topic)
	#print "QoS: " + str(msg.qos)
	#print "Payload: " + str(msg.payload)
	payload_dict = str(msg.payload)
	print(payload_dict)

def on_subscribe(mosq, obj, mid, granted_qos):
    print("Subscribed to Topic: " + 
	MQTT_TOPIC + " with QoS: " + str(granted_qos))

# Initiate MQTT Client
mqttc = mqtt.Client()

# Assign event callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe

# Configure TLS Set
mqttc.tls_set(CA_ROOT_CERT_FILE, certfile=THING_CERT_FILE, keyfile=THING_PRIVATE_KEY, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)


# Connect with MQTT Broker
mqttc.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)

# Continue monitoring the incoming messages for subscribed topic
mqttc.loop_forever()

'''
data_list = []
latitude_list = []
longitude_list = []

with open('DRIVE_CYCLE_DATA_1.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    line_count = 0
    data = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            data = row["LAT_LON (S)"]
            lat, lon  = data.split(",")
            latitude_list.append(float(lat))
            longitude_list.append(float(lon))
            line_count += 1
    print('Processed {} lines.'.format(line_count))
with open('DRIVE_CYCLE_DATA_2.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    line_count = 0
    data = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            data = row["LAT_LON (S)"]
            lat, lon  = data.split(",")
            latitude_list.append(float(lat))
            longitude_list.append(float(lon))
            line_count += 1
    print('Processed {} lines.'.format(line_count))
with open('DRIVE_CYCLE_DATA_3.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    line_count = 0
    data = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            data = row["LAT_LON (S)"]
            lat, lon  = data.split(",")
            latitude_list.append(float(lat))
            longitude_list.append(float(lon))
            line_count += 1
    print('Processed {} lines.'.format(line_count))
print(latitude_list)
print(longitude_list)

#gmap4 = gmplot.GoogleMapPlotter.from_geocode("Delhi, India")
gmap4 = gmplot.GoogleMapPlotter(28.534014, 77.213432, 13 ) 
gmap4.scatter( latitude_list, longitude_list, '#FF0000', size = 10, marker = False )
gmap4.draw( "C:\\Users\\user\\Desktop\\map14.html" )
#top = Tkinter.Tk()
# Code to add widgets will go here...
#top.mainloop()
webbrowser.open("C:\\Users\\user\\Desktop\\map14.html")
