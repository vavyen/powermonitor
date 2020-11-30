#!/usr/bin/env python

import time

#initializing time in the past so the first pulse will be measured ~0
start_time = time.time() - 1500000000

#mqtt settings

mqtt_host = "YOURMQTTHOST"
mqtt_topic = "YOUR/TOPIC/TO/PUBLISH"

# value based on the energy meter's pulse#/KWh, comment/uncomment for your needs

# 1000 pulse/KWH
#pulse = 3600

# 2000 pulse/KWH
pulse = 1800
