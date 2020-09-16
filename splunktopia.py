#!/usr/bin/env python3

__author__ = 'Mike Walker'

# TODO: Handle creds/auth
# TODO: Iterate through profile
# TODO: Iterate through activity metrics
# TODO: Activity metrics into JSON

import sys
import zwift

username = sys.argv[1]
password = sys.argv[2]
player_id = sys.argv[3]

print('username is ', username)
print('password is ', password)
print('player_id is ', player_id)
