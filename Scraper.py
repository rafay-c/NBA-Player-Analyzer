from nba_api.stats.static import players

# Get all players.


players.find_players_by_full_name('james')

# Find players by first name.
players.find_players_by_first_name('lebron')

# Find players by last name.
players.find_players_by_last_name('^(james|love)$')
print(players.find_players_by_last_name('^(james|love)$'))

# # Basic Request
# player_info = commonplayerinfo.CommonPlayerInfo(player_id=2544)


# custom_headers = {
#     'Host': 'stats.nba.com',
#     'Connection': 'keep-alive',
#     'Cache-Control': 'max-age=0',
#     'Upgrade-Insecure-Requests': '1',
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
#     'Accept-Encoding': 'gzip, deflate, br',
#     'Accept-Language': 'en-US,en;q=0.9',
# }

# # Only available after v1.1.0
# # Proxy Support, Custom Headers Support, Timeout Support (in seconds)
# player_info = commonplayerinfo.CommonPlayerInfo(player_id=2544, proxy='127.0.0.1:80', headers=custom_headers, timeout=100)


# # Returns data in a JSON string.
# player_info.available_seasons.get_json()

# # Returns data in a dictionary.
# player_info.available_seasons.get_dict()

# # Returns the data set in a pandas DataFrame.
# player_info.available_seasons.get_data_frame()


