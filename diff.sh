#!/bin/bash

if [ $# -ne 2 ]; then
  echo "Usage: $0 file1 file2"
  exit 1
fi

if [ ! -f $1 ]; then
  echo "Error: $1 is not a regular file"
  exit 1
fi

if [ ! -f $2 ]; then
  echo "Error: $2 is not a regular file"
  exit 1
fi

diff $1 $2
