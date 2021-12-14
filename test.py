import subprocess
cmd = 'gst-launch-1.0.exe autovideosrc ! videoconvert ! clockoverlay ! x264enc tune=zerolatency ! mpegtsmux ! hlssink playlist-root=http://192.168.0.11:8080 location=/home/gstreamer/hlstest/segment_%05d.ts target-duration=5 max-files=5'
subprocess.call(cmd)


