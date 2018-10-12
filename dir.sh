#!/bin/bash

filename="teledir.txt"
name=$1
output="$(grep $1 $filename)"

if [ ! -z "$output" ] ; then
    grep "$1" "$filename"
else
    case $1 in
    ''|*[!0-9]*) echo "Name does not exist" ;;
    *) echo "Number does not exist" ;;
    esac
fi
