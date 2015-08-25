__author__ = 'xilin'
from time import ctime
import os
import heapq
tempdir = "d:\\temp"
destfile = "d:\\sorted3.txt"
def decorated_file(f):
    """
    Avoid All data Loaded in Memory once in case of Memory Overflow
    Yields an easily sortable tuple.
    """
    for line in f:
        count, ip = line.split('\t', 2)
        yield (-int(count), ip)  # cann't neglect '-'
def mergefiles():
    fs = []
    if not os.path.exists(tempdir):
        return
    for f in range(0,10):
        fs.append(open(tempdir + "\\tmp_" + str(f)+".txt", 'r+'))
    # Store the finally sorted result
    f_dest = open(destfile, "w")
    lines_written = 0
    #  Call the heap sort algorithm : heapq.merge(*iterables)
    for line in heapq.merge(*[decorated_file(f) for f in fs]):
        f_dest.write(str(line[0])+'\n')
        lines_written += 1
    return lines_written
if __name__ == '__main__':
    print("Start At: " + str(ctime()))
    print("sorting completed, total queries: ", mergefiles())
    print("End At: " + str(ctime()))
