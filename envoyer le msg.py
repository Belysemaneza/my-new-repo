# Ecrit tonfrom microbit import *
import radio

radio.config(channel = 6)

rock = Image(
"09990:"
"99999:"
"99999:"
"99999:"
"09990")

paper = Image(
"99990:"
"90009:"
"90009:"
"90009:"
"99999")

scissors = Image(
"90009:"
"09090:"
"00900:"
"09090:"
"90009")

answers = [rock, paper, scissors]
while True:
    radio.send("HI")



