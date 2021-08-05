import paho.mqtt.client as mqtt
import json
from heartrate_monitor import HeartRateMonitor
import time

THINGSBOARD_HOST = '192.168.1.101'
ACCESS_TOKEN = 'T2_TEST_TOKEN'

sensor_data = {'valid_spo2': False, 'finger_on': False, "bpm":0,"spo2":0}


client = mqtt.Client()

client.username_pw_set(ACCESS_TOKEN)

client.connect(THINGSBOARD_HOST, 1883, 60)
hrm = HeartRateMonitor()
hrm.start_sensor()
next_reading = time.time() 
INTERVAL=0.25
client.loop_start()
try:
    while True:
        sensor_data_1=hrm.get_data()
        print(sensor_data_1)
        sensor_data["valid_spo2"]=sensor_data_1["valid_spo2"]
        sensor_data["finger_on"]=sensor_data_1["finger_on"]
        sensor_data["bpm"]=round(sensor_data_1["bpm"],2)
        sensor_data["spo2"]=round(sensor_data_1["spo2"],2)
        client.publish('v1/devices/me/telemetry', json.dumps(sensor_data), 1)

        next_reading += INTERVAL
        sleep_time = next_reading-time.time()
        if sleep_time > 0:
            time.sleep(sleep_time)

except KeyboardInterrupt:
    pass

client.loop_stop()
client.disconnect()
hrm.stop_sensor()
