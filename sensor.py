import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)

def distance():
    try:
        GPIO.setmode (GPIO.BOARD)
        GPIO_TRIGGER = 18
        GPIO_ECHO = 16

        print "Ultrasonic Measurement"

        GPIO.setup(GPIO_TRIGGER, GPIO.OUT) 	# TRIGGER
        GPIO.setup(GPIO_ECHO, GPIO.IN) 		# ECHO

        GPIO.output(GPIO_TRIGGER, False)
        time.sleep(0.5)

        GPIO.output(GPIO_TRIGGER, True)
        time.sleep(0.00001)
        GPIO.output(GPIO_TRIGGER, False)
        start = time.time()
        while GPIO.input(GPIO_ECHO) == 0:
            start = time.time()

        while GPIO.input(GPIO_ECHO) == 1:
	        stop = time.time()
	
        elapsed = stop - start

        # DISTANCE MEASUREMENT
        distance = elapsed * 34000

        distance = distance / 2

        distance_ft = distance * 0.39
    
        GPIO.cleanup()
        return distance_ft
    
    except:
        distance_ft = 100
        GPIO.cleanup()
        return distance_ft

#print distance()

