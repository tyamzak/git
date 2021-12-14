#!/bin/bash

gst-launch-1.0.exe autovideosrc ! autovideosink

#STREAMER_PATH="/home/pi/mjpg-streamer/mjpg-streamer-experimental"
#sudo ${STREAMER_PATH}/mjpg_streamer -i "${STREAMER_PATH}/input_uvc.so -f 10 -r 320x240 -d /dev/video0 -y -n" -o "${STREAMER_PATH}/output_http.so -w ${STREAMER_PATH}/www -p 8080" -b