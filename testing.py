#!/usr/bin/env python3

import RPi.GPIO as gp
import os
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

    date = date_time.split(" ")[0].split("-")
    new_date = date[1] + date[2] + date[0]
    
    # print(date)
    # print(new_date)
    
    time = date_time.split(" ")[1].split(".")
    new_time = time[0]
    
    # print(time)
    # print(new_time)

    return new_date, new_time

def capture(cam):

    date_time = str(dt.datetime.now())

    date, time = get_time_and_date(date_time)

    cmd = "raspistill -o ~/Desktop/camera%d/z3c%d_%s_%s.png" % (cam, cam, date, time)
    os.system(cmd)
    
if __name__ == "__main__":
    
    main()
    
    gp.output(7, False)
    gp.output(11, False)
    gp.output(12, True)