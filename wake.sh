#!/bin/bash
echo "Sending magic packet to $1"
etherwake $1 -i eth0
echo wake.sh returned $?
