import json
from pprint import pprint

users = {}
sessions = {}
appconfig = {}

def checkToken(data):
    if "token" not in data: return False
    if data["token"] not in sessions: return False
    return True

def loadConfig(filename):
  global appconfig
  with open(filename) as json_file:
    appconfig.update(json.load(json_file))
      
def loadUsers(filename):
  global users
  with open(filename) as json_file:
    users.update(json.load(json_file))
