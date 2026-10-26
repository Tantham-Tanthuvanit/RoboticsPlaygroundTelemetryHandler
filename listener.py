import serial
import requests
import json

SERIAL_PORT = "/dev/ttyACM0"
BAUD_RATE = 115200

SERVER_URL = "http://127.0.0.1:5000/lidar-scan"

print(f"Listening for Lidar stream on {SERIAL_PORT}...")

try:
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)

    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8', errors='ignore').strip()
