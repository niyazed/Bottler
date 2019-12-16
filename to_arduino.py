import paho.mqtt.client as mqtt
import time
import json
from time import sleep
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)


def on_message(client,userdata,msg):
    bytes_value = msg.payload
    # print(bytes_value)
    my_json = bytes_value.decode('utf8').replace("'", '"')
    data = json.loads(my_json)
    #ser.write(str(data).encode())
    if data==1:
        GPIO.output(2,GPIO.LOW)
    elif data==0:
        GPIO.output(2,GPIO.HIGH)
        
    print(data)



client = mqtt.Client()
client.connect("localhost")
topic_response = "test"
client.subscribe(topic_response) 
client.on_message = on_message
client.loop_forever()
