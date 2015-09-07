from bs4 import BeautifulSoup as bs4
import pandas as pd
import requests

url_base = 'http://chicago.craigslist.org/search/apa'
params = dict(bedrooms=1, is_furnished=1)
rsp = requests.get(url_base, params=params)

# Requests automatically created the correct url
print "Getting data from %s" % rsp.url

# Use BS4 to parse the response
html = bs4(rsp.text, 'html.parser')

# find_all will pull entries that fit your search criteria
# We have to use brackets to define attrs
# Class is a special word in python so we need to make it a string
apts = html.find_all('p', attrs={'class': 'row'})
print len(apts)