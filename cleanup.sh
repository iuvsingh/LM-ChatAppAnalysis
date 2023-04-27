#!/bin/bash
adb shell su -c "rm -rf /data/local/tmp/copydbF 2>/dev/null"
adb shell su -c "rm -rf /sdcard/dbs_attchmnt 2>/dev/null"

adb shell su -c "rm -rf /sdcard/copydbF 2>/dev/null"

# adb shell su -c "ls /sdcard/"
# adb shell su -c "ls /data/local/tmp/"

adb shell su -c "rm -rf /sdcard/exe_files 2>/dev/null"
adb shell su -c "killall -9 /data/local/tmp/./copydbF 2>/dev/null"

find . -mindepth 1 -type d ! -name old_version -exec rm -rf {} + -o -type f \( ! -name CMakeLists.txt ! -name DB2CSV.sh ! -name filewatchdog.py ! -name moving.c ! -name PrettyGUI.py ! -name README.md ! -name ScrollableNotebook.py ! -name test.py ! -name cleanup.sh ! -name .git \) -delete

rm -rf ~/Desktop/imports/* 2>/dev/null
rm -rf ~/Desktop/diff.txt 2>/dev/null

adb kill-server

#/sdcard/DCIM/kik/378386a4-417a-4f04-85ec-a9750a8eccc6.jpg
