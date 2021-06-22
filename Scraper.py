from nba_api.stats import endpoints
from nba_api.stats.endpoints import commonplayerinfo
from nba_api.stats.static import players
import json

# Get all players.
player_dict = players.get_players()

# Get a specific player's info
for p in player_dict:
     print(p["id"], p["full_name"], p["is_active"])

for p in player_dict:
      player_info = commonplayerinfo.CommonPlayerInfo(player_id=p['id'])
      player_dict2 = player_info.common_player_info.get_dict()
      for p1 in player_dict2['data']:
          print('First Name:' + p1[1])

#gets json of players info
player_json = player_info.common_player_info.get_json()
# #gets dictionary of players info
player_dict = player_info.common_player_info.get_dict()
# #getting data from the dictionary
for p in player_dict['data']:
    print('First name:' + p[1]) #prints first name
    print('Last name:' + p[2])

# #writes to json file(not sure if necessary here)  
if len(player_json) >= 0: #overwrites eachtime for some reason?
        with open('Player.json', 'w') as outfile:
            json.dump(player_json, outfile, indent=4)
            outfile.write('\n')

 


# #need to find a way to only get first/last name, position, and calculate age
# #idk if this part is still needed, maybe when we export the data itll have to be in javascript/we can talk bout it
# #with open('Player.json') as json_file:
#     #data = json.load(json_file)
#     #for p in data: 
#         #print(p[0])




# # this shit might be useless
# # data = endpoints.__init__()

# # data = endpoints.CommonAllPlayers.get_data_frames(player_id=78630)
# # print(data)