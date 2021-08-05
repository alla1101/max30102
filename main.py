import paho.mqtt.client as mqtt
import json
from heartrate_monitor import HeartRateMonitor
import time

THINGSBOARD_HOST = '192.168.1.101'
ACCESS_TOKEN = 'RASPBERRY_PI_DO_TOKE'

sensor_data = {'valid_spo2': False, 'finger_on': False, "bpm":0,"spo2":0}


client = mqtt.Client()

client.username_pw_set(ACCESS_TOKEN)

client.connect(THINGSBOARD_HOST, 1883, 60)
hrm = HeartRateMonitor()
hrm.start_sensor()
next_reading = time.time() 
INTERVAL=0.25

try:
    while True:
        sensor_data=hrm.get_data()
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
