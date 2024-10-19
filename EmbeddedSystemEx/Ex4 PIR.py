from gpiozero import MotionSensor, LED

pir=MotionSensor(19)

while True:
    pir.wait_for_motion()
    print("Motion Detected")
   
    #if(pir.value>0.5):
        #print("Motion Detected")
        #print("Motion Detected "+str(pir.value))
    
    
   # pir.wait_for_no_motion()
    #print("No Motion Detected")
