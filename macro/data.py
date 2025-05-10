import json
with open('../data/data.json', 'r') as f:
    data = json.load(f)

userdata = data['userdata']
gamedata = data['gamedata']




# discord
DISCORD_WEBHOOK_URL = userdata['config']['discord_webhook_url']
DISCORD_USERID = userdata['config']['discord_userid']
DISCORD_PING = f'<@{DISCORD_USERID}>'
DETAILED_REPORT = userdata['config']['detailed_report']

# roblox
from roblox_utils import generate_private_server_login_link
PRIVATE_SERVER_LINK = userdata['config']['private_server_link']
PRIVATE_SERVER_LOGIN_LINK = generate_private_server_login_link(PRIVATE_SERVER_LINK)
