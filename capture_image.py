#!/usr/bin/env python3

import RPi.GPIO as gp
import os
import socket
import datetime as dt

gp.setwarnings(False)
gp.setmode(gp.BOARD)

gp.setup(7, gp.OUT)
gp.setup(11, gp.OUT)
gp.setup(12, gp.OUT)

gp.output(11, True)
gp.output(12, True)

def main():
    
    gp.output(7, False)
    gp.output(11, False)
    gp.output(12, True)
    capture(1)

    gp.output(7, False)
    gp.output(11, True)
    gp.output(12, False)
    capture(2)

def get_time_and_date(date_time):

    date = date_time.split(" ")[0]
    
    time = date_time.split(" ")[1].split(".")[0].split(":")
    new_time = time[0] + "-" + time[1] + "-" + time[2]

    return date, new_time

def capture(cam):

    date_time = str(dt.datetime.now())

    date, time = get_time_and_date(date_time)
    zone_number = str(socket.gethostname())[-1]

    cmd = "raspistill -o ~/Desktop/camera%d/z%sc%d--%s--%s.png" % (cam, zone_number, cam, date, time)
    os.system(cmd)
    
if __name__ == "__main__":
    
    main()
    
    gp.output(7, False)
    gp.output(11, False)
    gp.output(12, True)