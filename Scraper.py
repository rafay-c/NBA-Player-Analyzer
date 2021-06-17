from nba_api.stats import endpoints
from nba_api.stats.endpoints import commonplayerinfo
from nba_api.stats.static import players
import json

# Get all players.
player_dict = players.get_players()

player_info = commonplayerinfo.CommonPlayerInfo(player_id=2544)

player = player_info.common_player_info.get_json()

if len(player) >= 0:
        with open('Player.json', 'w') as outfile:
            json.dump(player, outfile, indent=4)
			

print(player)

# tryna get 
# data = endpoints.__init__()

# data = endpoints.CommonAllPlayers.get_data_frames(player_id=78630)

#print(data)

