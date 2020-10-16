#!usr/bin/env/python
app_emailharvester = None

def search(domain, limit):
    url = 'http://www.baidu.com/search/s?wd="%40{word}"&pn={counter}'
    app_emailharvester.init_search(url, domain, limit, 0, 10, 'Baidu')
    app_emailharvester.process()
    return app_emailharvester.get_emails()

class Plugin:
    def __init__(self, app, conf):
        global app_emailharvester, config
        app.register_plugin('baidu', {'search': search})
        app_emailharvester = app