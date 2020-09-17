#!/usr/bin/env python3

__author__ = 'Mike Walker'

import sys
import time
from zwift import Client as ZwiftClient

# Parse user creds, player_id
username = sys.argv[1]
password = sys.argv[2]
player_id = sys.argv[3]

client = ZwiftClient(username, password)
profile = client.get_profile(player_id)

# print(profile.latest_activity)

data = {}

if profile.latest_activity['profile']['riding']:
    # print('Riding')
    world = client.get_world(profile.latest_activity['profile']['worldId'])

    data.update({
        'timestamp': time.time(),
        'online': True,
        'heartrate': world.player_status(player_id).heartrate,
        'cadence': world.player_status(player_id).cadence,
        'power': world.player_status(player_id).power,
        'speed': world.player_status(player_id).speed,
        'altitude': world.player_status(player_id).altitude,
        'distance': world.player_status(player_id).distance,
        'heading': world.player_status(player_id).heading,
        'lean': world.player_status(player_id).lean,
        'f19': world.player_status(player_id).f19,
        'f20': world.player_status(player_id).f20,
        'x': world.player_status(player_id).x,
        'y': world.player_status(player_id).y,
        'justWatching': world.player_status(player_id).justWatching,
        'watchingRiderId': world.player_status(player_id).watchingRiderId,
        'roadTime': world.player_status(player_id).roadTime,
        'roadPosition': world.player_status(player_id).roadPosition,
        'course': world.player_status(player_id).course,
        'has_aero_boost': world.player_status(player_id).has_aero_boost,
        'has_draft_boost': world.player_status(player_id).has_draft_boost,
        'has_feather_boost': world.player_status(player_id).has_feather_boost,
        'is_forward': world.player_status(player_id).is_forward,
        'is_turning': world.player_status(player_id).is_turning,
        'power_up': world.player_status(player_id).power_up,
        'ride_ons': world.player_status(player_id).ride_ons,
        'road_direction': world.player_status(player_id).road_direction,
        'road_id': world.player_status(player_id).road_id,
        'turn_signal': world.player_status(player_id).turn_signal,
        'worldTime': world.player_status(player_id).worldTime
    })

    print(data)
