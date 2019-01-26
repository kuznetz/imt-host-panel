class ApiNginx(object):
    @cherrypy.expose
    def getConfig(self):
        avail = os.listdir("/etc/nginx/sites-available")
        enabled = os.listdir("/etc/nginx/sites-available")
        return json.dumps(avail)
        
    def setSource(self):
        return None
        
    def setTemplate(self):
        return None