#!/usr/bin/env bash
# List usual (not-system) users and groups

if [ $EUID != 0 ]
then
	echo "Run as root"
	exit 1
fi

filename=''

if [ "$1" = "groups" ]; then
	filename='/etc/group'
elif [ "$1" = "users" ]; then
	filename='/etc/passwd'
else
	echo 'Incorrect usage'
	echo "Use: $0 users/groups"
	exit 1
fi

counter=0

while read line; do
	entity_name=`echo $line | cut -d: -f1`
	entity_id=`echo $line | cut -d: -f3`
	
	if [ $entity_id -ge 1000 ]; then
		echo $entity_name
		counter=$(($counter + 1))
	fi
done < $filename

echo "Total $1 $counter"
