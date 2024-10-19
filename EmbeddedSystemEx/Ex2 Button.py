from gpiozero import LED,Button
from time import sleep


button=Button(2)
myLed=LED(3)
myLed.off()
while True:
    if button.is_pressed:
        myLed.on()
        print("LED is pressed")
        sleep(1)
    else:
        myLed.off()
        #print("LED is released")
        sleep(1)
    