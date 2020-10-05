from microbit import*
import radio
radio.on()
radio.config(channel=3)

while True:
    radio.send("Cool")
    sleep(1000)
