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
activity = client.get_activity(player_id)

if len(sys.argv) == 5:
    try:
        if int(sys.argv[4]) <= 50:
            activity_list = activity.list(limit=sys.argv[4])
            for i in activity_list:
                print(i)
        else:
            print(activity.list())
    except:
        print("Got invalid arg. Exiting")
        pass
elif len(sys.argv) == 6:
    activity_list = activity.list(start=sys.argv[4], limit=sys.argv[5])
    for i in activity_list:
        print(i)
else:
    print(profile.latest_activity)
