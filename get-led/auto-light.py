import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
led = 26
GPIO.setup(led, GPIO.OUT)
photo = 6
GPIO.setup(photo, GPIO.IN)
while True:
    photo_state = GPIO.input(photo)
    GPIO.output(led, not photo_state)
    time.sleep(0.01)