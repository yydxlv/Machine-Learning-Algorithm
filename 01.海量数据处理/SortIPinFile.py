__author__ = 'xilin'
from time import ctime
import os
import operator
tempdir = "d:\\temp"
def sortipinfile():
    fs = []
    if not os.path.exists(tempdir):
        return
    for f in range(0,10):
        fs.append(open(tempdir + "\\tmp_" + str(f)+".txt", 'r+'))
    for f in fs:
        D = {}
        for ip in f:
            if ip in D:
                D[ip] += 1
            else:
                D[ip] = 1
        sorted_D = sorted(D.items(), key=operator.itemgetter(1), reverse=True)
        # sorted_D = sorted(IP.items(), key=lambda d: d[1])
        f.seek(0,0)
        #  Empty the contents of small files
        f.truncate()
        #  Write the sorted IP into the file
        for item in sorted_D:
            f.write(str(item[1]) + "\t" + item[0])
        f.close()

if __name__ == '__main__':
    print("Start At: " + str(ctime()))
    sortipinfile()
    print("End At: " + str(ctime()))
