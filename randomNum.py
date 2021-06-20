import random
num = random.randint(1, 20)
inputNum = int(input('請輸入一個數字: '))

# 若不等於時跳出的訊息
while inputNum != num:  # 用while在不等於時可重複進入此判斷
    if inputNum > num:
        print('再小一點')
        inputNum = int(input('請輸入一個數字: '))
    elif inputNum < num:
        print('再大一點')
        inputNum = int(input('請輸入一個數字: '))

# 若等於時跳出正確訊息
print('正確')
