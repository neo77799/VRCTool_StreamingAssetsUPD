import requests
import urllib.request
import json
import shutil
import os

api = json.loads(requests.get("https://api.github.com/repos/ytdl-org/youtube-dl/releases/latest").text)["assets"]
name = 'youtube-dl.exe'

# Directory
path = './dir.txt'
file = open(path, 'r')
dirlist = file.readlines()
print(dir)
dir = dirlist[0]
file.close()

# Download 
[urllib.request.urlretrieve(x["browser_download_url"],name) 
if x["name"]==name
else print('.', end="") 
for x in api] 

# Existence
if os.path.exists("./"+name):
    print("OK")
else:
    print("NO")

# Filecopy
shutil.copy("./"+name, dir)

# Delete
os.remove("./"+name)
