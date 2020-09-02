import json
import requests
from hashlib import md5
import time
from collections import namedtuple
import random

PUBLIC_KEY = ""
PRIVATE_KEY = ""
i = 1
while i==1:
    timestamp = int(time.time())
    input_string = str(timestamp) + PRIVATE_KEY + PUBLIC_KEY
    hash = md5(input_string.encode("utf-8")).hexdigest()
    offset = str(random.randint(0, 1462))
    requestURL = "https://gateway.marvel.com:443/v1/public/characters?ts="+str(timestamp)+"&apikey="+PUBLIC_KEY+"&offset=" + offset +"&hash="+ hash
    response = requests.get(requestURL)
    response.raise_for_status()
    jsonresponse = response.json()
    print(jsonresponse)
    
    pretty_data = json.dumps(jsonresponse, indent=4)
    character=json.loads(pretty_data, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
    characterNameHtml="""<h1>"""+character.data.results[0].name+"""</h1>"""
    characterImageHtml="""<image src="""+ "\"" +character.data.results[0].thumbnail.path + "." + character.data.results[0].thumbnail.extension +"\""+ """alt="blah" width="100%" height="100%">"""

    f = open('marvel.html', 'w')
    pageContent = """<html><head></head><body>"""+ characterNameHtml + characterImageHtml +"""</body></html>"""
    f.write(pageContent)
    f.close()
    time.sleep( 20 )
