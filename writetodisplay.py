#!/usr/bin/python
import time
import RPi.GPIO as GPIO
import sys

# Zuordnung der GPIO Pins (ggf. anpassen)
DISPLAY_RS    = 7
DISPLAY_E     = 8
DISPLAY_DATA4 = 25 
DISPLAY_DATA5 = 24
DISPLAY_DATA6 = 23
DISPLAY_DATA7 = 18

DISPLAY_WIDTH  = 16 	# Zeichen je Zeile
DISPLAY_LINE_1 = 0x80 	# Adresse der ersten Display Zeile
DISPLAY_LINE_2 = 0xC0 	# Adresse der zweiten Display Zeile
DISPLAY_CHR    = True
DISPLAY_CMD    = False
E_PULSE        = 0.00005
E_DELAY        = 0.00005

# Arguments
ARG_TEXT_1 = sys.argv[1]
ARG_TEXT_2 = sys.argv[2]

def main():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(DISPLAY_E, GPIO.OUT)
	GPIO.setup(DISPLAY_RS, GPIO.OUT)
	GPIO.setup(DISPLAY_DATA4, GPIO.OUT)
	GPIO.setup(DISPLAY_DATA5, GPIO.OUT)
	GPIO.setup(DISPLAY_DATA6, GPIO.OUT)
	GPIO.setup(DISPLAY_DATA7, GPIO.OUT)

	display_init()

	if len(ARG_TEXT_1) <= 16 and len(ARG_TEXT_2) <= 16:
		lcd_byte(DISPLAY_LINE_1, DISPLAY_CMD)
		lcd_string(ARG_TEXT_1)
		lcd_byte(DISPLAY_LINE_2, DISPLAY_CMD)
		lcd_string(ARG_TEXT_2)
	else:
		print "Too much chars. (max 16 chars a line)"


# display functions by www.schnatterente.net

def display_init():
	lcd_byte(0x33,DISPLAY_CMD)
	lcd_byte(0x32,DISPLAY_CMD)
	lcd_byte(0x28,DISPLAY_CMD)
	lcd_byte(0x0C,DISPLAY_CMD)  
	lcd_byte(0x06,DISPLAY_CMD)
	lcd_byte(0x01,DISPLAY_CMD)  

def lcd_string(message):
	message = message.ljust(DISPLAY_WIDTH," ")  
	for i in range(DISPLAY_WIDTH):
	  lcd_byte(ord(message[i]),DISPLAY_CHR)

def lcd_byte(bits, mode):
	GPIO.output(DISPLAY_RS, mode)
	GPIO.output(DISPLAY_DATA4, False)
	GPIO.output(DISPLAY_DATA5, False)
	GPIO.output(DISPLAY_DATA6, False)
	GPIO.output(DISPLAY_DATA7, False)
	if bits&0x10==0x10:
	  GPIO.output(DISPLAY_DATA4, True)
	if bits&0x20==0x20:
	  GPIO.output(DISPLAY_DATA5, True)
	if bits&0x40==0x40:
	  GPIO.output(DISPLAY_DATA6, True)
	if bits&0x80==0x80:
	  GPIO.output(DISPLAY_DATA7, True)
	time.sleep(E_DELAY)    
	GPIO.output(DISPLAY_E, True)  
	time.sleep(E_PULSE)
	GPIO.output(DISPLAY_E, False)  
	time.sleep(E_DELAY)      
	GPIO.output(DISPLAY_DATA4, False)
	GPIO.output(DISPLAY_DATA5, False)
	GPIO.output(DISPLAY_DATA6, False)
	GPIO.output(DISPLAY_DATA7, False)
	if bits&0x01==0x01:
	  GPIO.output(DISPLAY_DATA4, True)
	if bits&0x02==0x02:
	  GPIO.output(DISPLAY_DATA5, True)
	if bits&0x04==0x04:
	  GPIO.output(DISPLAY_DATA6, True)
	if bits&0x08==0x08:
	  GPIO.output(DISPLAY_DATA7, True)
	time.sleep(E_DELAY)    
	GPIO.output(DISPLAY_E, True)  
	time.sleep(E_PULSE)
	GPIO.output(DISPLAY_E, False)  
	time.sleep(E_DELAY)   

if __name__ == '__main__':
	main()
