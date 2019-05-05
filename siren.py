#!/usr/bin/env python
from gpiozero import Button, LED
from time import sleep
from subprocess import check_call, Popen

right = LED(21)
left = LED(19)
button = Button(6)
off = Button(26)
shutdown = Button(22)

def main():
    right.on() # For some reason the on and off are backwards
    left.on() # For some reason the on and off are backwards
    while True:
        if button.is_pressed:
            start_light()
        elif off.is_pressed:
            exit()
        elif shutdown.is_pressed:
            check_call(['sudo','poweroff'])

def start_light():
    Popen(['mpg321','/home/thomas/fire_truck_siren.mp3'])
    right.off()
    left.on()
    i = 0
    while i < 10:
        right.toggle()
        left.toggle()
        sleep(.5)
        i += 1
    right.on() # On is off
    left.on() # On is off
    
if __name__ == '__main__':
    main()
