import RPi.GPIO as GPIO
import time
i = 1
#these lines import the GPIO library and the time library, and declaring i so I can use a while loop to repeat this code
red = 12
green = 16
blue = 21
#these set the GPIO pin numbers equal to a color so I could better coordinate them

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
#the above lines setup the pins so they can be turned on and off
while i > 0:

	GPIO.output(green,GPIO.HIGH)
	time.sleep(5)
	GPIO.output(green,GPIO.LOW)
	#these lines turn on the pin for my green LED, pause for 5 seconds, then turn it off

	GPIO.output(green,GPIO.HIGH)
	GPIO.output(red,GPIO.HIGH)
	time.sleep(1)
	GPIO.output(red,GPIO.LOW)
	GPIO.output(green,GPIO.LOW)
	#these lines turn on the pins for red and green which mix to make a yellow light, pause for 1 second, then turn them back off

	GPIO.output(red,GPIO.HIGH)
	time.sleep(4)
	GPIO.output(red, GPIO.LOW)
	#these lines turn on the red LED, pause for 4 seconds then turn it back off
	#after this, my while loop checks that i is greater than 0 which it is, so it repeats infinitely since there is no counter :) 
