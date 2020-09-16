#!/usr/bin/env python3

__author__ = 'Mike Walker'

import sys
from zwift import Client as ZwiftClient

# Parse user creds, player_id
username = sys.argv[1]
password = sys.argv[2]
player_id = sys.argv[3]

client = ZwiftClient(username, password)
profile = client.get_profile(player_id)

# print(profile.latest_activity)

data = {}

print(profile.profile)
print(profile.latest_activity)
