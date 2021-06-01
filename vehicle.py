import sys
import urllib.request
from time import sleep
import random

myurl = "https://api.thingspeak.com/update?api_key=5NKLBPLHTEJC42RI"

while True:
    pressure = random.uniform(0 ,60)
    temperature = random.randrange(25, 90)
    smoke = random.uniform(100, 900)
    Oil = random.uniform(0, 50)
    poll = 0
    emergency = 0

    if smoke > 500:
        poll += 1
    if temperature > 82 and pressure > 20:
        emergency = 1
    urllib.request.urlopen(myurl + "&field1=" + str(pressure) + "&field2=" + str(temperature) + "&field3=" + str(smoke) + "&field4=" + str(Oil) + "&field5=" + str(poll) + "&field6=" + str(emergency))
    print("Uploaded")