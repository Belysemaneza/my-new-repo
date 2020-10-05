from microbit import*
from random import choice
while true:
    msg = uart.readif msg
    if msg:
        display scroll(msg)
