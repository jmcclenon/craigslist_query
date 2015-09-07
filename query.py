from bs4 import BeautifulSoup as bs4
import pandas as pd
import requests

def find_size_and_brs(size):
	split = size.strip('/- ').split(' - ')
	if len(split) == 2:
		n_brs = split[0].replace('br','')
		this_size = split[1].replace('ft2', '')
	elif 'br' in split[0]:
		n_brs = split[0].replace('br', '')
		this_size = np.nan
	elif 'ft2' in split[0]:
		this_size = split[0].replace('ft2', '')
		n_brs = np.nan
	return float(this_size), float(n_brs)

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

this_apt = apts[15]
size = this_apt.findAll(attrs={'class': 'housing'})[0].text
this_size, n_brs = find_size_and_brs(size)
print this_size, n_brs