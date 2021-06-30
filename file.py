# 儲存檔案
# file=open("data.txt",mode="w" , encoding="utf-8")
# file.write("hello File\n 讚讚")
# file.close()

# 最佳寫法
import json
with open("data.txt", mode="w", encoding="utf-8") as file:
    file.write("5\n8")

# 讀取檔案
sum = 0

with open("data.txt", mode="r", encoding="utf-8") as file:
    for line in file:
        sum += int(line)
print(sum)

#從檔案讀取JSON, 放入變數DATA內

with open("config.json", mode="r") as file:
    data = json.load(file)


data["name"] = "New Name"  # 修改變數中的資料

# 把最新資料複寫回檔案中

with open("config.json", mode="w") as file:
    json.dump(data, file)

print("name", data["name"])
print("version", data["version"])
