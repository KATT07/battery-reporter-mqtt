import psutil
import paho.mqtt.client as mqtt

#Edit These to match your config
broker_address = "192.168.XXX.XXX"
# username = 'XXX'
# password = 'XXX'
client_name = "XXX"
port = 1883
topic = "XXX/XXX"


battery_status = psutil.sensors_battery()
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1,client_name)  # create new instance
# client.username_pw_set(username, password)
client.connect(broker_address)  # connect to broker

if battery_status is not None:
  print(battery_status)
  print(battery_status.percent)
  client.publish(topic, int(battery_status.percent))  # publish
else:
  print("No Battery Found!")
