#!/usr/bin/env python3
# Get MD5 password hash

import crypt
import sys

if len(sys.argv) < 2:
    print('Usage:', sys.argv[0], 'password')
    exit(1)

text_to_crypt = ' '.join(sys.argv[1:])
print(crypt.crypt(text_to_crypt))
