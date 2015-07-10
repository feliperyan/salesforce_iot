import serial
import json
import requests
import time


def main():
    ser = serial.Serial('/dev/tty.usbmodem1411', 9600)
    url = 'https://cryptic-tor-2725.herokuapp.com/api/v1.0/scans'
    headers = {'Content-Type': 'application/json'}


    print ('\nHit Control + C to quit\n')
    print ('Now waiting for a scan...\n')

    while True:
        a = ser.readline()
        print (a)
        r = requests.post(url, headers=headers, data=json.dumps({'rfid':a.strip()}))
        time.sleep(5)


if __name__ == "__main__":
    main()
