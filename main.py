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
TIMER = 0

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
    TIMER = time.time()

def stop():
    READ = False


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

def reset():
    TIMER = time.time()

LDR_MAX_VOLTAGE = 2.5 # Calibrated Max when really dark.
LDR_MIN_VOLTAGE = 0.5 # Calibrated Min when really lit. 
def ADCfromLDR(value):
    res = 1024
    max = 3.3
    voltage = max/(res - 1) * value # The voltage across the LDR
    return (LDR_MAX_VOLTAGE - voltage)/(LDR_MAX_VOLTAGE - LDR_MIN_VOLTAGE * 100)

def main():
    while (READ):
        READINGS.append(Reading(
            time.time(), MCP.read_adc(0), MCP.read_adc(1), MCP.read_adc(2)
            ))
        time.sleep(1/FREQ)