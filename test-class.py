class IO:
    supportSrcs = ["concole", "file"]

    def read(src):
        if src not in IO.supportSrcs:
            print("not suppted")
        else:
            print("Read from", src)


print(IO.supportSrcs)
IO.read("file")
IO.read('internet')

print('-----------')


class Count:
    def count(x, y):
        print(int(x)+int(y))


Count.count(5, 15)


class FullName:
    def __init__(self, firName, lastName):
        self.first = firName
        self.last = lastName


name1 = FullName('Mark', 'C')
print(name1.first+' '+name1.last)

name2 = FullName('Marry', 'L')
print(name2.first+' '+name2.last)


# 讀取檔案
class File:
    def __init__(self, name):
        self.name = name
        self.file = None  # 初始值為None

    def openFile(self):
        # 使用 python 內建 open函式
        self.file = open(self.name, mode="r", encoding="utf-8")

    def read(self):
        return self.file.read()


f1 = File('data.txt')
f1.openFile()
data = f1.read()
# print(data)
