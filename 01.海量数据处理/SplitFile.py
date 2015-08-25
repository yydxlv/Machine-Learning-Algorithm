__author__ = 'xilin'
from time import ctime
import os
def splitFile(fileLocation, targetFolder):
    file_handler = open(fileLocation, 'r')
    block_size = 9142857  # 14.4M
    line = file_handler.readline()
    temp = []
    countFile = 1
    while line:
        for i in range(block_size):
            if i == (block_size-1):
                # write block to small files
                file_writer = open(targetFolder +"\\file_"+str(countFile)+".txt", 'a+')
                file_writer.writelines(temp)
                file_writer.close()
                temp = []
                print("  file " + str(countFile) + " generated at: " + str(ctime()))
                countFile = countFile + 1
            else:
                line=file_handler.readline()
                temp.append(line)
    file_handler.close()

if __name__ == '__main__':
    print("Start At: " + str(ctime()))
    os.makedirs('d:\\massiveData')
    splitFile("d:\\massiveIP.txt", "d:\\massiveData")
