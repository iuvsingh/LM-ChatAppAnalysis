#!/bin/bash

#this script is cleaning up the sdcard on the device

#the following 3 commands are recursively deleting the copydbF, dbs_attchmnt, copydbF directories in the sdcard
#accesses the device using adb shell and gaining elevated priveleges with "su"
adb shell su -c "rm -rf /data/local/tmp/copydbF 2>/dev/null"
adb shell su -c "rm -rf /sdcard/dbs_attchmnt 2>/dev/null"
adb shell su -c "rm -rf /sdcard/copydbF 2>/dev/null"
#it is outputting any error messages from the rm command into /dev/null, which discards it

#the same command is being executed on the exe_files directory
adb shell su -c "rm -rf /sdcard/exe_files 2>/dev/null"

# killall -9 is sending a message to a process to terminate it immediately
#sends an error ouput messages into /dev/null, which discards it
adb shell su -c "killall -9 /data/local/tmp/./copydbF 2>/dev/null"

#this command is finding and deleting all files and directories within the current directory
#all of the hardcoded file names in this command are excluded from the deletion
find . -mindepth 1 -type d ! -name old_version -exec rm -rf {} + -o -type f \( ! -name CMakeLists.txt ! -name DB2CSV.sh ! -name filewatchdog.py ! -name moving.c ! -name PrettyGUI.py ! -name README.md ! -name ScrollableNotebook.py ! -name test.py ! -name cleanup.sh ! -name .git \) -delete

#removes any directories/files within the imports folder on the local machine"
#sends all error messages to the /dev/null, discarding them
#the imports folder is where all of the chat application directories will reside once pulled from the device
rm -rf ~/Desktop/imports/* 2>/dev/null

#removes the diff.txt file on the local machine"
#sends all error messages to the /dev/null, discarding them
rm -rf ~/Desktop/diff.txt 2>/dev/null

#command to end the adb server
adb kill-server

