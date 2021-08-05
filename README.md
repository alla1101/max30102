# max30102
MAX30102 Pulse Oximetry Sensor code for Raspberry Pi

## Info
The code originally comes from: https://github.com/vrano714/max30102-tutorial-raspberrypi
but with some modifications so that it doesn't require the interrupt pin and
instead polls by checking the read and write FIFO pointers. I've also added a
top level of code that encapsulates everything into a thread.

The original code is a Python port based on Maxim's reference design written to
run on an Arduino UNO: https://github.com/MaximIntegratedRefDesTeam/RD117_ARDUINO/

## Setup
A couple non-standard Python libraries are required: `smbus` and `numpy`. I recommend
installing the `numpy` library with apt as opposed to pip since pip takes a really
long time.
`sudo apt install python-numpy`

## Use as a script

Run `python main.py`, data will be sent with MQTT client. 


