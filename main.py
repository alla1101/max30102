from heartrate_monitor import HeartRateMonitor
import time
import argparse

parser = argparse.ArgumentParser(description="Read and print data from MAX30102")
parser.add_argument("-r", "--raw", action="store_true",
                    help="print raw data instead of calculation result")
parser.add_argument("-t", "--time", type=int, default=30,
                    help="duration in seconds to read from sensor, default 30")
args = parser.parse_args()

print('sensor starting...')
#hrm = HeartRateMonitor(print_raw=args.raw, print_result=(not args.raw))
hrm = HeartRateMonitor()
hrm.start_sensor()
count=1000
i=0
try:
    while True:
        i=i+1
        time.sleep(0.25)
        ss=hrm.get_data()
        print(ss)
        if i == count:
            break
except KeyboardInterrupt:
    hrm.stop_sensor()

hrm.stop_sensor()