import requests
web = "https://roblox.com"
r = requests.get(web)
print(r.content)
def log_ip():
  r = requests.get('https://ipinfo.io/json')
  print(r.content)
