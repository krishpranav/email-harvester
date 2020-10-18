#!usr/bin/env/python
app_emailharvester = None

def search(domain, limit):
    url = "http://www.bing.com/search?q=%40{word}&count=50&first={counter}"
    app_emailharvester.init_search(url, domain, limit, 0, 50, 'Bing')
    app_emailharvester.process()
    return app_emailharvester.get_emails()

class Plugin:
    def __init__(self, app, conf):
        global app_emailharvester, config
        app.register_plugin('bing', {'search': search})
        app_emailharvester = app