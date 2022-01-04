import requests

"""
For more information on the What3Words APIs see
https://developer.what3words.com/public-api/docs

For more information of the Python Requests library see
https://docs.python-requests.org/en/latest/


To find a location on a map try this
https://what3words.com/pretty.resort.quick
"""

apikey = 'IMULZHKN'
uri = 'https://api.what3words.com/v3/convert-to-3wa'
coords = '50.737508,-3.532954'
query = {'coordinates': coords, 'key': apikey} 
r = requests.get(uri, params=query)
print("response->\n", r.text)
print()
print("response['words']->\n", r.json()['words'])
print()

words = r.json()['words']

# To go from 3 words to lat/lon do this

uri = 'https://api.what3words.com/v3/convert-to-coordinates'
query= {'words' : words, 'key': apikey}
r = requests.get(uri, params=query)
print("response->\n", r.text)
print()
print("coordinates->\n", r.json()['coordinates'])
print()

