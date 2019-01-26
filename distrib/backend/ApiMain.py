import cherrypy
import cherrypy_cors
import os
import json
from pprint import pprint

from common import *

class ApiMain(object):
    @cherrypy.expose
    @cherrypy_cors.tools.expose()
    @cherrypy.tools.allow(methods=["POST","OPTIONS"])    
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def sites(self):
        if cherrypy.request.method == "OPTIONS":
            cherrypy_cors.preflight(allowed_methods=["POST"])
            return None
        data = cherrypy.request.json
        if not checkToken(data): return {"error":"Invalid token"}

        sites = os.listdir(appconfig["paths"]["sites"])
        result = []
        for site in sites:
          path = appconfig["paths"]["sites"]+"/"+site
          full_site = None
          with open(path) as json_file:  
            full_site = json.load(json_file)
          full_site["name"] = site
          result.append(full_site)
        return result
        
    @cherrypy.expose
    @cherrypy_cors.tools.expose()
    @cherrypy.tools.allow(methods=["POST","OPTIONS"])    
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def create(self):
        if cherrypy.request.method == "OPTIONS":
            cherrypy_cors.preflight(allowed_methods=["POST"])
            return None
        data = cherrypy.request.json
        if not checkToken(data): return {"error":"Invalid token"}
        if ("siteName" not in data): return {"error":"Invalid request"}
        
        path = appconfig["paths"]["sites"] + "/" + data["siteName"]
        if os.path.isfile(path) : return {"error":"Site exist"}
        with open(path, "w") as new_file:
          print("{}", file=new_file)
        return json.dumps({"result":"OK"})
        
    @cherrypy.expose
    @cherrypy_cors.tools.expose()
    @cherrypy.tools.allow(methods=["POST","OPTIONS"])    
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def setSite(self):
        if cherrypy.request.method == "OPTIONS":
            cherrypy_cors.preflight(allowed_methods=["POST"])
            return None
        data = cherrypy.request.json
        if not checkToken(data): return {"error":"Invalid token"}
        if ("siteName" not in data) or ("data" not in data) :
          return {"error":"Invalid request"}
        
        path = appconfig["paths"]["sites"] + "/" + data["siteName"]
        if not os.path.isfile(path) : return {"error":"Site not exist"}
        with open(path, "w") as new_file:
          print(json.dumps(data["data"]), file=new_file)
        return json.dumps({"result":"OK"})
        
    @cherrypy.expose
    @cherrypy_cors.tools.expose()
    @cherrypy.tools.allow(methods=["POST","OPTIONS"])    
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def restart(self):
        avail = os.listdir("/etc/nginx/sites-available")
        enabled = os.listdir("/etc/nginx/sites-available")
        return json.dumps(avail)
        
    def enable():
      return None
      
    def disable():
      return None