from gpiozero import LED
from time import sleep

led_1 = LED(4)

i = 0

while i < 3:
    led_1.on()
    sleep(2)
    led_1.off()
    sleep(2)
    i = i+1