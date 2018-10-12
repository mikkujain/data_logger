#!/bin/bash
echo "The current time is:"
date

echo "\nThe current users are:"
w -h | cut -d' ' -f1 | sort | uniq
echo ''
while true
do   
    output="$(last -s -3s | grep -v "wtmp")"
    if [ -z "$output" ]
    then
        echo "No user has logged in/out in the last 3 seconds."
    else
        last -s -3d | grep pts/ | awk '{ if (users[$8] == "still") { print "User "$1 " has logged in."} else { print "User "$1 " has logged out."}}' | uniq
    fi
    sleep 3s
done
