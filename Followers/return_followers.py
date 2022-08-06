"""Use to return the name of each of your Instagram followers"""

import json

followers_path = "/Users/cjsigmon/Python_projects/Followers/followers.json"
following_path = "/Users/cjsigmon/Python_projects/Followers/following.json"

# make a dict of all followers
with open(followers_path, 'r') as j:
     followers = json.loads(j.read())

# make a dict of all accounts user is following
with open(following_path, 'r') as j:
     following = json.loads(j.read())

# create an empty list to hold all accounts user is following that do not follow back
no_follow_back = []

# print(no_follow_back)


for list_item in following["relationships_following"]:
    print(list_item['string_list_data'][0])