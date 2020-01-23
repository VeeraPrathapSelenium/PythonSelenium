import  json

import pandas as pd

from pandas.io.json import  json_normalize

jsonfile=open("Teja.json",encoding="utf8")

rawdata=json.load(jsonfile)
print(rawdata)

smartdata=json_normalize(rawdata)

print(smartdata)