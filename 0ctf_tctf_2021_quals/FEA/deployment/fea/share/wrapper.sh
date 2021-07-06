#!/bin/sh

cd /home/pwn
TEMPDIR="/tmp/$(date "+%Y%m%d%H%M%S")_$(cat /dev/urandom | head -n 10 | md5sum | head -c 10)"
# mkdir $TEMPDIR
cp -r server $TEMPDIR
cd $TEMPDIR
# exec timeout 5m ./rrrrrusttttt
timeout 5m python server.py 2>err
cd /home/pwn
rm -rf $TEMPDIR
