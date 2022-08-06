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


folls = []
# # print(no_follow_back)

# i: int = 0

# while i < len(followers["relationships_followers"]):
for item in followers["relationships_followers"]:
    folls.append(item["string_list_data"][0]["href"])

for each in following["relationships_following"]:
    if not each["string_list_data"][0]["href"] in folls:
        no_follow_back.append(each["string_list_data"][0]["href"])


print(no_follow_back)

#     i += 1
    
# print(no_follow_back)


# lar = [{"a": 123, "b": 15656, "c": 77777}]
# sba = [{"a": 123, "b": 15656, "c": 77777}]

# print(lar[0] in sba)

