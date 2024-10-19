from gpiozero import MCP3202
from time import sleep

pot = MCP3202(channel=0)
# pot2 = MCP3202(channel=1)
while True:
    #value = pot.value
    print(pot.value)
    #print(f"Potentiometer value: {value:.2f}")
    sleep(0.7)