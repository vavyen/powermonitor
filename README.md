# Powermonitor 

  Python script to monitor electricity consumption or, as in my case, electricity generation by my AC coupled PV system, using a cheap DIN rail mount electric meter instead of a 10 times more expensive proprietary power monitoring gateway and cloud connected software blob. The consumed/generated power value is sent to an mqtt broker (then manipulated in NodeRed, visualized in Homeassistant, and stored in InfluxDB, see IOTstack). 

# Hardware:

- raspberry pi zero w, or any raspi laying around on your bench...

!!!WARNING!!! MAINS VOLTAGE IS DANGEROUS! DO YOUR OWN RESARCH BEFORE GOING FURTHER... HIRE A LICENSED ELECTRICIAN! 
insert here all the legal language, diclaimer, etc. I'm not liable for anything and everything YOU are doing!

- Din rail mount electric meter, e.g. DDS238-1, DDS6619, 02-553/DIG - Adeleq, 004670-Legrand, etc.. Links for examples (non affiliate):
   - https://www.banggood.com/DDS238-1-230V-Rail-Type-Electronic-Type-Mini-Electricity-Meter-LCD-Display-p-1050470.html
   - https://www.amazon.com/Yosoo-Health-Gear-Electric-Backlight/dp/B08FY5WLNM
   - https://www.amazon.com/DDS6619-526L-Digital-Wattmeter-Backlight-Function/dp/B081N1C1PM/
   - https://www.ebay.com/itm/Single-Phase-Energy-Meter-Digital-LCD-Single-phase-DIN-Rail-Electric-Meter/193704005846
   
  You'll need one rated to your local grid voltage and frequency, choose one with auxiliary circuit, with the lowest possible supply voltage range required (minimum 3V is perfect!), mine requires a supply voltage between 5V and 19V, so a voltage divider is needed to not kill the GPIO pins.
