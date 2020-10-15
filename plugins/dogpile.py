#!usr/bin/env/python

app_emailharvester = None

def search(domain, limit):
    url = 'http://www.dogpile.com/search/web?qsi={counter}&q="%40{word}"'
    app_emailharvester.__init__search(url, domain, limit, 1, 10, 'Dogpile')
    app_emailharvester.process()
    return app_emailharvester.get_emails()


class Plugin:
    def __init__(self, app, conf):
        global app_emailharvester, config
        app.register_plugin('dogpile', {'search': search})
        app_emailharvester = app
