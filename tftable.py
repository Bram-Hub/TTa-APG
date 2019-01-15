#-*- coding:utf8 -*-
import itertools

def getvar(ex):     #get variables list from expression, like ('A','B','C')
    var_table = []
    for ch in ex:
        if ch in [' ','(',')','<','-','>','+','~','&','|','0','1']:
            continue
        else:
            if ch not in var_table:
                var_table.append(ch)
    return var_table

def genTF(ex = '~(A | B) <-> (~B & ~A)|C'):     #get 0 and 1 combinations of variables
    #ex = '~(A | B) <-> (~B & ~A)|C'
    var_table = getvar(ex)
    tf = []
    tmp = []
    for each in var_table:
        tmp.append((each,'0'))
        tmp.append((each,'1'))
    for i in itertools.combinations(tmp,len(var_table)):
        #print set(zip(*i)[0])
        if set(zip(*i)[0]) == set(var_table):
            #pass
            tmps= ex
            for r in i:
                tmps = tmps.replace(*r)
            tf.append((i,tmps))
    return tf

if __name__ == '__main__':
    tf = genTF()
    for each in tf:
        print each
    pass