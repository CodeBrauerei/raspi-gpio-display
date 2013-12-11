#!/usr/bin/python

# bad words counter. 
# someone said a bad word? press "+"
# you pressed one to much or it wasn't a bad word? press "-"

import time
import RPi.GPIO as GPIO

# GPIO Pins
ACTION_LED = 2
DISPLAY_RS = 7
DISPLAY_E  = 8
DISPLAY_DATA4 = 25 
DISPLAY_DATA5 = 24
DISPLAY_DATA6 = 23
DISPLAY_DATA7 = 18

DISPLAY_WIDTH = 16
DISPLAY_LINE_1 = 0x80
DISPLAY_LINE_2 = 0xC0
DISPLAY_CHR = True
DISPLAY_CMD = False
E_PULSE = 0.00005
E_DELAY = 0.00005

def main():
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(DISPLAY_E, GPIO.OUT)
        GPIO.setup(DISPLAY_RS, GPIO.OUT)
        GPIO.setup(DISPLAY_DATA4, GPIO.OUT)
        GPIO.setup(DISPLAY_DATA5, GPIO.OUT)
        GPIO.setup(DISPLAY_DATA6, GPIO.OUT)
        GPIO.setup(DISPLAY_DATA7, GPIO.OUT)
        GPIO.setup(ACTION_LED, GPIO.OUT)

        display_init()
        zahl = 0
        
        while True:
                var = raw_input("bad word said? (+/-): ")
                if var == "+":
                        zahl += 1
                        GPIO.output(ACTION_LED, True)
                        time.sleep(0.05)
                        GPIO.output(ACTION_LED, False)
                        print("one more bad word said...")
                elif var == "-":
                        zahl -= 1
                        print("counter was decremented.")
                lcd_byte(DISPLAY_LINE_1, DISPLAY_CMD)
                lcd_string("BAD WORDS TODAY:")
                lcd_byte(DISPLAY_LINE_2, DISPLAY_CMD)
                lcd_string(str(zahl))

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