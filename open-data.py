#網路連線
import urllib.request as request
import json
src="https://mark-proxy-server-php.herokuapp.com/covid19.php"
with request.urlopen(src) as response:
    data=json.load(response) #利用json模組處理json 資料格式

with open("data.txt","w",encoding="utf-8") as file:
    for company in data:
        if company["縣市"] != '' and company["縣市"] != '空值':
            file.write(company["個案研判日"]+' '+company["縣市"]+"\n")

