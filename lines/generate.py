#would download the requests package (see notes for details)
import json
import requests
import sys
if len(sys.argv) != 2:
    sys.exit
#this is the API that allows us to talk to apple's server
#this essentially asks apple's server for a song but allows song name input at command line
#whatever apple returns will be in JSON format, which will be converted to a python dict
#that return will be stored in response
#the json.dumps() will format the return into something more readable and user friendly
response = requests.get("https://itunes.apple.com/search?entry=song&limit=1&term=" + sys.argv[1])
print(json.dumps(response.json(), indent=2))
o = response.json

for result in o["results"]:
    print(result["trackName"])

    return f"""
    ======= REPORT =======

    Name: {spacecraft["name"]}
    Distance: {spacecraft.get("distance", "unknown")} AU

    ======================
    """
