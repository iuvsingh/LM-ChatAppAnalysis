#!/bin/bash

keep_files=("CMakeLists.txt" "DB2CSV.sh" "filewatchdog.py" "moving.c" "PrettyGUI.py" "README.md" "ScrollableNotebook.py" "test.py")
keep_dir="old_version"

# Remove everything except the specified files and directory
shopt -s extglob
rm -rf !( "${keep_files[@]}" | "$keep_dir" )

# Disable extglob
shopt -u extglob