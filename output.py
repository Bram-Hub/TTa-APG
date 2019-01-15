#-*- coding:utf8 -*-
from tftable import genTF
from result import calcresult,readexp
import StringIO



def output1(symbol,result,tmpvalue):
    for i,s in enumerate(symbol[1:-1]):
        if s in ['0','1']:
            #print s,
            routput.write(s+' ')
        elif s in ['~','+','&','|']:
            #print tmpvalue[i+1],
            routput.write(tmpvalue[i+1]+' ')
        elif s in ['<->']:
            #print ' '+tmpvalue[i+1]+' ',
            routput.write(' '+tmpvalue[i+1]+'  ')
        elif s in ['->']:
            #print ' '+tmpvalue[i+1]+'',
            routput.write(' '+tmpvalue[i+1]+' ')
        else:
            #print ' ',
            routput.write('  ')
    #print result
    routput.write('\n')
    #print
    pass

def formatprint(ex = '(A | ~B | ~C) & (~A | ~B | ~C) & (A | B | ~C) & (A | ~B | C)'):
    global routput
    routput = StringIO.StringIO()
    #ex = '(A | ~B | ~C) & (~A | ~B | ~C) & (A | B | ~C) & (A | ~B | C)'
    #print 
    table = genTF(ex)
    #print ' '.join(zip(*table[0][0])[0]),'|',
    routput.write(' '.join(zip(*table[0][0])[0])+' | ')
    exsymbol = readexp(ex)
    #print ' '.join(exsymbol[1:-1])
    routput.write(' '.join(exsymbol[1:-1])+'\n')
    for each in table:
        #print ' '.join(zip(*each[0])[1]),'|',
        routput.write(' '.join(zip(*each[0])[1])+' | ')
        output1(*calcresult(each[1]))
    pass


if __name__ == '__main__':
    #global routput
    #routput = StringIO.StringIO()
    formatprint()
    print routput.getvalue()
    
