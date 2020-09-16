#!/usr/bin/env python3

__author__ = 'Mike Walker'

# TODO: Handle creds/auth
# TODO: Iterate through profile
# TODO: Iterate through activity metrics
# TODO: Activity metrics into JSON

import sys
from zwift import Client as ZwiftClient

# Parse user creds, player_id
username = sys.argv[1]
password = sys.argv[2]
player_id = sys.argv[3]

print('username is ', username)
print('password is ', password)
print('player_id is ', player_id)

client = ZwiftClient(username, password)
# profile = client.get_profile()
profile = client.get_profile(player_id)

print(profile.latest_activity)

if profile.latest_activity['profile']['riding']:
    print('Riding')
    world = client.get_world(profile.latest_activity['worldId'])
    print(world.players)
