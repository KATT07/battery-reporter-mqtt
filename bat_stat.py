import psutil
import paho.mqtt.client as mqtt

broker_address="192.168.1.61"
username = 'admin'
password = 'adminpassword'
client_name="Homelab"
port = 1883
topic = "homelab/bat"

battery_status = psutil.sensors_battery()
client = mqtt.Client(client_name) #create new instance
client.username_pw_set(username, password)
client.connect(broker_address) #connect to broker

print(battery_status)
print(battery_status.percent)
client.publish(topic,int(battery_status.percent)) #publish