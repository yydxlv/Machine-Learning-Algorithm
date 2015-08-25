__author__ = 'xilin'
from time import ctime
import os
datadir = "d:\\massiveData"
tempdir = "d:\\temp"
def hashfiles():
    fs = []
    if not os.path.exists(tempdir):
        os.makedirs(tempdir)  # create buffer
    for f in range(0, 10):
        fs.append(open(tempdir + "\\tmp_" + str(f)+".txt", 'w'))
    for parent, dirnames, filenames in os.walk(datadir):  # traverse datadir
        for filename in filenames:
            f = open(os.path.join(parent, filename), 'r')
            for ip in f:
                fs[hash(ip) % 10].write(ip)
            f.close()
    for f in fs:
        f.close()

if __name__ == '__main__':
    print("Start At: " + str(ctime()))
    hashfiles()
    print("End At: " + str(ctime()))
