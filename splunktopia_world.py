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
        "timestamp": time.time(),
        "altitude": world.player_status(player_id).altitude,
        "cadence": world.player_status(player_id).cadence,
        "course": world.player_status(player_id).course,
        "distance": world.player_status(player_id).distance,
        "f19": world.player_status(player_id).f19,
        "f20": world.player_status(player_id).f20,
        "has_aero_boost": world.player_status(player_id).has_aero_boost,
        "has_draft_boost": world.player_status(player_id).has_draft_boost,
        "has_feather_boost": world.player_status(player_id).has_feather_boost,
        "heading": world.player_status(player_id).heading,
        "heartrate": world.player_status(player_id).heartrate,
        "is_forward": world.player_status(player_id).is_forward,
        "is_turning": world.player_status(player_id).is_turning,
        "justWatching": world.player_status(player_id).justWatching,
        "lean": world.player_status(player_id).lean,
        "online": True,
        "power": world.player_status(player_id).power,
        "power_up": world.player_status(player_id).power_up,
        "ride_ons": world.player_status(player_id).ride_ons,
        "roadPosition": world.player_status(player_id).roadPosition,
        "roadTime": world.player_status(player_id).roadTime,
        "road_direction": world.player_status(player_id).road_direction,
        "road_id": world.player_status(player_id).road_id,
        "speed": world.player_status(player_id).speed,
        "turn_signal": world.player_status(player_id).turn_signal,
        "watchingRiderId": world.player_status(player_id).watchingRiderId,
        "worldTime": world.player_status(player_id).worldTime,
        "x": world.player_status(player_id).x,
        "y": world.player_status(player_id).y
    })

    print(data)
