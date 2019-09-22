##
# Main Module: display.py
##

import configparser
import tm1637
from time import sleep

config = configparser.ConfigParser()
config.read('config/appconfig.ini')

CLK = int(config['GPIO']['clk'])
DIO = int(config['GPIO']['dio'])

tm = tm1637.TM1637(clk=CLK, dio=DIO)

tm.brightness(7)

while True:
    tm.scroll('HELLO LISA')
    tm.numbers(69, 69)
    sleep(3)
