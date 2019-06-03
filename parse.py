import os

if __name__ == "__main__":
    f = open('created.csv')
    lines = f.readlines()
    f.close()
    for line in lines:
        print(line.split(',')[1])
    