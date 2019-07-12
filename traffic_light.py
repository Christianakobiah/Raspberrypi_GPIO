#from gpiozero import LED
#
#green = LED(2)
#green.blink()

#from gpiozero import LED
#from time import sleep
#
#green = LED(2)
#
#while True:
# green.on()
# sleep(1)
# green.off()
# sleep(1)

from gpiozero import LED
from time import sleep

green = LED(2)

for i in range (0, 10):
     green.on()
     sleep(1)
     green.off()
     sleep(1)
     print ("%d blink" % (i))