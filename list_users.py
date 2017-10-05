#!/usr/bin/env python3
# List usual (not-system) users

import os

if os.getuid() != 0:
    print('Run script as root')
    exit(1)

with open('/etc/passwd') as file:
    users = file.read().splitlines();
    for user in users:
        username = user.split(':')[0]
        user_id = int(user.split(':')[2])

        if user_id > 1000:
            print(username)

