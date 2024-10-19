from gpiozero import LED, Buzzer, Button
from time import sleep

button =Button(2)
buzzer=Buzzer(26)
myLed=LED(3)


while True:
    if button.is_pressed:
        print("button pressed")
        buzzer.on()
        myLed.on()
        sleep(1)

    else:
        buzzer.off()
        myLed.off()
    