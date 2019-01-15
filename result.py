#-*- coding:utf8 -*-

def readexp(exp):   #parse a single expression
    
    index = 0
    symbol = ['(']
    maxindex = len(exp)
    while index < maxindex:
        while exp[index] == ' ':
            index += 1
        if exp[index] in ['(',')','0','1','~','+','&','|']:
            symbol.append(exp[index])
            index += 1
            continue
        if exp[index:index+2] == '->':
            symbol.append('->')
            index += 2
            continue
        if exp[index:index+3] == '<->':
            symbol.append('<->')
            index += 3
            continue
        symbol.append(exp[index])
        index += 1
        #assert False,'failed to parse expression'
    symbol.append(')')
    return symbol

def calc(var1,var2,operator,tmpvalue):  #calculate A op B 
    #print '%s %s %s' % (var1,operator,var2)
    
    var1 = int(var1[1])
    if var2 != None:
        var2 = int(var2[1])
    '''    
    if var2 != None:
        print 'calc %s (%d)%s %s' % (var1,operator[0],operator[1],var2)
    else:
        print 'calc (%d)%s %s' % (operator[0],operator[1],var1)
    '''   
    f = lambda x: '1' if x else '0'
    if operator[1] == '~':
        tmpvalue[operator[0]] = f(not var1)
        return f(not var1)
    if operator[1] == '+':
        tmpvalue[operator[0]] = f(var1 ^ var2)
        return f(var1 ^ var2)
    if operator[1] == '&':
        tmpvalue[operator[0]] = f(var1 and var2)
        return f(var1 and var2)
    if operator[1] == '|':
        tmpvalue[operator[0]] = f(var1 + var2)
        return f(var1 + var2)
    if operator[1] == '->':
        if var1 == 1 and var2 == 0:
            tmpvalue[operator[0]] = f(False)
            return f(False)
        else:
            tmpvalue[operator[0]] = f(True)
            return f(True)
    if operator[1] == '<->':
        tmpvalue[operator[0]] = f(not (var1 ^ var2))
        return f(not (var1 ^ var2))
    assert False,'--------'

def check_stack(stack,tmpvalue):    #check stack after deal '~' and ')' symbol
    #print 'stack to be checked' ,stack
    if len(stack) == 1:
        return stack
    index = 0
    for count in range(len(stack)):
        if stack[count][1] == '(':
            index = count
    tmp = stack[index+1:]
    if len(tmp) <= 1:
        return stack
    if tmp[-2][1] == '~':
        var2 = tmp.pop(-1)
        operator = tmp.pop(-1)
        tmp.append((0,calc(var2,None,operator,tmpvalue)))
        stack = stack[:index+1] + tmp
        return check_stack(stack,tmpvalue)
    if tmp[-2][1] in ['+','&','|','->','<->']:
        var2 = tmp.pop(-1)
        operator = tmp.pop(-1)
        var1 = tmp.pop(-1)
        tmp.append((0,calc(var1,var2,operator,tmpvalue)))
        return stack[:index+1] + tmp
    pass

def deal_stack(stack):  #deal with symbol ')'
    #print 'stack',stack
    var = stack.pop(-1)
    stack.pop(-1)
    stack.append(var)
    #print 'after stack',stack
    #pass

def analysis(symbol):   #analysis expression
    length = len(symbol)
    #print symbol
    index = 0
    stack = []
    tmpvalue = {}
    while index < length:
        #print 'stack',stack
        current = index,symbol[index]
        if current[1] in ['(','0','1']:
            stack.append(current)
            index += 1
            continue
        if current[1] == '~':
            if symbol[index+1] == '(':
                stack.append(current)
                index += 1
                continue
            stack.append((0,calc((index+1,symbol[index+1]),None,current,tmpvalue)))
            stack = check_stack(stack,tmpvalue)
            index += 2
            continue
        if current[1] in ['+','&','|','->','<->']:
            if symbol[index+1] in ['(','~']:
                stack.append(current)
                index += 1
                continue
            stack.append((0,calc(stack.pop(-1),(index+1,symbol[index+1]),current,tmpvalue)))
            index += 2
            continue
        if current[1] == ')':
            stack = check_stack(stack,tmpvalue)
            deal_stack(stack)
            stack = check_stack(stack,tmpvalue)
            index += 1
            continue
        assert False,'calc error'
    return stack[0][1],tmpvalue

def output(symbol,result,tmpvalue):
    for i,s in enumerate(symbol[1:-1]):
        if s in ['0','1']:
            print s,
        elif s in ['~','+','&','|','->','<->']:
            print tmpvalue[i+1],
    print result
    pass

def calcresult(expression = '~(0 | 1) <-> (~0 & ~1)'):      #for a single expression ,calculate its value and tmpvalue
    #expression = '~(0 | 1) <-> (~0 & ~1)'
    symbol = readexp(expression)
    result,tmpvalue = analysis(symbol)
    #print symbol
    #print tmpvalue
    #print expression
    #output(symbol,result,tmpvalue)
    return symbol,result,tmpvalue
    
if __name__ == '__main__':
    symbol,result,tmpvalue = calcresult('~(0 | 0) <-> (~0 & ~0)')
    print symbol
    print tmpvalue
    print result
    #output(*calcresult('~(0 | 0) <-> (~0 & ~0)'))
