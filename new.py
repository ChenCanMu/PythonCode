import random # 導入randam


def get_int(msg, minimum, default):  #定義get_int函數
    while True:
        try:
            line = input(msg)#鍵入數字
            if not line and default is not None:#判斷not line和default是否存在
                return default#回傳default
            i = int(line)#將鍵入轉為數值
            if i < minimum:#如果i小於最小值
                print("must be >=", minimum)#印出must be >=minimum
            else:
                return i#回傳i
        except ValueError as err:
            print(err)#印出"錯誤訊息"


rows = get_int("rows: ", 1, None)#鍵入行數
columns = get_int("columns: ", 1, None)#鍵入列數
minimum = get_int("minimum (or Enter for 0): ", -1000000, 0)#鍵入最小值

default = 1000#預設值
if default < minimum:#若預設值小於最小值,將最大值設為最小值的兩倍
    default = 2 * minimum
maximum = get_int("maximum (or Enter for " + str(default) + "): ",
                  minimum, default)#鍵入最大值

row = 0#使rows在print時user不會超出預設的值
while row < rows:
    line = ""
    column = 0#使column在print時user不會超出預設的值
    while column < columns:#
        i = random.randint(minimum, maximum)#產生亂數(在最小最大值之間)
        s = str(i)
        while len(s) < 10:#字元小於十,加空格使字元長度為十
            s = " " + s
        line += s#連在一起
        column += 1#換列
    print(line)
    row += 1#換行