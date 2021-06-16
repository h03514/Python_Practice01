####隨機模組#####
import random

#隨機選取 單筆
data=random.choice([1,5,7,9,10,20,25])

#隨機選取 可設定多筆
data=random.sample([1,5,7,9,10,20,25],3)

#隨機調換順序 概念像洗牌
data=[1,3,8,12,15]
random.shuffle(data)

#隨機取得亂數
data=random.uniform(60,100) # 可指定兩數之間的亂數
data=random.random() # 0~1 之間隨機亂數

#取得常態分配亂數
#平均數100, 標準差10, 得到的資料多數會在90-110之間
data=random.normalvariate(100,10)



##### 統計模組 #####
import statistics as stat

#平均數
data=stat.mean([1,2,3,4,5,6,200])

#中位數
data=stat.median([1,2,3,4,5,6,200])

#標準差
data=stat.stdev([1,2,3,4,5,6,10])

print(data)