import geocoder
import requests
import json
 
send_url = 'http://freegeoip.net/json'
r = requests.get(send_url)
j = json.loads(r.text)
lat = j['latitude']
lon = j['longitude']
print(lat)
print(lon)
g = geocoder.google([lat, lon], method='reverse')
print(g.city)
print(g.state)
print(g.state_long)
print(g.country)
print(g.country_long)
