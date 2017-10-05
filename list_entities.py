#!/usr/bin/env python3
# List usual (not-system) users and groups

import os
import sys

if os.getuid() != 0:
    print('Run script as root')
    exit(1)

if len(sys.argv) != 2:
    print('Incorrect usage')
    print('Use:', sys.argv[0], 'users/groups')
    exit(1)

filename = ''

if sys.argv[1] == 'users':
    filename = '/etc/passwd'
elif sys.argv[1] == 'groups':
    filename = '/etc/group'
else:
    print('Invalid operation')
    exit(1)

with open(filename) as file:
    entities = file.read().splitlines();
    for entity in entities:
        entity_name = entity.split(':')[0]
        entity_id = int(entity.split(':')[2])

        if entity_id > 1000:
            print(entity_name)

