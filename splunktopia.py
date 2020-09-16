#!/usr/bin/env python3

__author__ = 'Mike Walker'

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
profile = client.get_profile(player_id)

print(profile.latest_activity)

data = {}

if profile.latest_activity['profile']['riding']:
    print('Riding')
    world = client.get_world(profile.latest_activity['profile']['worldId'])

    data.update({
        'online': True,
        'heartrate': world.player_status(player_id).heartrate,
        'cadence': world.player_status(player_id).cadence,
        'power': world.player_status(player_id).power,
        'speed': world.player_status(player_id).speed,
        'altitude': world.player_status(player_id).altitude,
        'distance': world.player_status(player_id).distance
    })

    print(data)
