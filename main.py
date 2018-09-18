import RPi.GPIO as GPIO
import spidev

import time

# GPIO Switch Pins
RESET_SWITCH = 2
FREQ_SWITCH = 3
STOP_SWITCH = 4

# GPIO SPI Pins
SPICLK = 11
SPIMISO = 9
SPIMOSI = 10
SPICS = 8

# Global variables
FREQ = 0
TIMER

spi = spidev.SpiDev()
spi.open(0,0)

def setup():

    #Set the GPIO mode

    GPIO.setmode(GPIO.BCM)
    
    # Set up the switch pins

    GPIO.setup(RESET_SWITCH, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(FREQ_SWITCH, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(STOP_SWITCH, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(DISPLAY_SWITCH, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def switch_frequency():
    if FREQ == 0.5:
        FREQ = 1
    elif FREQ == 1:
        FREQ = 2
    else:
        FREQ = 0.5


def reset():
    // Reset Timer
    // Clean console


def stop():
    # Start monitoring
    # Stop monitoring


def display():
    # Display first five readings
    print("_____________________________")
    print("{0:8} {1:8} {2:4} {3:4} {4:5}".format("Time", "Timer", "Pot", "Temp", "Light"))
    print("_____________________________")
    for reading in READINGS:
        reading.printReading()
        print("_____________________________")


class Reading:

    def __init__(self, time, pot, temp, light):
        self.time = time
        self.pot = pot
        self.temp = temp
        self.light = light

    def printReading(self):
        print("{0:8} {1:8} {2:3}V {3:2}C {4:2}%"
              .format(self.time, self.timer, self.pot, self.light))

def ADCPOT(value):
    max = 3.3
    levels = 1024
    return max/(levels-1) *value

def ADCTEMP(value):
    levels = 1024
    max =3.3
    voltage = max/(levels-1)* value
    return temp