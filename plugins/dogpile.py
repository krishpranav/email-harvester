#!usr/bin/env/python
#config = None
app_emailharvester = None





class Plugin:
    def __init__(self, app, conf):#
        global app_emailharvester, config
        #config = conf
        app.register_plugin('dogpile', {'search': search})
        app_emailharvester = app
        