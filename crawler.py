# 爬蟲練習

import bs4
import urllib.request as req
url = "https://www.dcard.tw/f/nba"

# 建立request物件 , 附加 Request Header 的資訊
request = req.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
})

with req.urlopen(request) as response:
    data = response.read().decode("utf-8")

# 解析資料
root = bs4.BeautifulSoup(data, "html.parser")

# print(root.title)
titles = root.find_all("h2", class_="tgn9uw-2")  # 尋找 class="title" 的 tag
# print(titles)
for index in titles:
    if index.span != None:
        print(index.span)
