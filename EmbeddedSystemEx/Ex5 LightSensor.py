from gpiozero import LightSensor
from time import sleep

sensor=LightSensor(13)

while True:
    if(sensor.value>0.5):
        print("It is Light")
    else:
        print("It is dark")

    # print("Sensor Value is"+str(sensor.value))
    # print("Sensor threshold is"+str(sensor.threshold))
    sleep(1)

    
    
    