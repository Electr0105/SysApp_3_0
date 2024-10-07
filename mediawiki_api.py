#!/usr/bin/python3

"""
    login.py

    MediaWiki API Demos
    Demo of `Login` module: Sending post request to login
    MIT license
"""

import requests

USERNAME = 'Jackson.Gleeson@Account.Bot'
PASSWORD = 'vheqr60rae6cgl6jdso1hpq8cnskvokc'
URL = "https://wiki.amtek.com.au/api.php"
WIKI_URL = "https://wiki.amtek.com.au"

S = requests.Session()


# Retrieve login token first
PARAMS_0 = {
    'action':"query",
    'meta':"tokens",
    'type':"login",
    'format':"json"
}

R = S.get(url=URL, params=PARAMS_0)
DATA = R.json()

LOGIN_TOKEN = DATA['query']['tokens']['logintoken']

# Send a post request to login. Using the main account for login is not
# supported. Obtain credentials via Special:BotPasswords
# (https://www.mediawiki.org/wiki/Special:BotPasswords) for lgname & lgpassword

# PARAMS_1 = {
#     'action': "login",
#     'lgname': USERNAME,
#     'lgpassword': PASSWORD,
#     'lgtoken': LOGIN_TOKEN,
#     'format': "json"
# }

# R = S.post(URL, data=PARAMS_1)
# DATA = R.json()

# print(DATA)
# assert DATA['login']['result'] == 'Success'

# PARAMS_0 = {
#     'action':"query",
#     'meta':"tokens",
#     'type':"createaccount",
#     'format':"json"
# }

# R = S.get(url=URL, params=PARAMS_0)
# DATA = R.json()

# TOKEN = DATA['query']['tokens']['createaccounttoken']

# # Second step
# # Send a post request with the fetched token and other data (user information,
# # return URL, etc.)  to the API to create an account

# PARAMS_1 = {
#     'action': "createaccount",
#     'createtoken': TOKEN,
#     'username': 'Test.Test',
#     'password': 'JackJack123!',
#     'retype': 'JackJack123!',
#     'createreturnurl': WIKI_URL,
#     'email': "john.doe@amtek.com.au",
#     'format': "json"
# }

# R = S.post(URL, data=PARAMS_1)
# DATA = R.json()

# print(DATA)
#!/usr/bin/python3

"""
    userrights.py

    MediaWiki API Demos
    Demo of `Userrights` module: Add and remove user rights by
    changing the user's group membership.
    MIT license
"""

import requests

S = requests.Session()


# Step 1: Retrieve a login token
PARAMS_1 = {
    "action": "query",
    "meta": "tokens",
    "type": "login",
    "format": "json"
}

R = S.get(url=URL, params=PARAMS_1)
DATA = R.json()

LOGIN_TOKEN = DATA["query"]["tokens"]["logintoken"]

# # Step 2: Send a post request to log in. See
# # https://www.mediawiki.org/wiki/Manual:Bot_passwords
# # for a special note on logging in using a simplified
# # interface when accessing wikis via an application,
# # rather than the GUI
# PARAMS_2 = {
#     "action": "login",
#     "lgname": USERNAME,
#     "lgpassword": PASSWORD,
#     "lgtoken": LOGIN_TOKEN,
#     "format": "json"
# }

# R = S.post(URL, data=PARAMS_2)
# print(R.json())
# # Step 3: Obtain a Userrights token
# PARAMS_3 = {
#     "action": "query",
#     "format": "json",
#     "meta": "tokens",
#     "type": "userrights"
# }

# R = S.get(url=URL, params=PARAMS_3)
# DATA = R.json()
# print(DATA["query"]["tokens"])
# USERRIGHTS_TOKEN = DATA["query"]["tokens"]["userrightstoken"]

# Step 4: Request to add or remove a user from a group
# PARAMS_4 = {
#     "action": "userrights",
#     "format": "json",
#     "add": "Home",
#     "expiry":"infinite",
#     "user": "Test.Test",
#     "remove": "CHD",
#     "token": USERRIGHTS_TOKEN
# }

# R = S.post(URL, data=PARAMS_4)
# DATA = R.json()

# -----------------------------------------------------------------
#!/usr/bin/python3

# PARAMS_1 = {
#     "action": "query",
#     "meta": "tokens",
#     "type": "login",
#     "format": "json"
# }

# R = S.get(url=URL, params=PARAMS_1)
# DATA = R.json()

# LOGIN_TOKEN = DATA["query"]["tokens"]["logintoken"]

# # Step 2: Send a post request to log in. See
# # https://www.mediawiki.org/wiki/Manual:Bot_passwords
# # for a special note on logging in using a simplified
# # interface when accessing wikis via an application,
# # rather than the GUI
# PARAMS_2 = {
#     "action": "login",
#     "lgname": USERNAME,
#     "lgpassword": PASSWORD,
#     "lgtoken": LOGIN_TOKEN,
#     "format": "json"
# }

# R = S.post(URL, data=PARAMS_2)
# PARAMS = {
#     "action": "query",
#     "format": "json",
#     "list": "users",
#     "ususers": "Test.Test",
#     "usprop": "blockinfo|groups"
# }

# R = S.get(url=URL, params=PARAMS)
# DATA = R.json()

# USERS = DATA["query"]["users"]

# print(USERS)
# -----------------------------------------------------------------

# PARAMS_1 = {
#     "action": "query",
#     "meta": "tokens",
#     "type": "login",
#     "format": "json"
# }

# R = S.get(url=URL, params=PARAMS_1)
# DATA = R.json()

# LOGIN_TOKEN = DATA["query"]["tokens"]["logintoken"]

# Step 2: Send a post request to log in. See
# https://www.mediawiki.org/wiki/Manual:Bot_passwords
# for a special note on logging in using a simplified
# interface when accessing wikis via an application,
# rather than the GUI
PARAMS_2 = {
    "action": "login",
    "lgname": USERNAME,
    "lgpassword": PASSWORD,
    "lgtoken": LOGIN_TOKEN,
    "format": "json"
}

R = S.post(URL, data=PARAMS_2)
print(R.json())
# Step 3: Obtain a Userrights token
PARAMS_3 = {
    "action": "resetpassword",
    "format": "json",
    "meta": "tokens",
    "type": "userrights"
}

R = S.get(url=URL, params=PARAMS_3)
DATA = R.json()
print(DATA["query"]["tokens"])
USERRIGHTS_TOKEN = DATA["query"]["tokens"]["userrightstoken"]