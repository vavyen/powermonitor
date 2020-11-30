#!/usr/bin/env python

# Import python libraries
import RPi.GPIO as GPIO
import time
import config
import paho.mqtt.publish as publish

#Function called when GPIO.RISING

def power_function():

  pulse_period  = time.time() - config.start_time
  power = int(round(config.pulse / pulse_period))
  load = str(power) + str(" watt") 
  print('\r' + load)
  publish.single(config.mqtt_topic, payload=power, hostname=config.mqtt_host)
  config.start_time = time.time()

# use BCM GPIO numbering
GPIO.setmode(GPIO.BCM)

# Define BCM-PIN number, change it to your setup
GPIO_PIN = 25

# Define pin as input, pulled down
GPIO.setup(GPIO_PIN, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

try:
  
  while True :

    # Wait for the trigger then call the function
    GPIO.wait_for_edge(GPIO_PIN, GPIO.RISING)
    power_function()
    # Delay so to not catch the edge return as signal, 
    # experiment with different delays in line with your own setup and power needs if the edge return is catched as signal.
    time.sleep(0.1)

except KeyboardInterrupt:
  # Reset the GPIO settings
  GPIO.cleanup()
