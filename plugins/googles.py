#!usr/bin/env/python

app_emailharvester = None

def search(domain, limit):
	url = 'https://www.google.com/search?num=100&start={counter}&hl=en&q="%40{word}"'
	app_emailharvester.init_search(url, domain, limit, 0, 100, 'Google')
	app_emailharvester.process()
	return app_emailharvester.get_emails()

class Plugin:
	def __init__(self, app, conf):
		global app_emailharvester, config
		app.register_plugin('googles', {'search': search})
		app_emailharvester = app


