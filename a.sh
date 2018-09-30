#!/bin/bash
FILE="$1"
file_size = $(stat -c%s "$1")
echo $file_size
if [ -f "$1" ]
then
    echo "FILE: $1"
    bzip2 $1
    du -sh $1.bz2
else
    echo "file not exists"
fi
