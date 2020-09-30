#!usr/bin/env/python
app_emailharvester = None


def search(domain, limit):
    url = "http://www.exalead.com/search/web/results/?q=%40{word}&elements_per_page=10&start_index={counter}" 
    app_emailharvester.init_search(url, domain, limit, 0, 50, 'Exalead')
    app_emailharvester.process()
    return app_emailharvester.get_emails()


