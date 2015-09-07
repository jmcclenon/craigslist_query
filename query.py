import pandas as pd
import requests

url_base = 'http://chicago.craigslist.org/search/apa'
params = dict(bedrooms=1, is_furnished=1)
rsp = requests.get(url_base, params=params)

# Requests automatically created the correct url
print rsp.url