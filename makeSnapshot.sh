#!/usr/bin/bash

adb shell screencap -p /sdcard/capture.png
adb pull /sdcard/capture.png .
gimp capture.png
