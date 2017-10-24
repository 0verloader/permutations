import time
import sys

def table_hard_copy(table):
    new = []
    for i in table:
        new.append(i)
    return new

def create_anagrams_recursive(length,curr,res):
    tmp = table_hard_copy(curr)
    if len(tmp) == length:
        print curr
        res.append(curr)
    for i in range(length):
        zz = table_hard_copy(tmp)
        if i not in zz:
            zz.append(i)
            create_anagrams_recursive(length,zz,res)
    return zz


def create_anagrams(length):
    a=[]
    res=[]
    t1 = time.time()
    create_anagrams_recursive(length,a,res)
    t2 = time.time()
    print "______________________"
    print len(res),"samples"
    print t2-t1,"s."
    return res

create_anagrams(int(sys.argv[1]))