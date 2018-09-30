#!/bin/bash
FILE="$1"
if [ -f "$1" ]
then
    echo "FILE: $1"
	fsize="$(du -b $1 | cut -f1)"
    bzip2 -k $1
    gzip -k $1
    zip -uq $1.zip $1
    bsize="$(du -b $1.bz2 | cut -f1)"
    gsize="$(du -b $1.gz | cut -f1)"
    zsize="$(du -b $1.bz2 | cut -f1)"
    echo "bzip2 \t ${bsize} \t ${fsize}"
    echo "gzip \t ${gsize} \t ${fsize}"
    echo "zip \t ${zsize} \t ${fsize}"
else
    echo "file not exists"
fi
