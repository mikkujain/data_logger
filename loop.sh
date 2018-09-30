#!/bin/bash
echo "The current time is:"
date

echo "\nThe current users are:"
w -h | cut -d' ' -f1 | sort | uniq
while true
do
    echo "1"
    sleep 3s
done
