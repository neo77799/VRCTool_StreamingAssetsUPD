import requests
import urllib.request
import json
import shutil
import os
import time

api = json.loads(requests.get("https://api.github.com/repos/ytdl-org/youtube-dl/releases/latest").text)["assets"]
name = 'youtube-dl.exe'

# Startmessage
print("copy start...")

# Directory
path = './dir.txt'
file = open(path, 'r')
dirlist = file.readlines()
dir = dirlist[0]
file.close()

# Download 
[urllib.request.urlretrieve(x["browser_download_url"],name) 
if x["name"]==name
else print('.', end="") 
for x in api] 

# Existence check
if os.path.exists("./"+name):
    print("OK")
    time.sleep(0.5)
else:
    print("file not found")
    time.sleep(3)
    exit()

# Filecopy
shutil.copy("./"+name, dir)

# Delete
os.remove("./"+name)

# Endmessage
print("processing successful...")
time.sleep(3)
