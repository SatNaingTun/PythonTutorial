from gpiozero import LED, Buzzer, Button,LightSensor,MotionSensor

from time import sleep



button =Button(2)
buzzer=Buzzer(26)
led1=LED(14)
led2=LED(4)
led3=LED(17)
led4=LED(27)

LDR=LightSensor(13)
pir=MotionSensor(19)

all_Leds=[led1,led2,led3,led4]

isSurveillance=False

def dark():
    led1.on()
    led2.on()
    led3.on()
    led4.on()
    

def ledOff():
    led1.off()
    led2.off()
    led3.off()
    led4.off()

def light():
    led1.on()
    led4.on()
    

def ready():
    if(LDR.value>0.5):
        print("It is Light")
        light()
    else:
        print("It is dark")
        dark()
    print("Press and hold button 2s to enter surveillance mode!")
    sleep(2)
    button.hold_time=2
        # button.held_time=2
    button.wait_for_press(2)
    if button.is_pressed:
        isSurveillance=True
        surveillance()
    
    

def scanning():
 for led in all_Leds:
    led.on()
    sleep(1)
    led.off()

def surveillance():
    print("Surveillance is active")
    ledOff()
    scanning()
    is_motion()

def alarm():
    
        print("LEDs are blinking")
        led1.blink(1,1)
        led2.blink(1,1)
        led3.blink(1,1)
        led4.blink(1,1)
        # led1.on()
        # led2.on()
        # led3.on()
        # led4.on()
        # sleep(.3)
        # ledOff()
        # sleep(.3)

def is_motion():
    while button.is_pressed==False:
        pir.wait_for_motion(2)
        print("PIR value"+str(pir.value))
        if(pir.value==1):
            print("Alarm run")
            alarm()
    # pir.when_motion=motionFun()
    # pir.when_no_motion=buzzer.off
    #pir.when_motion=motionFun()
    # pir_value=pir.value
    # if(pir_value==1):
    #     print("Motion Detected")

    # if button.is_pressed:
    #     buzzer.off()
    #     print("Motion stopped")
    
    # button.when_pressed=ready()
    
        if button.is_pressed:
            ready()
            isSurveillance=False
            break
        
    
        
    
    
    
def motionFun():
    print("Motion detected")
    buzzer.on()
    sleep(2)
    buzzer.off()
    # if button.is_pressed:
    #     print("Button is pressed")


# while True:

if __name__ == '__main__':
    
    while True:
        if isSurveillance==False:
            ready()
            ledOff()
    
           

            

    
    
    
        

# while True:
#     is_motion()
    

# all_Leds.off()
# sleep(1)

# ready()
