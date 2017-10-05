#!/usr/bin/env bash
# List usual (not-system) users

if [ $EUID != 0 ]
then
	echo "Run as root"
	exit 1
fi

cat /etc/passwd | \
while read line; do
	username=`echo $line | cut -d: -f1`
	userid=`echo $line | cut -d: -f3`
	
	if [ $userid -ge 1000 ]
	then
		echo $username
	fi
done
