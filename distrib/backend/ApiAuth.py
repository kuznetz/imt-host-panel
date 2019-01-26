import cherrypy
import cherrypy_cors
import random
import json
import hashlib
import string 
#from pprint import pprint

from common import *

class ApiAuth(object):
    @cherrypy.expose
    @cherrypy_cors.tools.expose()
    @cherrypy.tools.allow(methods=["POST","OPTIONS"])    
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def login(self):
        if cherrypy.request.method == "OPTIONS":
            cherrypy_cors.preflight(allowed_methods=["POST"])
            return None
        #Проверим пользователя
        data = cherrypy.request.json
        if ("username" not in data) or ("password" not in data):
            return {"error":"Invalid request"}
        if data["username"] not in users:
            return {"error":"Invalid username or password"}
        if users[data["username"]]["password"] != data["password"]:
            return {"error":"Invalid username or password"}
        #Сделаем сессию
        newToken = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(16))
        sessions[newToken] = {
          "username" : data["username"]
        }       
        return {"token":newToken}
        
    @cherrypy.expose
    @cherrypy_cors.tools.expose()
    @cherrypy.tools.allow(methods=["POST","OPTIONS"])    
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def logout(self):
        if cherrypy.request.method == "OPTIONS":
            cherrypy_cors.preflight(allowed_methods=["POST"])
            return None
        data = cherrypy.request.json
        if "token" not in data:
            return {"error":"Invalid request"}
        sessions.pop(data["token"], None)
        return json.dumps({"result":"OK"})