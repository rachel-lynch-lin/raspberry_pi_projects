# Can only run this file on the Raspbian OS
# import RPi.GPIO as GPIO
# import time

# GPIO.setmode(GPIO.BCM)
# GPIO.setup(18, GPIO.OUT)

# while (True):
#     GPIO.output(18, True)
#     time.sleep(0.5)
#     GPIO.output(18, False)
#     time.sleep(0.5)

# Version 2 for GPIO Pins in a Safe State to reduce possibility of damage to Raspberry Pi

# import RPi.GPIO as GPIO
# import time

# GPIO.setmode(GPIO.BCM)
# GPIO.setup(18, GPIO.OUT)

# try:
#     while (True):
#         GPIO.output(18, True)
#         time.sleep(0.5)
#         GPIO.output(18, False)
#         time.sleep(0.5)
# finally:
#     print("Cleaning Up!")
#     GPIO.cleanup()

# When you use Ctrl-C to exit the program GPIO.cleanup will be called before the program completely stops

# This prevents shorts if you begin wiring a new project before rebooting your Raspberry Pi
# A better way to prevent shorts is to always power down your Pi before connecting hardware to it