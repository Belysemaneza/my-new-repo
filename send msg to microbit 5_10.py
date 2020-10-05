from microbit import*

while True:
    msg = uart.read()
    if msg == b"heads":
        display.show (Image.TRIANGLE)
    elif msg == b"Tails":
        display.show (Image.HEART)it ton programme
