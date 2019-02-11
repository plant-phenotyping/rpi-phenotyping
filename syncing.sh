#!/bin/bash

rsync -av -e ssh ~/Desktop/camera1/ pi@142.244.190.228:/root/mnt/PIHDD/zone3/camera1/
rsync -av -e ssh ~/Desktop/camera2/ pi@142.244.190.228:/root/mnt/PIHDD/zone3/camera2/