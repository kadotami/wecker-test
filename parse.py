import os

if __name__ == "__main__":
    f = open('created.csv')
    lines = f.readlines() # 1行毎にファイル終端まで全て読む(改行文字も含まれる)
    f.close()
    for line in lines:
        print line.split(',')[1]
    