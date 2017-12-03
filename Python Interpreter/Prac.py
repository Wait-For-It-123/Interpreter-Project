import sys
import math

def main(output):
    input_list = []
    finalized_values_list = []
    stack = []
    let_bound_items = []
    answer = []
    toDelete = []
    bindDict = {}
    let_bindDict = {}
    fun_Dict = {}
    fun_bindDict = {}
    boundB4Fun = {}
    multipleLetBoundVar_dict = {}
    nestedFunCall_dict = {}
    argToBindToFunOutput = []
    stack_count = 0
    input_list_count = 0
    let_count = 0
    stack_count_b4_let = 0
    toDeleteCounter = 0
    mlbv = 0
    multipleLetBoundVarCount = 0
    is_inoutfun = False
    returnInFun = False
    multipleLetBoundVarDictIsEmpty = True
    nestedFunCall = False

    input_list.append('fun stop arg')
    input_list.append('push 1')
    input_list.append('return')
    input_list.append('funEnd')
    input_list.append('fun factorial arg')
    input_list.append('push arg')
    input_list.append('push 1')
    input_list.append('sub')
    input_list.append('push 1')
    input_list.append('push arg')
    input_list.append('equal')
    input_list.append('push factorial')
    input_list.append('push stop')
    input_list.append('if')
    input_list.append('call')
    input_list.append('push arg')
    input_list.append('mul')
    input_list.append('return')
    input_list.append('funEnd')
    input_list.append('push 3')
    input_list.append('push factorial')
    input_list.append('call')
    input_list.append('quit')

# Begin here by looping through each item of the init_readin_list that was set up
# The soul purpose of this loop is to create the finalized_values_list
# that I will be working with by taking out 'push #' and replacing it with
# just the integer that I will be working with along with passing through the
# other functions that I will need in the finalized_values_list
# such ass add, sub , mul ...

    for item in input_list:
        if 'push' in item:
            values = item.split(" ")
            needed_value = values[1]
            if '.' in needed_value:
                finalized_values_list.append(':error:')
            elif str.isdigit(needed_value) == True:
                finalized_values_list.append(int(needed_value))
            elif '-' in needed_value:
                if str.isdigit(needed_value[1:]) == True:
                    finalized_values_list.append(int(needed_value))
                else:
                    finalized_values_list.append(':error:')
            elif str.isdigit(needed_value[0:1]) == True and str.isdigit(needed_value[1:0]) == False:
                finalized_values_list.append(':error:')
            elif needed_value == 'sin':
                finalized_values_list.append(needed_value)
            elif needed_value == 'stop':
                finalized_values_list.append(needed_value)
            else:
                finalized_values_list.append(item.strip(' push'))
        elif 'fun' in item or 'inOutFun' in item:
            if item == 'funEnd':
                finalized_values_list.append(item)
            else:
                values = item.split(" ")
                act_fun = values[0]
                fun_name = values[1]
                arg = values[2]
                if act_fun == 'fun' or act_fun == 'inOutFun':
                    finalized_values_list.append(act_fun)
                else:
                    finalized_values_list.append(':error:')
                if '.' in fun_name:
                    finalized_values_list.append(':error:')
                elif '-' in fun_name:
                    finalized_values_list.append(':error:')
                elif str.isdigit(fun_name[0:1]) == True and str.isdigit(fun_name[1:0]) == False:
                    finalized_values_list.append(':error:')
                else:
                    finalized_values_list.append(fun_name)
                if '.' in arg:
                    finalized_values_list.append(':error:')
                elif '-' in arg:
                    finalized_values_list.append(':error:')
                elif str.isdigit(arg[0:1]) == True and str.isdigit(arg[1:0]) == False:
                    finalized_values_list.append(':error:')
                else:
                    finalized_values_list.append(arg)
        elif item == ':true:':
            finalized_values_list.append(item)
        elif item == ':false:':
            finalized_values_list.append(item)
        elif item == 'add':
            finalized_values_list.append(item)
        elif item == 'neg':
            finalized_values_list.append(item)
        elif item == 'mul':
            finalized_values_list.append(item)
        elif item == 'sub':
            finalized_values_list.append(item)
        elif item == 'div':
            finalized_values_list.append(item)
        elif item == 'rem':
            finalized_values_list.append(item)
        elif item == 'pop':
            finalized_values_list.append(item)
        elif item == 'swap':
            finalized_values_list.append(item)
        elif item == ':error:':
            finalized_values_list.append(item)
        elif item == 'and':
            finalized_values_list.append(item)
        elif item == 'or':
            finalized_values_list.append(item)
        elif item == 'not':
            finalized_values_list.append(item)
        elif item == 'equal':
            finalized_values_list.append(item)
        elif item == 'lessThan':
            finalized_values_list.append(item)
        elif item == 'bind':
            finalized_values_list.append(item)
        elif item == 'if':
            finalized_values_list.append(item)
        elif item == 'let':
            finalized_values_list.append(item)
        elif item == 'end':
            finalized_values_list.append(item)
        elif item == 'funEnd':
            finalized_values_list.append(item)
        elif item == 'call':
            finalized_values_list.append(item)
        elif item == 'return':
            finalized_values_list.append(item)
        elif item == 'quit':
            finalized_values_list.append(item)
        else:
            finalized_values_list.append(':error:')

# The purpose of this loop is to look through my finalized_values_list element
# by element and append values such as integers, errors, bools, to my stack
# and once i reach an opperation check my stack and see if the action can be
# performed, if it can then pop the necessary elements from the stack and
# and use them to preform tge function such as add, sub, mul, div, etc
# the else statment at the bottom is reseved for when I hit quit and that is
# where I open my output file and print the elements in my stack.

    print("finalized_values_list: ", finalized_values_list)

    for item in finalized_values_list:
        #print("main loop looking at: ", item)
        input_list_count += 1
        if type(item) == int:
            stack.append(item)
            stack_count += 1
        elif item != ':error:' and item != ':true:' and item != ':false:' and item != 'add' and item != 'neg' and item != 'mul' and item != 'sub' and item != 'div' and item != 'rem' and item != 'swap' and item != 'pop' and item != 'and' and item != 'or' and item != 'not' and item != 'equal' and item != 'lessThan' and item != 'bind' and item != 'if' and item != 'let' and item != 'end' and item != 'fun' and item != 'funEnd' and item != 'call' and item != 'return' and item != 'inOutFun' and item != 'quit':
            stack.append(item)
            stack_count += 1
        elif item == ':error:':
            stack.append(item)
            stack_count += 1
        elif item == ':true:':
            stack.append(item)
            stack_count += 1
        elif item == ':false:':
            stack.append(item)
            stack_count += 1
        elif item == 'add':
            if stack_count >= 2:
                if type(stack[stack_count - 1]) == int and type(stack[stack_count - 2]) == int:
                    x = stack.pop()
                    y = stack.pop()
                    z = x + y
                    stack.append(z)
                    stack_count -= 1
                elif stack[stack_count - 1] in bindDict and stack[stack_count - 2] in bindDict:
                    x = stack.pop()
                    y = stack.pop()
                    if type(bindDict[x]) == int and type(bindDict[y]) == int:
                        z = bindDict[x] + bindDict[y]
                        stack.append(z)
                        stack_count -= 1
                    else:
                        stack.append(y)
                        stack.append(x)
                        stack.append(':error:')
                        stack_count += 1
                elif stack[stack_count - 1] in bindDict:
                    x = stack.pop()
                    y = stack.pop()
                    if type(bindDict[x]) == int and type(y) == int:
                        z = bindDict[x] + y
                        stack.append(z)
                        stack_count -= 1
                    else:
                        stack.append(y)
                        stack.append(x)
                        stack.append(':error:')
                        stack_count += 1
                elif stack[stack_count - 2] in bindDict:
                    x = stack.pop()
                    y = stack.pop()
                    if type(x) == int and type(bindDict[y]) == int:
                        z = x + bindDict[y]
                        stack.append(z)
                        stack_count -= 1
                    else:
                        stack.append(y)
                        stack.append(x)
                        stack.append(':error:')
                        stack_count += 1
                else:
                    stack.append(':error:')
                    stack_count += 1
            else:
                stack.append(':error:')
                stack_count += 1
        elif item == 'neg':
            if stack_count >= 1:
                if type(stack[stack_count - 1]) == int:
                    x = stack.pop()
                    x *= -1
                    stack.append(x)
                elif stack[stack_count - 1] in bindDict:
                    x = stack.pop()
                    if type(bindDict[x]) == int:
                        z = bindDict[x] * -1
                        stack.append(z)
                    else:
                        stack.append(x)
                        stack.append(':error:')
                        stack_count += 1
                else:
                    stack.append(':error:')
                    stack_count += 1
            else:
                stack.append(':error:')
                stack_count += 1
        elif item == 'mul':
            if stack_count >= 2:
                if type(stack[stack_count - 1]) == int and type(stack[stack_count - 2]) == int:
                    x = stack.pop()
                    y = stack.pop()
                    z = x * y
                    stack.append(z)
                    stack_count -= 1
                elif stack[stack_count - 1] in bindDict and stack[stack_count - 2] in bindDict:
                    x = stack.pop()
                    y = stack.pop()
                    if type(bindDict[x]) == int and type(bindDict[y]) == int:
                        z = bindDict[x] * bindDict[y]
                        stack.append(z)
                        stack_count -= 1
                    else:
                        stack.append(y)
                        stack.append(x)
                        stack.append(':error:')
                        stack_count += 1
                elif stack[stack_count - 1] in bindDict:
                    x = stack.pop()
                    y = stack.pop()
                    if type(bindDict[x]) == int and type(y) == int:
                        z = bindDict[x] * y
                        stack.append(z)
                        stack_count -= 1
                    else:
                        stack.append(y)
                        stack.append(x)
                        stack.append(':error:')
                        stack_count += 1
                elif stack[stack_count - 2] in bindDict:
                    x = stack.pop()
                    y = stack.pop()
                    if type(x) == int and type(bindDict[y]) == int:
                        z = x * bindDict[y]
                        stack.append(z)
                        stack_count -= 1
                    else:
                        stack.append(y)
                        stack.append(x)
                        stack.append(':error:')
                        stack_count += 1
                else:
                    stack.append(':error:')
                    stack_count += 1
            else:
                stack.append(':error:')
                stack_count += 1
        elif item == 'sub':
            if stack_count >= 2:
                if type(stack[stack_count - 1]) == int and type(stack[stack_count - 2]) == int:
                    x = stack.pop()
                    y = stack.pop()
                    z = y - x
                    stack.append(z)
                    stack_count -= 1
                elif stack[stack_count - 1] in bindDict and stack[stack_count - 2] in bindDict:
                    x = stack.pop()
                    y = stack.pop()
                    if type(bindDict[x]) == int and type(bindDict[y]) == int:
                        z = bindDict[y] - bindDict[x]
                        stack.append(z)
                        stack_count -= 1
                    else:
                        stack.append(y)
                        stack.append(x)
                        stack.append(':error:')
                        stack_count += 1
                elif stack[stack_count - 1] in bindDict:
                    x = stack.pop()
                    y = stack.pop()
                    if type(bindDict[x]) == int and type(y) == int:
                        z =  y - bindDict[x]
                        stack.append(z)
                        stack_count -= 1
                    else:
                        stack.append(y)
                        stack.append(x)
                        stack.append(':error:')
                        stack_count += 1
                elif stack[stack_count - 2] in bindDict:
                    x = stack.pop()
                    y = stack.pop()
                    if type(x) == int and type(bindDict[y]) == int:
                        z = bindDict[y] - x
                        stack.append(z)
                        stack_count -= 1
                    else:
                        stack.append(y)
                        stack.append(x)
                        stack.append(':error:')
                        stack_count += 1
                else:
                    stack.append(':error:')
                    stack_count += 1
            else:
                stack.append(':error:')
                stack_count += 1
        elif item == 'div':
            if stack_count >= 2:
                if type(stack[stack_count - 1]) == int and type(stack[stack_count - 2]) == int:
                    y = stack.pop()
                    x = stack.pop()
                    if y != 0:
                        z = x / y
                        stack.append(int(z))
                        stack_count -= 1
                    else:
                        stack.append(x)
                        stack.append(y)
                        stack.append(':error:')
                        stack_count += 1
                elif stack[stack_count - 1] in bindDict and stack[stack_count - 2] in bindDict:
                    y = stack.pop()
                    x = stack.pop()
                    if type(bindDict[x]) == int and type(bindDict[y]) == int:
                        if bindDict[y] != 0:
                            z = bindDict[x] / bindDict[y]
                            stack.append(int(z))
                            stack_count -= 1
                        else:
                            stack.append(x)
                            stack.append(y)
                            stack.append(':error:')
                            stack_count += 1
                    else:
                        stack.append(x)
                        stack.append(y)
                        stack.append(':error:')
                        stack_count += 1
                elif stack[stack_count - 1] in bindDict:
                    y = stack.pop()
                    x = stack.pop()
                    if type(x) == int and type(bindDict[y]) == int:
                        if bindDict[y] != 0:
                            z = x / bindDict[y]
                            stack.append(int(z))
                            stack_count -= 1
                        else:
                            stack.append(x)
                            stack.append(y)
                            stack.append(':error:')
                            stack_count += 1
                    else:
                        stack.append(x)
                        stack.append(y)
                        stack.append(':error:')
                        stack_count += 1
                elif stack[stack_count - 2] in bindDict:
                    y = stack.pop()
                    x = stack.pop()
                    if type(bindDict[x]) == int and type(y) == int:
                        if y != 0:
                            z = bindDict[x] / y
                            stack.append(int(z))
                            stack_count -= 1
                        else:
                            stack.append(x)
                            stack.append(y)
                            stack.append(':error:')
                            stack_count += 1
                    else:
                        stack.append(x)
                        stack.append(y)
                        stack.append(':error:')
                        stack_count += 1
                else:
                    stack.append(':error:')
                    stack_count += 1
            else:
                stack.append(':error:')
                stack_count += 1
        elif item == 'rem':
            if stack_count >= 2:
                if type(stack[stack_count - 1]) == int and type(stack[stack_count - 2]) == int:
                    y = stack.pop()
                    x = stack.pop()
                    if y != 0:
                        z = x % y
                        stack.append(int(z))
                        stack_count -= 1
                    else:
                        stack.append(x)
                        stack.append(y)
                        stack.append(':error:')
                        stack_count += 1
                elif stack[stack_count - 1] in bindDict and stack[stack_count - 2] in bindDict:
                    y = stack.pop()
                    x = stack.pop()
                    if type(bindDict[x]) == int and type(bindDict[y]) == int:
                        if bindDict[y] != 0:
                            z = bindDict[x] % bindDict[y]
                            stack.append(int(z))
                            stack_count -= 1
                        else:
                            stack.append(x)
                            stack.append(y)
                            stack.append(':error:')
                            stack_count += 1
                    else:
                        stack.append(x)
                        stack.append(y)
                        stack.append(':error:')
                        stack_count += 1
                elif stack[stack_count - 1] in bindDict:
                    y = stack.pop()
                    x = stack.pop()
                    if type(x) == int and type(bindDict[y]) == int:
                        if bindDict[y] != 0:
                            z = x % bindDict[y]
                            stack.append(int(z))
                            stack_count -= 1
                        else:
                            stack.append(x)
                            stack.append(y)
                            stack.append(':error:')
                            stack_count += 1
                    else:
                        stack.append(x)
                        stack.append(y)
                        stack.append(':error:')
                        stack_count += 1
                elif stack[stack_count - 2] in bindDict:
                    y = stack.pop()
                    x = stack.pop()
                    if type(bindDict[x]) == int and type(y) == int:
                        if y != 0:
                            z = bindDict[x] % y
                            stack.append(int(z))
                            stack_count -= 1
                        else:
                            stack.append(x)
                            stack.append(y)
                            stack.append(':error:')
                            stack_count += 1
                    else:
                        stack.append(x)
                        stack.append(y)
                        stack.append(':error:')
                        stack_count += 1
                else:
                    stack.append(':error:')
                    stack_count += 1
            else:
                stack.append(':error:')
                stack_count += 1
        elif item == 'pop':
            if stack_count >= 1:
                stack.pop()
                stack_count -= 1
            else:
                stack.append(':error:')
                stack_count += 1
        elif item == 'swap':
            if stack_count >= 2:
                x = stack.pop()
                y = stack.pop()
                stack.append(x)
                stack.append(y)
            else:
                stack.append(':error:')
                stack_count += 1
        elif item == 'and':
            if stack_count >= 2:
                x = stack.pop()
                y = stack.pop()
                if x == ':true:' and y == ':true:':
                    stack.append(':true:')
                    stack_count -= 1
                elif x == ':true:' and y == ':false:':
                    stack.append(':false:')
                    stack_count -= 1
                elif x == ':false:' and y == ':true:':
                    stack.append(':false:')
                    stack_count -= 1
                elif x == ':false:' and y == ':false:':
                    stack.append(':false:')
                    stack_count -= 1
                elif x in bindDict and y in bindDict:
                    if bindDict[x] == ':true:' and bindDict[y] == ':true:':
                        stack.append(':true:')
                        stack_count -= 1
                    elif bindDict[x] == ':true:' and bindDict[y] == ':false:':
                        stack.append(':false:')
                        stack_count -= 1
                    elif bindDict[x] == ':false:' and bindDict[y] == ':true:':
                        stack.append(':false:')
                        stack_count -= 1
                    elif bindDict[x] == ':false:' and bindDict[y] == ':false:':
                        stack.append(':false:')
                        stack_count -= 1
                    else:
                        stack.append(y)
                        stack.append(x)
                        stack.append(':error:')
                        stack_count += 1
                elif x in bindDict:
                    if bindDict[x] == ':true:' and y == ':true:':
                        stack.append(':true:')
                        stack_count -= 1
                    elif bindDict[x] == ':true:' and y == ':false:':
                        stack.append(':false:')
                        stack_count -= 1
                    elif bindDict[x] == ':false:' and y == ':true:':
                        stack.append(':false:')
                        stack_count -= 1
                    elif bindDict[x] == ':false:' and y == ':false:':
                        stack.append(':false:')
                        stack_count -= 1
                    else:
                        stack.append(y)
                        stack.append(x)
                        stack.append(':error:')
                        stack_count += 1
                elif y in bindDict:
                    if x == ':true:' and bindDict[y] == ':true:':
                        stack.append(':true:')
                        stack_count -= 1
                    elif x == ':true:' and bindDict[y] == ':false:':
                        stack.append(':false:')
                        stack_count -= 1
                    elif x == ':false:' and bindDict[y] == ':true:':
                        stack.append(':false:')
                        stack_count -= 1
                    elif x == ':false:' and bindDict[y] == ':false:':
                        stack.append(':false:')
                        stack_count -= 1
                    else:
                        stack.append(y)
                        stack.append(x)
                        stack.append(':error:')
                        stack_count += 1
                else:
                    stack.append(y)
                    stack.append(x)
                    stack.append(':error:')
                    stack_count += 1
            else:
                stack.append(':error:')
                stack_count += 1
        elif item == 'or':
            if stack_count >= 2:
                x = stack.pop()
                y = stack.pop()
                if x == ':true:' and y == ':true:':
                    stack.append(':true:')
                    stack_count -= 1
                elif x == ':true:' and y == ':false:':
                    stack.append(':true:')
                    stack_count -= 1
                elif x == ':false:' and y == ':true:':
                    stack.append(':true:')
                    stack_count -= 1
                elif x == ':false:' and y == ':false:':
                    stack.append(':false:')
                    stack_count -= 1
                elif x in bindDict and y in bindDict:
                    if bindDict[x] == ':true:' and bindDict[y] == ':true:':
                        stack.append(':true:')
                        stack_count -= 1
                    elif bindDict[x] == ':true:' and bindDict[y] == ':false:':
                        stack.append(':true:')
                        stack_count -= 1
                    elif bindDict[x] == ':false:' and bindDict[y] == ':true:':
                        stack.append(':true:')
                        stack_count -= 1
                    elif bindDict[x] == ':false:' and bindDict[y] == ':false:':
                        stack.append(':false:')
                        stack_count -= 1
                    else:
                        stack.append(y)
                        stack.append(x)
                        stack.append(':error:')
                        stack_count += 1
                elif x in bindDict:
                    if bindDict[x] == ':true:' and y == ':true:':
                        stack.append(':true:')
                        stack_count -= 1
                    elif bindDict[x] == ':true:' and y == ':false:':
                        stack.append(':true:')
                        stack_count -= 1
                    elif bindDict[x] == ':false:' and y == ':true:':
                        stack.append(':true:')
                        stack_count -= 1
                    elif bindDict[x] == ':false:' and y == ':false:':
                        stack.append(':false:')
                        stack_count -= 1
                    else:
                        stack.append(y)
                        stack.append(x)
                        stack.append(':error:')
                        stack_count += 1
                elif y in bindDict:
                    if x == ':true:' and bindDict[y] == ':true:':
                        stack.append(':true:')
                        stack_count -= 1
                    elif x == ':true:' and bindDict[y] == ':false:':
                        stack.append(':true:')
                        stack_count -= 1
                    elif x == ':false:' and bindDict[y] == ':true:':
                        stack.append(':true:')
                        stack_count -= 1
                    elif x == ':false:' and bindDict[y] == ':false:':
                        stack.append(':false:')
                        stack_count -= 1
                    else:
                        stack.append(y)
                        stack.append(x)
                        stack.append(':error:')
                        stack_count += 1
                else:
                    stack.append(y)
                    stack.append(x)
                    stack.append(':error:')
                    stack_count += 1
            else:
                stack.append(':error:')
                stack_count += 1
        elif item == 'not':
            if stack_count >= 1:
                x = stack.pop()
                if x == ':true:':
                    stack.append(':false:')
                elif x == ':false:':
                    stack.append(':true:')
                elif x in bindDict:
                    if bindDict[x] == ':true:':
                        stack.append(':false:')
                    elif bindDict[x] == ':false:':
                        stack.append(':true:')
                    else:
                        stack.append(x)
                        stack.append(':error:')
                        stack_count += 1
                else:
                    stack.append(x)
                    stack.append(':error:')
                    stack_count += 1
            else:
                stack.append(':error:')
                stack_count += 1
        elif item == 'equal':
            if stack_count >= 2:
                if type(stack[stack_count - 1]) == int and type(stack[stack_count - 2]) == int:
                    x = stack.pop()
                    y = stack.pop()
                    if x == y:
                        stack.append(':true:')
                        stack_count -= 1
                    else:
                        stack.append(':false:')
                        stack_count -= 1
                elif stack[stack_count - 1] in bindDict and stack[stack_count - 2] in bindDict:
                    x = stack.pop()
                    y = stack.pop()
                    if type(bindDict[x]) == int and type(bindDict[y]) == int:
                        if bindDict[x] == bindDict[y]:
                            stack.append(':true:')
                            stack_count -= 1
                        else:
                            stack.append(':false:')
                            stack_count -= 1
                    else:
                        stack.append(y)
                        stack.append(x)
                        stack.append(':error:')
                        stack_count += 1
                elif stack[stack_count - 1] in bindDict:
                    x = stack.pop()
                    y = stack.pop()
                    if type(bindDict[x]) == int and type(y) == int:
                        if bindDict[x] == y:
                            stack.append(':true:')
                            stack_count -= 1
                        else:
                            stack.append(':false:')
                            stack_count -= 1
                    else:
                        stack.append(y)
                        stack.append(x)
                        stack.append(':error:')
                        stack_count += 1
                elif stack[stack_count - 2] in bindDict:
                    x = stack.pop()
                    y = stack.pop()
                    if type(x) == int and type(bindDict[y]) == int:
                        if x == bindDict[y]:
                            stack.append(':true:')
                            stack_count -= 1
                        else:
                            stack.append(':false:')
                            stack_count -= 1
                    else:
                        stack.append(y)
                        stack.append(x)
                        stack.append(':error:')
                        stack_count += 1
                else:
                    stack.append(':error:')
                    stack_count += 1
            else:
                stack.append(':error:')
                stack_count += 1
        elif item == 'lessThan':
            if stack_count >= 2:
                if type(stack[stack_count - 1]) == int and type(stack[stack_count - 2]) == int:
                    x = stack.pop()
                    y = stack.pop()
                    if x > y:
                        stack.append(':true:')
                        stack_count -= 1
                    else:
                        stack.append(':false:')
                        stack_count -= 1
                elif stack[stack_count - 1] in bindDict and stack[stack_count - 2] in bindDict:
                    x = stack.pop()
                    y = stack.pop()
                    if type(bindDict[x]) == int and type(bindDict[y]) == int:
                        if bindDict[x] > bindDict[y]:
                            stack.append(':true:')
                            stack_count -= 1
                        else:
                            stack.append(':false:')
                            stack_count -= 1
                    else:
                        stack.append(y)
                        stack.append(x)
                        stack.append(':error:')
                        stack_count += 1
                elif stack[stack_count - 1] in bindDict:
                    x = stack.pop()
                    y = stack.pop()
                    if type(bindDict[x]) == int and type(y) == int:
                        if bindDict[x] > y:
                            stack.append(':true:')
                            stack_count -= 1
                        else:
                            stack.append(':false:')
                            stack_count -= 1
                    else:
                        stack.append(y)
                        stack.append(x)
                        stack.append(':error:')
                        stack_count += 1
                elif stack[stack_count - 2] in bindDict:
                    x = stack.pop()
                    y = stack.pop()
                    if type(x) == int and type(bindDict[y]) == int:
                        if x > bindDict[y]:
                            stack.append(':true:')
                            stack_count -= 1
                        else:
                            stack.append(':false:')
                            stack_count -= 1
                    else:
                        stack.append(y)
                        stack.append(x)
                        stack.append(':error:')
                        stack_count += 1
                else:
                    stack.append(':error:')
                    stack_count += 1
            else:
                stack.append(':error:')
                stack_count += 1
        elif item == 'bind':
            if stack_count >= 2:
                if stack[stack_count - 2] != ':true:' and stack[stack_count - 2] != ':false:' and stack[stack_count - 2] != 'add' and stack[stack_count - 2] != 'sub' and stack[stack_count - 2] != 'mul' and stack[stack_count - 2] != 'div' and stack[stack_count - 2] != 'rem' and stack[stack_count - 2] != 'neg' and stack[stack_count - 2] != 'pop' and stack[stack_count - 2] != 'swap' and stack[stack_count - 2] != ':error:' and stack[stack_count - 2] != 'and' and stack[stack_count - 2] != 'or' and stack[stack_count - 2] != 'not' and stack[stack_count - 2] != 'equal' and stack[stack_count - 2] != 'lessThan' and stack[stack_count - 2] != 'bind' and stack[stack_count - 2] != 'if' and stack[stack_count - 2] != 'let' and stack[stack_count - 2] != 'end':
                    if stack[stack_count - 1] != 'add' and stack[stack_count - 1] != 'sub' and stack[stack_count - 1] != 'mul' and stack[stack_count - 1] != 'div' and stack[stack_count - 1] != 'rem' and stack[stack_count - 1] != 'neg' and stack[stack_count - 1] != 'pop' and stack[stack_count - 1] != 'swap' and stack[stack_count - 1] != ':error:' and stack[stack_count - 1] != 'and' and stack[stack_count - 1] != 'or' and stack[stack_count - 1] != 'not' and stack[stack_count - 1] != 'equal' and stack[stack_count - 1] != 'lessThan' and stack[stack_count - 1] != 'bind' and stack[stack_count - 1] != 'if' and stack[stack_count - 1] != 'let' and stack[stack_count - 1] != 'end':
                        x = stack.pop()
                        y = stack.pop()
                        if type(y) != int and '"' not in y:
                            if x in bindDict:
                                bindDict[y] = bindDict[x]
                                stack.append(':unit:')
                                stack_count -= 1
                            elif type(x) == str and '"' not in x and x != ':true:' and x != ':false:' and x != ':unit:':
                                stack.append(y)
                                stack.append(x)
                                stack.append(':error:')
                                stack_count += 1
                            else:
                                bindDict[y] = x
                                stack.append(':unit:')
                                stack_count -= 1
                        else:
                            stack.append(y)
                            stack.append(x)
                            stack.append(':error:')
                            stack_count += 1
                    else:
                        stack.append(':error:')
                        stack_count += 1
                else:
                    stack.append(':error:')
                    stack_count += 1
            else:
                stack.append(':error:')
                stack_count += 1
        elif item == 'if':
            if stack_count >= 3:
                if stack[stack_count - 3] == ':true:' or stack[stack_count - 3] == ':false:':
                    x = stack.pop()
                    y = stack.pop()
                    z = stack.pop()
                    if z == ':true:':
                        stack.append(x)
                        stack_count -= 2
                    elif z == ':false:':
                        stack.append(y)
                        stack_count -= 2
                    else:
                        stack.append(z)
                        stack.append(y)
                        stack.append(x)
                        stack.append(':error:')
                        stack_count += 1
                elif stack[stack_count - 3] in bindDict:
                    x = stack[stack_count - 3]
                    if bindDict[x] == ':true:' or bindDict[x] == ':false:':
                        x = stack.pop()
                        y = stack.pop()
                        z = stack.pop()
                        if bindDict[z] == ':true:':
                            stack.append(x)
                            stack_count -= 2
                        elif bindDict[z] == ':false:':
                            stack.append(y)
                            stack_count -= 2
                        else:
                            stack.append(z)
                            stack.append(y)
                            stack.append(x)
                            stack.append(':error:')
                            stack_count += 1
                    else:
                        stack.append(':error:')
                        stack_count += 1
                else:
                    stack.append(':error:')
                    stack_count += 1
            else:
                stack.append(':error:')
                stack_count += 1
        elif item == 'let':
            if let_count == 0:
                stack_count_b4_let = stack_count
                let_bindDict.update(bindDict)
            stack_count += 1
            let_count += 1
            tempStack = []
            stack.append(tempStack)
            for item in finalized_values_list[input_list_count:]:
                #print("Now printing the finalized_values_list: ", finalized_values_list)
                #print('this is the current tempStack: ', tempStack)
                #print('this is the current need to delete list: ', toDelete)
                #print('In the let looking at: ', item)
                if toDeleteCounter > 0:
                    if item in toDelete:
                        #print('about to delete because its apart of the function that ive already taken care of: ', item)
                        finalized_values_list.remove(item)
                        toDeleteCounter -= 1
                elif type(item) == int:
                    finalized_values_list.remove(item)
                    tempStack.append(item)
                elif item != ':error:' and item != ':true:' and item != ':false:' and item != 'add' and item != 'neg' and item != 'mul' and item != 'sub' and item != 'div' and item != 'rem' and item != 'swap' and item != 'pop' and item != 'and' and item != 'or' and item != 'not' and item != 'equal' and item != 'lessThan' and item != 'bind' and item != 'if' and item != 'let' and item != 'end' and item != 'fun' and item != 'funEnd' and item != 'call' and item != 'return' and item != 'inOutFun' and item != 'quit':
                    finalized_values_list.remove(item)
                    tempStack.append(item)
                    #print("In the long conditionial that should append names to the tempStack and remove them from the finalized_values_list, looking at: ", item)
                elif item == ':error:':
                    finalized_values_list.remove(item)
                    tempStack.append(item)
                elif item == ':true:':
                    finalized_values_list.remove(item)
                    tempStack.append(item)
                elif item == ':false:':
                    finalized_values_list.remove(item)
                    tempStack.append(item)
                elif item == 'add':
                    finalized_values_list.remove(item)
                    if len(tempStack) >= 2:
                        x = tempStack.pop()
                        y = tempStack.pop()
                        if type(x) == int and type(y) == int:
                            z = x + y
                            tempStack.append(z)
                        elif x in let_bindDict and y in let_bindDict:
                            if type(let_bindDict[x]) == int and type(let_bindDict[y]) == int:
                                z = let_bindDict[x] + let_bindDict[y]
                                tempStack.append(z)
                            else:
                                tempStack.append(y)
                                tempStack.append(x)
                                tempStack.append(':error:')
                        elif x in let_bindDict:
                            if type(let_bindDict[x]) == int and type(y) == int:
                                z = let_bindDict[x] + y
                                tempStack.append(z)
                            else:
                                tempStack.append(y)
                                tempStack.append(x)
                                tempStack.append(':error:')
                        elif y in let_bindDict:
                            if type(x) == int and type(let_bindDict[y]) == int:
                                z = x + let_bindDict[y]
                                tempStack.append(z)
                            else:
                                tempStack.append(y)
                                tempStack.append(x)
                                tempStack.append(':error:')
                        else:
                            tempStack.append(y)
                            tempStack.append(x)
                            tempStack.append(':error:')
                    else:
                        tempStack.append(':error:')
                elif item == 'sub':
                    finalized_values_list.remove(item)
                    if len(tempStack) >= 2:
                        x = tempStack.pop()
                        y = tempStack.pop()
                        if type(x) == int and type(y) == int:
                            z = y - x
                            tempStack.append(z)
                        elif x in let_bindDict and y in let_bindDict:
                            if type(let_bindDict[x]) == int and type(let_bindDict[y]) == int:
                                z = let_bindDict[y] - let_bindDict[x]
                                tempStack.append(z)
                            else:
                                tempStack.append(y)
                                tempStack.append(x)
                                tempStack.append(':error:')
                        elif x in let_bindDict:
                            if type(let_bindDict[x]) == int and type(y) == int:
                                z =  y - let_bindDict[x]
                                tempStack.append(z)
                            else:
                                tempStack.append(y)
                                tempStack.append(x)
                                tempStack.append(':error:')
                        elif y in let_bindDict:
                            if type(x) == int and type(let_bindDict[y]) == int:
                                z = let_bindDict[y] - x
                                tempStack.append(z)
                            else:
                                tempStack.append(y)
                                tempStack.append(x)
                                tempStack.append(':error:')
                        else:
                            tempStack.append(y)
                            tempStack.append(x)
                            tempStack.append(':error:')
                    else:
                        tempStack.append(':error:')
                elif item == 'neg':
                    finalized_values_list.remove(item)
                    if len(tempStack) >= 1:
                        x = tempStack.pop()
                        if type(x) == int:
                            z = x * -1
                            tempStack.append(z)
                        elif x in let_bindDict:
                            z = let_bindDict[x] *-1
                        else:
                            tempStack.append(x)
                            tempStack.append(':error:')
                    else:
                        tempStack.append(':error:')
                elif item == 'mul':
                    finalized_values_list.remove(item)
                    if len(tempStack) >= 2:
                        x = tempStack.pop()
                        y = tempStack.pop()
                        if type(x) == int and type(y) == int:
                            z = x * y
                            tempStack.append(z)
                        elif x in let_bindDict and y in let_bindDict:
                            if type(let_bindDict[x]) == int and type(let_bindDict[y]) == int:
                                z = let_bindDict[x] * let_bindDict[y]
                                tempStack.append(z)
                            else:
                                tempStack.append(y)
                                tempStack.append(x)
                                tempStack.append(':error:')
                        elif x in let_bindDict:
                            if type(let_bindDict[x]) == int and type(y) == int:
                                z = let_bindDict[x] * y
                                tempStack.append(z)
                            else:
                                tempStack.append(y)
                                tempStack.append(x)
                                tempStack.append(':error:')
                        elif y in let_bindDict:
                            if type(x) == int and type(let_bindDict[y]) == int:
                                z = x * let_bindDict[y]
                                tempStack.append(z)
                            else:
                                tempStack.append(y)
                                tempStack.append(x)
                                tempStack.append(':error:')
                        else:
                            tempStack.append(y)
                            tempStack.append(x)
                            tempStack.append(':error:')
                    else:
                        tempStack.append(':error:')
                elif item == 'div':
                    finalized_values_list.remove(item)
                    if len(tempStack) >= 2:
                        y = tempStack.pop()
                        x = tempStack.pop()
                        if type(x) == int and type(y) == int:
                            if y != 0:
                                z = x / y
                                tempStack.append(int(z))
                            else:
                                tempStack.append(x)
                                tempStack.append(y)
                                tempStack.append(':error:')
                        elif x in let_bindDict and y in let_bindDict:
                            if type(let_bindDict[x]) == int and type(let_bindDict[y]) == int:
                                if let_bindDict[y] != 0:
                                    z = let_bindDict[x] / let_bindDict[y]
                                    tempStack.append(int(z))
                                else:
                                    tempStack.append(x)
                                    tempStack.append(y)
                                    tempStack.append(':error:')
                            else:
                                tempStack.append(x)
                                tempStack.append(y)
                                tempStack.append(':error:')
                        elif x in let_bindDict:
                            if type(let_bindDict[x]) == int and type(y) == int:
                                if y != 0:
                                    z = let_bindDict[x] / y
                                    tempStack.append(int(z))
                                else:
                                    tempStack.append(x)
                                    tempStack.append(y)
                                    tempStack.append(':error:')
                            else:
                                tempStack.append(x)
                                tempStack.append(y)
                                tempStack.append(':error:')
                        elif y in let_bindDict:
                            if type(x) == int and type(let_bindDict[y]) == int:
                                if let_bindDict[y] != 0:
                                    z = x / let_bindDict[y]
                                    tempStack.append(int(z))
                                else:
                                    tempStack.append(x)
                                    tempStack.append(y)
                                    tempStack.append(':error:')
                            else:
                                tempStack.append(x)
                                tempStack.append(y)
                                tempStack.append(':error:')
                        else:
                            tempStack.append(x)
                            tempStack.append(y)
                            tempStack.append(':error:')
                    else:
                        tempStack.append(':error:')
                elif item == 'rem':
                    finalized_values_list.remove(item)
                    if len(tempStack) >= 2:
                        y = tempStack.pop()
                        x = tempStack.pop()
                        if type(x) == int and type(y) == int:
                            if y != 0:
                                z = x % y
                                tempStack.append(int(z))
                            else:
                                tempStack.append(x)
                                tempStack.append(y)
                                tempStack.append(':error:')
                        elif x in let_bindDict and y in let_bindDict:
                            if type(let_bindDict[x]) == int and type(let_bindDict[y]) == int:
                                if let_bindDict[y] != 0:
                                    z = let_bindDict[x] % let_bindDict[y]
                                    tempStack.append(int(z))
                                else:
                                    tempStack.append(x)
                                    tempStack.append(y)
                                    tempStack.append(':error:')
                            else:
                                tempStack.append(x)
                                tempStack.append(y)
                                tempStack.append(':error:')
                        elif x in let_bindDict:
                            if type(let_bindDict[x]) == int and type(y) == int:
                                if y != 0:
                                    z = let_bindDict[x] % y
                                    tempStack.append(int(z))
                                else:
                                    tempStack.append(x)
                                    tempStack.append(y)
                                    tempStack.append(':error:')
                            else:
                                tempStack.append(x)
                                tempStack.append(y)
                                tempStack.append(':error:')
                        elif y in let_bindDict:
                            if type(x) == int and type(let_bindDict[y]) == int:
                                if let_bindDict[y] != 0:
                                    z = x % let_bindDict[y]
                                    tempStack.append(int(z))
                                else:
                                    tempStack.append(x)
                                    tempStack.append(y)
                                    tempStack.append(':error:')
                            else:
                                tempStack.append(x)
                                tempStack.append(y)
                                tempStack.append(':error:')
                        else:
                            tempStack.append(x)
                            tempStack.append(y)
                            tempStack.append(':error:')
                    else:
                        tempStack.append(':error:')
                elif item == 'pop':
                    finalized_values_list.remove(item)
                    if len(tempStack) >= 1:
                        tempStack.pop()
                    else:
                        tempStack.append(':error:')
                elif item == 'swap':
                    finalized_values_list.remove(item)
                    if len(tempStack) >= 2:
                        x = tempStack.pop()
                        y = tempStack.pop()
                        tempStack.append(x)
                        tempStack.append(y)
                    else:
                        tempStack.append(':error:')
                elif item == 'and':
                    finalized_values_list.remove(item)
                    if len(tempStack) >= 2:
                        x = tempStack.pop()
                        y = tempStack.pop()
                        if x == ':true:' and y == ':true:':
                            tempStack.append(':true:')
                        elif x == ':true:' and y == ':false:':
                            tempStack.append(':false:')
                        elif x == ':false:' and y == ':true:':
                            tempStack.append(':false:')
                        elif x == ':false:' and y == ':false:':
                            tempStack.append(':false:')
                        elif x in let_bindDict and y in let_bindDict:
                            if let_bindDict[x] == ':true:' and let_bindDict[y] == ':true:':
                                tempStack.append(':true:')
                            elif let_bindDict[x] == ':true:' and let_bindDict[y] == ':false:':
                                tempStack.append(':false:')
                            elif let_bindDict[x] == ':false:' and let_bindDict[y] == ':true:':
                                tempStack.append(':false:')
                            elif let_bindDict[x] == ':false:' and let_bindDict[y] == ':false:':
                                tempStack.append(':false:')
                            else:
                                tempStack.append(y)
                                tempStack.append(x)
                                tempStack.append(':error:')
                        elif x in let_bindDict:
                            if let_bindDict[x] == ':true:' and y == ':true:':
                                tempStack.append(':true:')
                            elif let_bindDict[x] == ':true:' and y == ':false:':
                                tempStack.append(':false:')
                            elif let_bindDict[x] == ':false:' and y == ':true:':
                                tempStack.append(':false:')
                            elif let_bindDict[x] == ':false:' and y == ':false:':
                                tempStack.append(':false:')
                            else:
                                tempStack.append(y)
                                tempStack.append(x)
                                tempStack.append(':error:')
                        elif y in let_bindDict:
                            if x == ':true:' and let_bindDict[y] == ':true:':
                                tempStack.append(':true:')
                            elif x == ':true:' and let_bindDict[y] == ':false:':
                                tempStack.append(':false:')
                            elif x == ':false:' and let_bindDict[y] == ':true:':
                                tempStack.append(':false:')
                            elif x == ':false:' and let_bindDict[y] == ':false:':
                                tempStack.append(':false:')
                            else:
                                tempStack.append(y)
                                tempStack.append(x)
                                tempStack.append(':error:')
                        else:
                            tempStack.append(y)
                            tempStack.append(x)
                            tempStack.append(':error:')
                    else:
                        tempStack.append(':error:')
                elif item == 'or':
                    finalized_values_list.remove(item)
                    if len(tempStack) >= 2:
                        x = tempStack.pop()
                        y = tempStack.pop()
                        if x == ':true:' and y == ':true:':
                            tempStack.append(':true:')
                        elif x == ':true:' and y == ':false:':
                            tempStack.append(':true:')
                        elif x == ':false:' and y == ':true:':
                            tempStack.append(':true:')
                        elif x == ':false:' and y == ':false:':
                            tempStack.append(':false:')
                        elif x in let_bindDict and y in let_bindDict:
                            if let_bindDict[x] == ':true:' and let_bindDict[y] == ':true:':
                                tempStack.append(':true:')
                            elif let_bindDict[x] == ':true:' and let_bindDict[y] == ':false:':
                                tempStack.append(':true:')
                            elif let_bindDict[x] == ':false:' and let_bindDict[y] == ':true:':
                                tempStack.append(':true:')
                            elif let_bindDict[x] == ':false:' and let_bindDict[y] == ':false:':
                                tempStack.append(':false:')
                            else:
                                tempStack.append(y)
                                tempStack.append(x)
                                tempStack.append(':error:')
                        elif x in let_bindDict:
                            if let_bindDict[x] == ':true:' and y == ':true:':
                                tempStack.append(':true:')
                            elif let_bindDict[x] == ':true:' and y == ':false:':
                                tempStack.append(':true:')
                            elif let_bindDict[x] == ':false:' and y == ':true:':
                                tempStack.append(':true:')
                            elif let_bindDict[x] == ':false:' and y == ':false:':
                                tempStack.append(':false:')
                            else:
                                tempStack.append(y)
                                tempStack.append(x)
                                tempStack.append(':error:')
                        elif y in let_bindDict:
                            if x == ':true:' and let_bindDict[y] == ':true:':
                                tempStack.append(':true:')
                            elif x == ':true:' and let_bindDict[y] == ':false:':
                                tempStack.append(':true:')
                            elif x == ':false:' and let_bindDict[y] == ':true:':
                                tempStack.append(':true:')
                            elif x == ':false:' and let_bindDict[y] == ':false:':
                                tempStack.append(':false:')
                            else:
                                tempStack.append(y)
                                tempStack.append(x)
                                tempStack.append(':error:')
                        else:
                            tempStack.append(y)
                            tempStack.append(x)
                            tempStack.append(':error:')
                    else:
                        tempStack.append(':error:')
                elif item == 'not':
                    finalized_values_list.remove(item)
                    if len(tempStack) >= 1:
                        x = tempStack.pop()
                        if x == ':true:':
                            tempStack.append(':false:')
                        elif x == ':false:':
                            tempStack.append(':true:')
                        elif x in let_bindDict:
                            if let_bindDict[x] == ':true:':
                                tempStack.append(':false:')
                            elif let_bindDict[x] == ':false:':
                                tempStack.append(':true:')
                            else:
                                tempStack.append(x)
                                tempStack.append(':error:')
                        else:
                            tempStack.append(x)
                            tempStack.append(':error:')
                    else:
                        tempStack.append(':error:')
                elif item == 'equal':
                    finalized_values_list.remove(item)
                    if len(tempStack) >= 2:
                        y = tempStack.pop()
                        x = tempStack.pop()
                        if type(x) == int and type(y) == int:
                            if x == y:
                                tempStack.append(':true:')
                            else:
                                tempStack.append(':false:')
                        elif x in let_bindDict and y in let_bindDict:
                            if type(let_bindDict[x]) == int and type(let_bindDict[y]) == int:
                                if let_bindDict[x] == let_bindDict[y]:
                                    tempStack.append(':true:')
                                else:
                                    tempStack.append(':false:')
                            else:
                                tempStack.append(x)
                                tempStack.append(y)
                                tempStack.append(':error:')
                        elif x in let_bindDict:
                            if type(let_bindDict[x]) == int and type(y) == int:
                                if let_bindDict[x] == y:
                                    tempStack.append(':true:')
                                else:
                                    tempStack.append(':false:')
                            else:
                                tempStack.append(x)
                                tempStack.append(y)
                                tempStack.append(':error:')
                        elif y in let_bindDict:
                            if type(x) == int and type(let_bindDict[y]) == int:
                                if x == let_bindDict[y]:
                                    tempStack.append(':true:')
                                else:
                                    tempStack.append(':false:')
                            else:
                                tempStack.append(x)
                                tempStack.append(y)
                                tempStack.append(':error:')
                        else:
                            tempStack.append(x)
                            tempStack.append(y)
                            tempStack.append(':error:')
                    else:
                        tempStack.append(':error:')
                elif item == 'lessThan':
                    finalized_values_list.remove(item)
                    if len(tempStack) >= 2:
                        x = tempStack.pop()
                        y = tempStack.pop()
                        if type(x) == int and type(y) == int:
                            if x > y:
                                tempStack.append(':true:')
                            else:
                                tempStack.append(':false:')
                        elif x in let_bindDict and y in let_bindDict:
                            if type(let_bindDict[x]) == int and type(let_bindDict[y]) == int:
                                if let_bindDict[x] > let_bindDict[y]:
                                    tempStack.append(':true:')
                                else:
                                    tempStack.append(':false:')
                            else:
                                tempStack.append(x)
                                tempStack.append(y)
                                tempStack.append(':error:')
                        elif x in let_bindDict:
                            if type(let_bindDict[x]) == int and type(y) == int:
                                if let_bindDict[x] > y:
                                    tempStack.append(':true:')
                                else:
                                    tempStack.append(':false:')
                            else:
                                tempStack.append(x)
                                tempStack.append(y)
                                tempStack.append(':error:')
                        elif y in let_bindDict:
                            if type(x) == int and type(let_bindDict[y]) == int:
                                if x > let_bindDict[y]:
                                    tempStack.append(':true:')
                                else:
                                    tempStack.append(':false:')
                            else:
                                tempStack.append(x)
                                tempStack.append(y)
                                tempStack.append(':error:')
                        else:
                            tempStack.append(x)
                            tempStack.append(y)
                            tempStack.append(':error:')
                    else:
                        tempStack.append(':error:')
                elif item == 'bind':
                    finalized_values_list.remove(item)
                    if len(tempStack) >= 2:
                        x = tempStack.pop()
                        y = tempStack.pop()
                        if y != ':true:' and y != ':false:' and y != 'add' and y != 'sub' and y != 'mul' and y != 'div' and y != 'rem' and y != 'neg' and y != 'pop' and y != 'swap' and y != ':error:' and y != 'and' and y != 'or' and y != 'not' and y != 'equal' and y != 'lessThan' and y != 'bind' and y != 'if' and y != 'let' and y != 'end':
                            if x != 'add' and x != 'sub' and x != 'mul' and x != 'div' and x != 'rem' and x != 'neg' and x != 'pop' and x != 'swap' and x != ':error:' and x != 'and' and x != 'or' and x != 'not' and x != 'equal' and x != 'lessThan' and x != 'bind' and x != 'if' and x != 'let' and x != 'end':
                                if type(y) != int and '"' not in y:
                                    if x in let_bindDict:
                                        let_bound_items.append(y)
                                        let_bindDict[y] = let_bindDict[x]
                                        tempStack.append(':unit:')
                                        multipleLetBoundVar_dict[x].append(y)
                                    elif type(x) == str and '"' not in x and x != ':true:' and x != ':false:' and x != ':unit:':
                                        tempStack.append(y)
                                        tempStack.append(x)
                                        tempStack.append(':error:')
                                    else:
                                        let_bound_items.append(y)
                                        let_bindDict[y] = x
                                        tempStack.append(':unit:')
                                        if y in multipleLetBoundVar_dict:
                                            multipleLetBoundVar_dict[y].append(x)
                                            mlbv += 1
                                        if multipleLetBoundVarCount < 1:
                                            multipleLetBoundVar_dict[y] = []
                                            multipleLetBoundVar_dict[y].append(x)
                                            multipleLetBoundVarCount += 1
                                else:
                                    tempStack.append(y)
                                    tempStack.append(x)
                                    tempStack.append(':error:')
                            else:
                                tempStack.append(y)
                                tempStack.append(x)
                                tempStack.append(':error:')
                        else:
                            tempStack.append(y)
                            tempStack.append(x)
                            tempStack.append(':error:')
                    else:
                        tempStack.append(':error:')
                elif item == 'if':
                    finalized_values_list.remove(item)
                    if len(tempStack) >= 3:
                            x = tempStack.pop()
                            y = tempStack.pop()
                            z = tempStack.pop()
                            if z == ':true:' or z == ':false:':
                                if z == ':true:':
                                    tempStack.append(x)
                                elif z == ':false:':
                                    tempStack.append(y)
                                else:
                                    tempStack.append(z)
                                    tempStack.append(y)
                                    tempStack.append(x)
                                    tempStack.append(':error:')
                            elif z in let_bindDict:
                                if let_bindDict[z] == ':true:' or let_bindDict[z] == ':false:':
                                    if let_bindDict[z] == ':true:':
                                        tempStack.append(x)
                                    elif let_bindDict[z] == ':false:':
                                        tempStack.append(y)
                                    else:
                                        tempStack.append(z)
                                        tempStack.append(y)
                                        tempStack.append(x)
                                        tempStack.append(':error:')
                            else:
                                tempStack.append(':error:')
                    else:
                        tempStack.append(':error:')
                elif item == 'fun' or item == 'inOutFun':
                    finalized_values_list.remove(item)
                    if item == 'inOutFun':
                        is_inoutfun = True
                    tempStack.append(':unit:')
                    fun_stack = []
                    boundB4Fun.update(let_bindDict)
                    for item in finalized_values_list[input_list_count:]:
                        #print("function loop within let looking at: ", item)
                        if item == 'fun':
                            break
                        elif item == 'quit':
                            break
                        elif item != 'funEnd':
                            if item == 'return':
                                returnInFun = True
                                toDeleteCounter += 1
                                toDelete.append(item)
                                fun_stack.append(item)
                            else:
                                toDeleteCounter += 1
                                toDelete.append(item)
                                fun_stack.append(item)
                        else:
                            if returnInFun == True:
                                if 'call' in fun_stack:
                                    nestedFunCall = True
                                toDelete.append(item)
                                toDeleteCounter += 1
                                key = fun_stack[0]
                                arg = fun_stack[1]
                                del fun_stack[0]
                                del fun_stack[0]
                                fun_Dict[key] = [fun_stack, arg]
                                break
                            else:
                                if 'call' in fun_stack:
                                    nestedFunCall = True
                                toDelete.append(item)
                                fun_stack.append('return')
                                toDeleteCounter += 1
                                key = fun_stack[0]
                                arg = fun_stack[1]
                                del fun_stack[0]
                                del fun_stack[0]
                                fun_Dict[key] = [fun_stack, arg]
                                break
                elif item == 'call':
                    finalized_values_list.remove(item)
                    fun_bindDict.update(let_bindDict)
                    fun_bindDict.update(boundB4Fun)
                    if len(tempStack) >= 2:
                        key = tempStack.pop()
                        arg = tempStack.pop()
                        argToBindToFunOutput.append(arg)
                        if arg != ':error:':
                            if key in fun_Dict:
                                fun_stack2 = []
                                fun_stack_final = []
                                #print("found this function in the function dictionary")
                                #print('Key: ', key)
                                #print('Here is the list of instructions for this function: ', fun_Dict[key][0])
                                #print('This argument needs to to change all ', fun_Dict[key][1], ' to ', arg)
                                for item in fun_Dict[key][0]:
                                    #print('looking at instruction in the function dictionary: ', item)
                                    #print('Comparing to: ', fun_Dict[key][1])
                                    if item == fun_Dict[key][1]:
                                        fun_stack2.append(arg)
                                    else:
                                        fun_stack2.append(item)
                                del fun_Dict[key]
                                fun_Dict[key] = fun_stack2
                                for item in fun_Dict[key]:
                                    if type(item) == int:
                                        fun_stack_final.append(item)
                                    elif item != ':error:' and item != ':true:' and item != ':false:' and item != 'add' and item != 'neg' and item != 'mul' and item != 'sub' and item != 'div' and item != 'rem' and item != 'swap' and item != 'pop' and item != 'and' and item != 'or' and item != 'not' and item != 'equal' and item != 'lessThan' and item != 'bind' and item != 'if' and item != 'let' and item != 'end' and item != 'fun' and item != 'funEnd' and item != 'call' and item != 'return' and item != 'quit':
                                        fun_stack_final.append(item)
                                    elif item == ':error:':
                                        fun_stack_final.append(item)
                                    elif item == ':true:':
                                        fun_stack_final.append(item)
                                    elif item == ':false:':
                                        fun_stack_final.append(item)
                                    elif item == 'add':
                                        if len(fun_stack_final) >= 2:
                                            x = fun_stack_final.pop()
                                            y = fun_stack_final.pop()
                                            if type(x) == int and type(y) == int:
                                                z = x + y
                                                fun_stack_final.append(z)
                                            elif x in fun_bindDict and y in fun_bindDict:
                                                if type(fun_bindDict[x]) == int and type(fun_bindDict[y]) == int:
                                                    z = fun_bindDict[x] + fun_bindDict[y]
                                                    fun_stack_final.append(z)
                                                else:
                                                    fun_stack_final.append(y)
                                                    fun_stack_final.append(x)
                                                    fun_stack_final.append(':error:')
                                            elif x in fun_bindDict:
                                                if type(fun_bindDict[x]) == int and type(y) == int:
                                                    z = fun_bindDict[x] + y
                                                    fun_stack_final.append(z)
                                                else:
                                                    fun_stack_final.append(y)
                                                    fun_stack_final.append(x)
                                                    fun_stack_final.append(':error:')
                                            elif y in fun_bindDict:
                                                if type(x) == int and type(fun_bindDict[y]) == int:
                                                    z = x + fun_bindDict[y]
                                                    fun_stack_final.append(z)
                                                else:
                                                    fun_stack_final.append(y)
                                                    fun_stack_final.append(x)
                                                    fun_stack_final.append(':error:')
                                            else:
                                                fun_stack_final.append(y)
                                                fun_stack_final.append(x)
                                                fun_stack_final.append(':error:')
                                        else:
                                            fun_stack_final.append(':error:')
                                    elif item == 'sub':
                                        if len(fun_stack_final) >= 2:
                                            x = fun_stack_final.pop()
                                            y = fun_stack_final.pop()
                                            if type(x) == int and type(y) == int:
                                                z = y - x
                                                fun_stack_final.append(z)
                                            elif x in fun_bindDict and y in fun_bindDict:
                                                if type(fun_bindDict[x]) == int and type(fun_bindDict[y]) == int:
                                                    z = fun_bindDict[y] - fun_bindDict[x]
                                                    fun_stack_final.append(z)
                                                else:
                                                    fun_stack_final.append(y)
                                                    fun_stack_final.append(x)
                                                    fun_stack_final.append(':error:')
                                            elif x in fun_bindDict:
                                                if type(fun_bindDict[x]) == int and type(y) == int:
                                                    z =  y - fun_bindDict[x]
                                                    fun_stack_final.append(z)
                                                else:
                                                    fun_stack_final.append(y)
                                                    fun_stack_final.append(x)
                                                    fun_stack_final.append(':error:')
                                            elif y in fun_stack_final_bindDict:
                                                if type(x) == int and type(fun_bindDict[y]) == int:
                                                    z = fun_bindDict[y] - x
                                                    fun_stack_final.append(z)
                                                else:
                                                    fun_stack_final.append(y)
                                                    fun_stack_final.append(x)
                                                    fun_stack_final.append(':error:')
                                            else:
                                                fun_stack_final.append(y)
                                                fun_stack_final.append(x)
                                                fun_stack_final.append(':error:')
                                        else:
                                            fun_stack_final.append(':error:')
                                    elif item == 'neg':
                                        if len(fun_stack_final) >= 1:
                                            x = fun_stack_final.pop()
                                            if type(x) == int:
                                                z = x * -1
                                                fun_stack_final.append(z)
                                            elif x in fun_bindDict:
                                                z = fun_bindDict[x] *-1
                                            else:
                                                fun_stack_final.append(x)
                                                fun_stack_final.append(':error:')
                                        else:
                                            fun_stack_final.append(':error:')
                                    elif item == 'mul':
                                        if len(fun_stack_final) >= 2:
                                            x = fun_stack_final.pop()
                                            y = fun_stack_final.pop()
                                            if type(x) == int and type(y) == int:
                                                z = x * y
                                                fun_stack_final.append(z)
                                            elif x in fun_bindDict and y in fun_bindDict:
                                                if type(fun_bindDict[x]) == int and type(fun_bindDict[y]) == int:
                                                    z = fun_bindDict[x] * fun_bindDict[y]
                                                    fun_stack_final.append(z)
                                                else:
                                                    fun_stack_final.append(y)
                                                    fun_stack_final.append(x)
                                                    fun_stack_final.append(':error:')
                                            elif x in fun_bindDict:
                                                if type(fun_bindDict[x]) == int and type(y) == int:
                                                    z = fun_bindDict[x] * y
                                                    fun_stack_final.append(z)
                                                else:
                                                    fun_stack_final.append(y)
                                                    fun_stack_final.append(x)
                                                    fun_stack_final.append(':error:')
                                            elif y in fun_bindDict:
                                                if type(x) == int and type(fun_bindDict[y]) == int:
                                                    z = x * fun_bindDict[y]
                                                    fun_stack_final.append(z)
                                                else:
                                                    fun_stack_final.append(y)
                                                    fun_stack_final.append(x)
                                                    fun_stack_final.append(':error:')
                                            else:
                                                fun_stack_final.append(y)
                                                fun_stack_final.append(x)
                                                fun_stack_final.append(':error:')
                                        else:
                                            fun_stack_final.append(':error:')
                                    elif item == 'div':
                                        if len(fun_stack_final) >= 2:
                                            y = fun_stack_final.pop()
                                            x = fun_stack_final.pop()
                                            if type(x) == int and type(y) == int:
                                                if y != 0:
                                                    z = x / y
                                                    fun_stack_final.append(int(z))
                                                else:
                                                    fun_stack_final.append(x)
                                                    fun_stack_final.append(y)
                                                    fun_stack_final.append(':error:')
                                            elif x in fun_bindDict and y in fun_bindDict:
                                                if type(fun_bindDict[x]) == int and type(fun_bindDict[y]) == int:
                                                    if fun_bindDict[y] != 0:
                                                        z = fun_bindDict[x] / fun_bindDict[y]
                                                        fun_stack_final.append(int(z))
                                                    else:
                                                        fun_stack_final.append(x)
                                                        fun_stack_final.append(y)
                                                        fun_stack_final.append(':error:')
                                                else:
                                                    fun_stack_final.append(x)
                                                    fun_stack_final.append(y)
                                                    fun_stack_final.append(':error:')
                                            elif x in fun_bindDict:
                                                if type(fun_bindDict[x]) == int and type(y) == int:
                                                    if y != 0:
                                                        z = fun_bindDict[x] / y
                                                        fun_stack_final.append(int(z))
                                                    else:
                                                        fun_stack_final.append(x)
                                                        fun_stack_final.append(y)
                                                        fun_stack_final.append(':error:')
                                                else:
                                                    fun_stack_final.append(x)
                                                    fun_stack_final.append(y)
                                                    fun_stack_final.append(':error:')
                                            elif y in fun_bindDict:
                                                if type(x) == int and type(fun_bindDict[y]) == int:
                                                    if fun_bindDict[y] != 0:
                                                        z = x / fun_bindDict[y]
                                                        fun_stack_final.append(int(z))
                                                    else:
                                                        fun_stack_final.append(x)
                                                        fun_stack_final.append(y)
                                                        fun_stack_final.append(':error:')
                                                else:
                                                    fun_stack_final.append(x)
                                                    fun_stack_final.append(y)
                                                    fun_stack_final.append(':error:')
                                            else:
                                                fun_stack_final.append(x)
                                                fun_stack_final.append(y)
                                                fun_stack_final.append(':error:')
                                        else:
                                            fun_stack_final.append(':error:')
                                    elif item == 'rem':
                                        if len(fun_stack_final) >= 2:
                                            y = fun_stack_final.pop()
                                            x = fun_stack_final.pop()
                                            if type(x) == int and type(y) == int:
                                                if y != 0:
                                                    z = x % y
                                                    fun_stack_final.append(int(z))
                                                else:
                                                    fun_stack_final.append(x)
                                                    fun_stack_final.append(y)
                                                    fun_stack_final.append(':error:')
                                            elif x in fun_bindDict and y in fun_bindDict:
                                                if type(fun_bindDict[x]) == int and type(fun_bindDict[y]) == int:
                                                    if fun_bindDict[y] != 0:
                                                        z = fun_bindDict[x] % fun_bindDict[y]
                                                        fun_stack_final.append(int(z))
                                                    else:
                                                        fun_stack_final.append(x)
                                                        fun_stack_final.append(y)
                                                        fun_stack_final.append(':error:')
                                                else:
                                                    fun_stack_final.append(x)
                                                    fun_stack_final.append(y)
                                                    fun_stack_final.append(':error:')
                                            elif x in fun_bindDict:
                                                if type(fun_bindDict[x]) == int and type(y) == int:
                                                    if y != 0:
                                                        z = fun_bindDict[x] % y
                                                        fun_stack_final.append(int(z))
                                                    else:
                                                        fun_stack_final.append(x)
                                                        fun_stack_final.append(y)
                                                        fun_stack_final.append(':error:')
                                                else:
                                                    fun_stack_final.append(x)
                                                    fun_stack_final.append(y)
                                                    fun_stack_final.append(':error:')
                                            elif y in fun_bindDict:
                                                if type(x) == int and type(fun_bindDict[y]) == int:
                                                    if fun_bindDict[y] != 0:
                                                        z = x % fun_bindDict[y]
                                                        fun_stack_final.append(int(z))
                                                    else:
                                                        fun_stack_final.append(x)
                                                        fun_stack_final.append(y)
                                                        fun_stack_final.append(':error:')
                                                else:
                                                    fun_stack_final.append(x)
                                                    fun_stack_final.append(y)
                                                    fun_stack_final.append(':error:')
                                            else:
                                                fun_stack_final.append(x)
                                                fun_stack_final.append(y)
                                                fun_stack_final.append(':error:')
                                        else:
                                            fun_stack_final.append(':error:')
                                    elif item == 'pop':
                                        if len(fun_stack_final) >= 1:
                                            fun_stack_final.pop()
                                        else:
                                            fun_stack_final.append(':error:')
                                    elif item == 'swap':
                                        if len(fun_stack_final) >= 2:
                                            x = fun_stack_final.pop()
                                            y = fun_stack_final.pop()
                                            fun_stack_final.append(x)
                                            fun_stack_final.append(y)
                                        else:
                                            fun_stack_final.append(':error:')
                                    elif item == 'and':
                                        if len(fun_stack_final) >= 2:
                                            x = fun_stack_final.pop()
                                            y = fun_stack_final.pop()
                                            if x == ':true:' and y == ':true:':
                                                fun_stack_final.append(':true:')
                                            elif x == ':true:' and y == ':false:':
                                                fun_stack_final.append(':false:')
                                            elif x == ':false:' and y == ':true:':
                                                fun_stack_final.append(':false:')
                                            elif x == ':false:' and y == ':false:':
                                                fun_stack_final.append(':false:')
                                            elif x in fun_bindDict and y in fun_bindDict:
                                                if fun_bindDict[x] == ':true:' and fun_bindDict[y] == ':true:':
                                                    fun_stack_final.append(':true:')
                                                elif fun_bindDict[x] == ':true:' and fun_bindDict[y] == ':false:':
                                                    fun_stack_final.append(':false:')
                                                elif fun_bindDict[x] == ':false:' and fun_bindDict[y] == ':true:':
                                                    fun_stack_final.append(':false:')
                                                elif fun_bindDict[x] == ':false:' and fun_bindDict[y] == ':false:':
                                                    fun_stack_final.append(':false:')
                                                else:
                                                    fun_stack_final.append(y)
                                                    fun_stack_final.append(x)
                                                    fun_stack_final.append(':error:')
                                            elif x in fun_bindDict:
                                                if fun_bindDict[x] == ':true:' and y == ':true:':
                                                    fun_stack_final.append(':true:')
                                                elif fun_bindDict[x] == ':true:' and y == ':false:':
                                                    fun_stack_final.append(':false:')
                                                elif fun_bindDict[x] == ':false:' and y == ':true:':
                                                    fun_stack_final.append(':false:')
                                                elif fun_bindDict[x] == ':false:' and y == ':false:':
                                                    fun_stack_final.append(':false:')
                                                else:
                                                    fun_stack_final.append(y)
                                                    fun_stack_final.append(x)
                                                    fun_stack_final.append(':error:')
                                            elif y in fun_bindDict:
                                                if x == ':true:' and fun_bindDict[y] == ':true:':
                                                    fun_stack_final.append(':true:')
                                                elif x == ':true:' and fun_bindDict[y] == ':false:':
                                                    fun_stack_final.append(':false:')
                                                elif x == ':false:' and fun_bindDict[y] == ':true:':
                                                    fun_stack_final.append(':false:')
                                                elif x == ':false:' and fun_bindDict[y] == ':false:':
                                                    fun_stack_final.append(':false:')
                                                else:
                                                    fun_stack_final.append(y)
                                                    fun_stack_final.append(x)
                                                    fun_stack_final.append(':error:')
                                            else:
                                                fun_stack_final.append(y)
                                                fun_stack_final.append(x)
                                                fun_stack_final.append(':error:')
                                        else:
                                            fun_stack_final.append(':error:')
                                    elif item == 'or':
                                        if len(fun_stack_final) >= 2:
                                            x = fun_stack_final.pop()
                                            y = fun_stack_final.pop()
                                            if x == ':true:' and y == ':true:':
                                                fun_stack_final.append(':true:')
                                            elif x == ':true:' and y == ':false:':
                                                fun_stack_final.append(':true:')
                                            elif x == ':false:' and y == ':true:':
                                                fun_stack_final.append(':true:')
                                            elif x == ':false:' and y == ':false:':
                                                fun_stack_final.append(':false:')
                                            elif x in fun_bindDict and y in fun_bindDict:
                                                if fun_bindDict[x] == ':true:' and fun_bindDict[y] == ':true:':
                                                    fun_stack_final.append(':true:')
                                                elif fun_bindDict[x] == ':true:' and fun_bindDict[y] == ':false:':
                                                    fun_stack_final.append(':true:')
                                                elif fun_bindDict[x] == ':false:' and fun_bindDict[y] == ':true:':
                                                    fun_stack_final.append(':true:')
                                                elif fun_bindDict[x] == ':false:' and fun_bindDict[y] == ':false:':
                                                    fun_stack_final.append(':false:')
                                                else:
                                                    fun_stack_final.append(y)
                                                    fun_stack_final.append(x)
                                                    fun_stack_final.append(':error:')
                                            elif x in fun_bindDict:
                                                if fun_bindDict[x] == ':true:' and y == ':true:':
                                                    fun_stack_final.append(':true:')
                                                elif fun_bindDict[x] == ':true:' and y == ':false:':
                                                    fun_stack_final.append(':true:')
                                                elif fun_bindDict[x] == ':false:' and y == ':true:':
                                                    fun_stack_final.append(':true:')
                                                elif fun_bindDict[x] == ':false:' and y == ':false:':
                                                    fun_stack_final.append(':false:')
                                                else:
                                                    fun_stack_final.append(y)
                                                    fun_stack_final.append(x)
                                                    fun_stack_final.append(':error:')
                                            elif y in fun_bindDict:
                                                if x == ':true:' and fun_bindDict[y] == ':true:':
                                                    fun_stack_final.append(':true:')
                                                elif x == ':true:' and fun_bindDict[y] == ':false:':
                                                    fun_stack_final.append(':true:')
                                                elif x == ':false:' and fun_bindDict[y] == ':true:':
                                                    fun_stack_final.append(':true:')
                                                elif x == ':false:' and fun_bindDict[y] == ':false:':
                                                    fun_stack_final.append(':false:')
                                                else:
                                                    fun_stack_final.append(y)
                                                    fun_stack_final.append(x)
                                                    fun_stack_final.append(':error:')
                                            else:
                                                fun_stack_final.append(y)
                                                fun_stack_final.append(x)
                                                fun_stack_final.append(':error:')
                                        else:
                                            fun_stack_final.append(':error:')
                                    elif item == 'not':
                                        if len(fun_stack_final) >= 1:
                                            x = fun_stack_final.pop()
                                            if x == ':true:':
                                                fun_stack_final.append(':false:')
                                            elif x == ':false:':
                                                fun_stack_final.append(':true:')
                                            elif x in fun_bindDict:
                                                if fun_bindDict[x] == ':true:':
                                                    fun_stack_final.append(':false:')
                                                elif fun_bindDict[x] == ':false:':
                                                    fun_stack_final.append(':true:')
                                                else:
                                                    fun_stack_final.append(x)
                                                    fun_stack_final.append(':error:')
                                            else:
                                                fun_stack_final.append(x)
                                                fun_stack_final.append(':error:')
                                        else:
                                            fun_stack_final.append(':error:')
                                    elif item == 'equal':
                                        if len(fun_stack_final) >= 2:
                                            y = fun_stack_final.pop()
                                            x = fun_stack_final.pop()
                                            if type(x) == int and type(y) == int:
                                                if x == y:
                                                    fun_stack_final.append(':true:')
                                                else:
                                                    fun_stack_final.append(':false:')
                                            elif x in fun_bindDict and y in fun_bindDict:
                                                if type(fun_bindDict[x]) == int and type(fun_bindDict[y]) == int:
                                                    if fun_bindDict[x] == fun_bindDict[y]:
                                                        fun_stack_final.append(':true:')
                                                    else:
                                                        fun_stack_final.append(':false:')
                                                else:
                                                    fun_stack_final.append(x)
                                                    fun_stack_final.append(y)
                                                    fun_stack_final.append(':error:')
                                            elif x in fun_bindDict:
                                                if type(fun_bindDict[x]) == int and type(y) == int:
                                                    if fun_bindDict[x] == y:
                                                        fun_stack_final.append(':true:')
                                                    else:
                                                        fun_stack_final.append(':false:')
                                                else:
                                                    fun_stack_final.append(x)
                                                    fun_stack_final.append(y)
                                                    fun_stack_final.append(':error:')
                                            elif y in fun_bindDict:
                                                if type(x) == int and type(fun_bindDict[y]) == int:
                                                    if x == fun_bindDict[y]:
                                                        fun_stack_final.append(':true:')
                                                    else:
                                                        fun_stack_final.append(':false:')
                                                else:
                                                    fun_stack_final.append(x)
                                                    fun_stack_final.append(y)
                                                    fun_stack_final.append(':error:')
                                            else:
                                                fun_stack_final.append(x)
                                                fun_stack_final.append(y)
                                                fun_stack_final.append(':error:')
                                        else:
                                            fun_stack_final.append(':error:')
                                    elif item == 'lessThan':
                                        if len(fun_stack_final) >= 2:
                                            x = fun_stack_final.pop()
                                            y = fun_stack_final.pop()
                                            if type(x) == int and type(y) == int:
                                                if x > y:
                                                    fun_stack_final.append(':true:')
                                                else:
                                                    fun_stack_final.append(':false:')
                                            elif x in fun_bindDict and y in fun_bindDict:
                                                if type(fun_bindDict[x]) == int and type(fun_bindDict[y]) == int:
                                                    if fun_bindDict[x] > fun_bindDict[y]:
                                                        fun_stack_final.append(':true:')
                                                    else:
                                                        fun_stack_final.append(':false:')
                                                else:
                                                    fun_stack_final.append(x)
                                                    fun_stack_final.append(y)
                                                    fun_stack_final.append(':error:')
                                            elif x in fun_bindDict:
                                                if type(fun_bindDict[x]) == int and type(y) == int:
                                                    if fun_bindDict[x] > y:
                                                        fun_stack_final.append(':true:')
                                                    else:
                                                        fun_stack_final.append(':false:')
                                                else:
                                                    fun_stack_final.append(x)
                                                    fun_stack_final.append(y)
                                                    fun_stack_final.append(':error:')
                                            elif y in fun_bindDict:
                                                if type(x) == int and type(fun_bindDict[y]) == int:
                                                    if x > fun_bindDict[y]:
                                                        fun_stack_final.append(':true:')
                                                    else:
                                                        fun_stack_final.append(':false:')
                                                else:
                                                    fun_stack_final.append(x)
                                                    fun_stack_final.append(y)
                                                    fun_stack_final.append(':error:')
                                            else:
                                                fun_stack_final.append(x)
                                                fun_stack_final.append(y)
                                                fun_stack_final.append(':error:')
                                        else:
                                            fun_stack_final.append(':error:')
                                    elif item == 'bind':
                                        if len(fun_stack_final) >= 2:
                                            x = fun_stack_final.pop()
                                            y = fun_stack_final.pop()
                                            if y != ':true:' and y != ':false:' and y != 'add' and y != 'sub' and y != 'mul' and y != 'div' and y != 'rem' and y != 'neg' and y != 'pop' and y != 'swap' and y != ':error:' and y != 'and' and y != 'or' and y != 'not' and y != 'equal' and y != 'lessThan' and y != 'bind' and y != 'if' and y != 'let' and y != 'end':
                                                if x != 'add' and x != 'sub' and x != 'mul' and x != 'div' and x != 'rem' and x != 'neg' and x != 'pop' and x != 'swap' and x != ':error:' and x != 'and' and x != 'or' and x != 'not' and x != 'equal' and x != 'lessThan' and x != 'bind' and x != 'if' and x != 'let' and x != 'end':
                                                    if type(y) != int and '"' not in y:
                                                        if x in fun_bindDict:
                                                            fun_bindDict[y] = fun_bindDict[x]
                                                            fun_stack_final.append(':unit:')
                                                        elif type(x) == str and '"' not in x and x != ':true:' and x != ':false:' and x != ':unit:':
                                                            fun_stack_final.append(y)
                                                            fun_stack_final.append(x)
                                                            fun_stack_final.append(':error:')
                                                        else:
                                                            fun_bindDict[y] = x
                                                            fun_stack_final.append(':unit:')
                                                    else:
                                                        fun_stack_final.append(y)
                                                        fun_stack_final.append(x)
                                                        fun_stack_final.append(':error:')
                                                else:
                                                    fun_stack_final.append(y)
                                                    fun_stack_final.append(x)
                                                    fun_stack_final.append(':error:')
                                            else:
                                                fun_stack_final.append(y)
                                                fun_stack_final.append(x)
                                                fun_stack_final.append(':error:')
                                        else:
                                            fun_stack_final.append(':error:')
                                    elif item == 'if':
                                        if len(fun_stack_final) >= 3:
                                                x = fun_stack_final.pop()
                                                y = fun_stack_final.pop()
                                                z = fun_stack_final.pop()
                                                if z == ':true:' or z == ':false:':
                                                    if z == ':true:':
                                                        fun_stack_final.append(x)
                                                    elif z == ':false:':
                                                        fun_stack_final.append(y)
                                                    else:
                                                        fun_stack_final.append(z)
                                                        fun_stack_final.append(y)
                                                        fun_stack_final.append(x)
                                                        fun_stack_final.append(':error:')
                                                elif z in fun_bindDict:
                                                    if fun_bindDict[z] == ':true:' or fun_bindDict[z] == ':false:':
                                                        if fun_bindDict[z] == ':true:':
                                                            fun_stack_final.append(x)
                                                        elif fun_bindDict[z] == ':false:':
                                                            fun_stack_final.append(y)
                                                        else:
                                                            fun_stack_final.append(z)
                                                            fun_stack_final.append(y)
                                                            fun_stack_final.append(x)
                                                            fun_stack_final.append(':error:')
                                                else:
                                                    fun_stack_final.append(':error:')
                                        else:
                                            fun_stack_final.append(':error:')
                                    elif item == 'return':
                                        if len(fun_stack_final) >= 1:
                                            if is_inoutfun == True:
                                                x = argToBindToFunOutput[0]
                                                #print("x: ", x)
                                                y = fun_bindDict[y]
                                                #print("y: ", y)
                                                let_bindDict[x] = y
                                            else:
                                                tempStack.append(fun_stack_final[len(fun_stack_final) - 1])
                                        else:
                                            tempStack.append(':error:')
                            else:
                                tempStack.append(arg)
                                tempStack.append(key)
                                tempStack.append(':error:')
                        else:
                            tempStack.append(arg)
                            tempStack.append(key)
                            tempStack.append(':error:')
                    else:
                        tempStack.append(':error:')
                elif item == 'end':
                    finalized_values_list.remove(item)
                    #print('This is the finalized_values_list: ', finalized_values_list)
                    if stack_count == let_count:
                        #print('In conditionial 1 for end')
                        if let_count > 1:
                            elementTransfer = tempStack[len(tempStack) - 1]
                            tempStack = stack[let_count - 2]
                            tempStack.append(elementTransfer)
                            del stack[let_count - 1]
                            let_count -= 1
                            stack_count -= 1
                            if not multipleLetBoundVar_dict:
                                continue
                            else:
                                multipleLetBoundVarDictIsEmpty = False
                            if multipleLetBoundVarDictIsEmpty == False:
                                #print("multipleLetBoundVar_dict[x][mlbv] = ", multipleLetBoundVar_dict[x][mlbv])
                                let_bindDict[x] = multipleLetBoundVar_dict[x][mlbv]
                                mlbv -= 2
                        elif let_count == 1:
                            elementTransfer = tempStack[len(tempStack) - 1]
                            stack.append(elementTransfer)
                            del stack[let_count - 1]
                            let_count -= 1
                            for item in let_bound_items:
                                if item in let_bindDict:
                                    del let_bindDict[item]
                            fun_Dict = {}
                            break
                    elif stack_count_b4_let > 1:
                        #print('In conditionial 2 for end')
                        if let_count > 1:
                            elementTransfer = tempStack[len(tempStack) - 1]
                            tempStack = stack[let_count]
                            tempStack.append(elementTransfer)
                            del stack[let_count + 1]
                            let_count -= 1
                            stack_count -= 1
                            #print("multipleLetBoundVar_dict[x][mlbv]", multipleLetBoundVar_dict[x][mlbv])
                            mlbv -= 1
                        elif let_count == 1:
                            elementTransfer = tempStack[len(tempStack) - 1]
                            stack.append(elementTransfer)
                            del stack[let_count + 1]
                            let_count -= 1
                            for item in let_bound_items:
                                if item in let_bindDict:
                                    del let_bindDict[item]
                            fun_Dict = {}
                            break
                    else:
                        #print('In conditionial 3 for end')
                        if let_count > 1:
                            elementTransfer = tempStack[len(tempStack) - 1]
                            tempStack = stack[let_count - 1]
                            tempStack.append(elementTransfer)
                            del stack[let_count]
                            let_count -= 1
                            stack_count -= 1
                        elif let_count == 1:
                            elementTransfer = tempStack[len(tempStack) - 1]
                            stack.append(elementTransfer)
                            del stack[let_count]
                            let_count -= 1
                            for item in let_bound_items:
                                if item in let_bindDict:
                                    del let_bindDict[item]
                            fun_Dict = {}
                            break
                elif item == 'let':
                    break
        elif item == 'fun' or item == 'inOutFun':
            if item == 'inOutFun':
                is_inoutfun = True
            stack.append(':unit:')
            stack_count += 1
            fun_stack = []
            boundB4Fun.update(bindDict)
            print("these items were bound before fun came up: ", boundB4Fun)
            for item in finalized_values_list[input_list_count:]:
                #print("function loop looking at: ", item)
                if item != 'funEnd':
                    if item == 'return':
                        returnInFun = True
                        #print("appending item to fun_stack: ", item)
                        fun_stack.append(item)
                        finalized_values_list.remove(item)
                    else:
                        fun_stack.append(item)
                        finalized_values_list.remove(item)
                elif item == 'fun':
                    break
                else:
                    if returnInFun == True:
                        if 'call' in fun_stack:
                            nestedFunCall = True
                        finalized_values_list.remove(item)
                        key = fun_stack[0]
                        arg = fun_stack[1]
                        del fun_stack[0]
                        del fun_stack[0]
                        fun_Dict[key] = [fun_stack, arg]
                        nestedFunCall_dict.update(fun_Dict)
                        break
                    else:
                        if 'call' in fun_stack:
                            nestedFunCall = True
                        finalized_values_list.remove(item)
                        fun_stack.append('return')
                        key = fun_stack[0]
                        arg = fun_stack[1]
                        del fun_stack[0]
                        del fun_stack[0]
                        fun_Dict[key] = [fun_stack, arg]
                        nestedFunCall_dict.update(fun_Dict)
                        break
        elif item == 'call':
            fun_bindDict.update(bindDict)
            fun_bindDict.update(boundB4Fun)
            if stack_count >= 2:
                key = stack.pop()
                arg = stack.pop()
                #print("key: ", key)
                #print("arg: ", arg)
                stack_count -= 2
                argToBindToFunOutput.append(arg)
                if arg != ':error:':
                    if key in fun_Dict:
                        fun_stack2 = []
                        fun_stack_final = []
                        #print("found this function in the function dictionary")
                        #print('Key: ', key)
                        #print('Here is the list of instructions for this function: ', fun_Dict[key][0])
                        #print('This argument needs to to change all ', fun_Dict[key][1], ' to ', arg)
                        for item in fun_Dict[key][0]:
                            #print('looking at instruction in the function dictionary: ', item)
                            #print('Comparing to: ', fun_Dict[key][1])
                            if item == fun_Dict[key][1]:
                                if fun_Dict[key][1] in fun_bindDict:
                                    fun_stack2.append(fun_bindDict[fun_Dict[key][1]])
                                else:
                                    fun_stack2.append(arg)
                            else:
                                fun_stack2.append(item)
                        del fun_Dict[key]
                        fun_Dict[key] = fun_stack2
                        for item in fun_Dict[key]:
                            if type(item) == int:
                                fun_stack_final.append(item)
                            elif item != ':error:' and item != ':true:' and item != ':false:' and item != 'add' and item != 'neg' and item != 'mul' and item != 'sub' and item != 'div' and item != 'rem' and item != 'swap' and item != 'pop' and item != 'and' and item != 'or' and item != 'not' and item != 'equal' and item != 'lessThan' and item != 'bind' and item != 'if' and item != 'let' and item != 'end' and item != 'fun' and item != 'funEnd' and item != 'call' and item != 'return' and item != 'quit':
                                fun_stack_final.append(item)
                            elif item == ':error:':
                                fun_stack_final.append(item)
                            elif item == ':true:':
                                fun_stack_final.append(item)
                            elif item == ':false:':
                                fun_stack_final.append(item)
                            elif item == 'add':
                                if len(fun_stack_final) >= 2:
                                    x = fun_stack_final.pop()
                                    y = fun_stack_final.pop()
                                    if type(x) == int and type(y) == int:
                                        z = x + y
                                        fun_stack_final.append(z)
                                    elif x in fun_bindDict and y in fun_bindDict:
                                        if type(fun_bindDict[x]) == int and type(fun_bindDict[y]) == int:
                                            z = fun_bindDict[x] + fun_bindDict[y]
                                            fun_stack_final.append(z)
                                        else:
                                            fun_stack_final.append(y)
                                            fun_stack_final.append(x)
                                            fun_stack_final.append(':error:')
                                    elif x in fun_bindDict:
                                        if type(fun_bindDict[x]) == int and type(y) == int:
                                            z = fun_bindDict[x] + y
                                            fun_stack_final.append(z)
                                        else:
                                            fun_stack_final.append(y)
                                            fun_stack_final.append(x)
                                            fun_stack_final.append(':error:')
                                    elif y in fun_bindDict:
                                        if type(x) == int and type(fun_bindDict[y]) == int:
                                            z = x + fun_bindDict[y]
                                            fun_stack_final.append(z)
                                        else:
                                            fun_stack_final.append(y)
                                            fun_stack_final.append(x)
                                            fun_stack_final.append(':error:')
                                    else:
                                        fun_stack_final.append(y)
                                        fun_stack_final.append(x)
                                        fun_stack_final.append(':error:')
                                else:
                                    fun_stack_final.append(':error:')
                            elif item == 'sub':
                                if len(fun_stack_final) >= 2:
                                    x = fun_stack_final.pop()
                                    y = fun_stack_final.pop()
                                    if type(x) == int and type(y) == int:
                                        z = y - x
                                        fun_stack_final.append(z)
                                    elif x in fun_bindDict and y in fun_bindDict:
                                        if type(fun_bindDict[x]) == int and type(fun_bindDict[y]) == int:
                                            z = fun_bindDict[y] - fun_bindDict[x]
                                            fun_stack_final.append(z)
                                        else:
                                            fun_stack_final.append(y)
                                            fun_stack_final.append(x)
                                            fun_stack_final.append(':error:')
                                    elif x in fun_bindDict:
                                        if type(fun_bindDict[x]) == int and type(y) == int:
                                            z =  y - fun_bindDict[x]
                                            fun_stack_final.append(z)
                                        else:
                                            fun_stack_final.append(y)
                                            fun_stack_final.append(x)
                                            fun_stack_final.append(':error:')
                                    elif y in fun_stack_final_bindDict:
                                        if type(x) == int and type(fun_bindDict[y]) == int:
                                            z = fun_bindDict[y] - x
                                            fun_stack_final.append(z)
                                        else:
                                            fun_stack_final.append(y)
                                            fun_stack_final.append(x)
                                            fun_stack_final.append(':error:')
                                    else:
                                        fun_stack_final.append(y)
                                        fun_stack_final.append(x)
                                        fun_stack_final.append(':error:')
                                else:
                                    fun_stack_final.append(':error:')
                            elif item == 'neg':
                                if len(fun_stack_final) >= 1:
                                    x = fun_stack_final.pop()
                                    if type(x) == int:
                                        z = x * -1
                                        fun_stack_final.append(z)
                                    elif x in fun_bindDict:
                                        z = fun_bindDict[x] *-1
                                    else:
                                        fun_stack_final.append(x)
                                        fun_stack_final.append(':error:')
                                else:
                                    fun_stack_final.append(':error:')
                            elif item == 'mul':
                                if len(fun_stack_final) >= 2:
                                    x = fun_stack_final.pop()
                                    y = fun_stack_final.pop()
                                    if type(x) == int and type(y) == int:
                                        z = x * y
                                        fun_stack_final.append(z)
                                    elif x in fun_bindDict and y in fun_bindDict:
                                        if type(fun_bindDict[x]) == int and type(fun_bindDict[y]) == int:
                                            z = fun_bindDict[x] * fun_bindDict[y]
                                            fun_stack_final.append(z)
                                        else:
                                            fun_stack_final.append(y)
                                            fun_stack_final.append(x)
                                            fun_stack_final.append(':error:')
                                    elif x in fun_bindDict:
                                        if type(fun_bindDict[x]) == int and type(y) == int:
                                            z = fun_bindDict[x] * y
                                            fun_stack_final.append(z)
                                        else:
                                            fun_stack_final.append(y)
                                            fun_stack_final.append(x)
                                            fun_stack_final.append(':error:')
                                    elif y in fun_bindDict:
                                        if type(x) == int and type(fun_bindDict[y]) == int:
                                            z = x * fun_bindDict[y]
                                            fun_stack_final.append(z)
                                        else:
                                            fun_stack_final.append(y)
                                            fun_stack_final.append(x)
                                            fun_stack_final.append(':error:')
                                    else:
                                        fun_stack_final.append(y)
                                        fun_stack_final.append(x)
                                        fun_stack_final.append(':error:')
                                else:
                                    fun_stack_final.append(':error:')
                            elif item == 'div':
                                if len(fun_stack_final) >= 2:
                                    y = fun_stack_final.pop()
                                    x = fun_stack_final.pop()
                                    if type(x) == int and type(y) == int:
                                        if y != 0:
                                            z = x / y
                                            fun_stack_final.append(int(z))
                                        else:
                                            fun_stack_final.append(x)
                                            fun_stack_final.append(y)
                                            fun_stack_final.append(':error:')
                                    elif x in fun_bindDict and y in fun_bindDict:
                                        if type(fun_bindDict[x]) == int and type(fun_bindDict[y]) == int:
                                            if fun_bindDict[y] != 0:
                                                z = fun_bindDict[x] / fun_bindDict[y]
                                                fun_stack_final.append(int(z))
                                            else:
                                                fun_stack_final.append(x)
                                                fun_stack_final.append(y)
                                                fun_stack_final.append(':error:')
                                        else:
                                            fun_stack_final.append(x)
                                            fun_stack_final.append(y)
                                            fun_stack_final.append(':error:')
                                    elif x in fun_bindDict:
                                        if type(fun_bindDict[x]) == int and type(y) == int:
                                            if y != 0:
                                                z = fun_bindDict[x] / y
                                                fun_stack_final.append(int(z))
                                            else:
                                                fun_stack_final.append(x)
                                                fun_stack_final.append(y)
                                                fun_stack_final.append(':error:')
                                        else:
                                            fun_stack_final.append(x)
                                            fun_stack_final.append(y)
                                            fun_stack_final.append(':error:')
                                    elif y in fun_bindDict:
                                        if type(x) == int and type(fun_bindDict[y]) == int:
                                            if fun_bindDict[y] != 0:
                                                z = x / fun_bindDict[y]
                                                fun_stack_final.append(int(z))
                                            else:
                                                fun_stack_final.append(x)
                                                fun_stack_final.append(y)
                                                fun_stack_final.append(':error:')
                                        else:
                                            fun_stack_final.append(x)
                                            fun_stack_final.append(y)
                                            fun_stack_final.append(':error:')
                                    else:
                                        fun_stack_final.append(x)
                                        fun_stack_final.append(y)
                                        fun_stack_final.append(':error:')
                                else:
                                    fun_stack_final.append(':error:')
                            elif item == 'rem':
                                if len(fun_stack_final) >= 2:
                                    y = fun_stack_final.pop()
                                    x = fun_stack_final.pop()
                                    if type(x) == int and type(y) == int:
                                        if y != 0:
                                            z = x % y
                                            fun_stack_final.append(int(z))
                                        else:
                                            fun_stack_final.append(x)
                                            fun_stack_final.append(y)
                                            fun_stack_final.append(':error:')
                                    elif x in fun_bindDict and y in fun_bindDict:
                                        if type(fun_bindDict[x]) == int and type(fun_bindDict[y]) == int:
                                            if fun_bindDict[y] != 0:
                                                z = fun_bindDict[x] % fun_bindDict[y]
                                                fun_stack_final.append(int(z))
                                            else:
                                                fun_stack_final.append(x)
                                                fun_stack_final.append(y)
                                                fun_stack_final.append(':error:')
                                        else:
                                            fun_stack_final.append(x)
                                            fun_stack_final.append(y)
                                            fun_stack_final.append(':error:')
                                    elif x in fun_bindDict:
                                        if type(fun_bindDict[x]) == int and type(y) == int:
                                            if y != 0:
                                                z = fun_bindDict[x] % y
                                                fun_stack_final.append(int(z))
                                            else:
                                                fun_stack_final.append(x)
                                                fun_stack_final.append(y)
                                                fun_stack_final.append(':error:')
                                        else:
                                            fun_stack_final.append(x)
                                            fun_stack_final.append(y)
                                            fun_stack_final.append(':error:')
                                    elif y in fun_bindDict:
                                        if type(x) == int and type(fun_bindDict[y]) == int:
                                            if fun_bindDict[y] != 0:
                                                z = x % fun_bindDict[y]
                                                fun_stack_final.append(int(z))
                                            else:
                                                fun_stack_final.append(x)
                                                fun_stack_final.append(y)
                                                fun_stack_final.append(':error:')
                                        else:
                                            fun_stack_final.append(x)
                                            fun_stack_final.append(y)
                                            fun_stack_final.append(':error:')
                                    else:
                                        fun_stack_final.append(x)
                                        fun_stack_final.append(y)
                                        fun_stack_final.append(':error:')
                                else:
                                    fun_stack_final.append(':error:')
                            elif item == 'pop':
                                if len(fun_stack_final) >= 1:
                                    fun_stack_final.pop()
                                else:
                                    fun_stack_final.append(':error:')
                            elif item == 'swap':
                                if len(fun_stack_final) >= 2:
                                    x = fun_stack_final.pop()
                                    y = fun_stack_final.pop()
                                    fun_stack_final.append(x)
                                    fun_stack_final.append(y)
                                else:
                                    fun_stack_final.append(':error:')
                            elif item == 'and':
                                if len(fun_stack_final) >= 2:
                                    x = fun_stack_final.pop()
                                    y = fun_stack_final.pop()
                                    if x == ':true:' and y == ':true:':
                                        fun_stack_final.append(':true:')
                                    elif x == ':true:' and y == ':false:':
                                        fun_stack_final.append(':false:')
                                    elif x == ':false:' and y == ':true:':
                                        fun_stack_final.append(':false:')
                                    elif x == ':false:' and y == ':false:':
                                        fun_stack_final.append(':false:')
                                    elif x in fun_bindDict and y in fun_bindDict:
                                        if fun_bindDict[x] == ':true:' and fun_bindDict[y] == ':true:':
                                            fun_stack_final.append(':true:')
                                        elif fun_bindDict[x] == ':true:' and fun_bindDict[y] == ':false:':
                                            fun_stack_final.append(':false:')
                                        elif fun_bindDict[x] == ':false:' and fun_bindDict[y] == ':true:':
                                            fun_stack_final.append(':false:')
                                        elif fun_bindDict[x] == ':false:' and fun_bindDict[y] == ':false:':
                                            fun_stack_final.append(':false:')
                                        else:
                                            fun_stack_final.append(y)
                                            fun_stack_final.append(x)
                                            fun_stack_final.append(':error:')
                                    elif x in fun_bindDict:
                                        if fun_bindDict[x] == ':true:' and y == ':true:':
                                            fun_stack_final.append(':true:')
                                        elif fun_bindDict[x] == ':true:' and y == ':false:':
                                            fun_stack_final.append(':false:')
                                        elif fun_bindDict[x] == ':false:' and y == ':true:':
                                            fun_stack_final.append(':false:')
                                        elif fun_bindDict[x] == ':false:' and y == ':false:':
                                            fun_stack_final.append(':false:')
                                        else:
                                            fun_stack_final.append(y)
                                            fun_stack_final.append(x)
                                            fun_stack_final.append(':error:')
                                    elif y in fun_bindDict:
                                        if x == ':true:' and fun_bindDict[y] == ':true:':
                                            fun_stack_final.append(':true:')
                                        elif x == ':true:' and fun_bindDict[y] == ':false:':
                                            fun_stack_final.append(':false:')
                                        elif x == ':false:' and fun_bindDict[y] == ':true:':
                                            fun_stack_final.append(':false:')
                                        elif x == ':false:' and fun_bindDict[y] == ':false:':
                                            fun_stack_final.append(':false:')
                                        else:
                                            fun_stack_final.append(y)
                                            fun_stack_final.append(x)
                                            fun_stack_final.append(':error:')
                                    else:
                                        fun_stack_final.append(y)
                                        fun_stack_final.append(x)
                                        fun_stack_final.append(':error:')
                                else:
                                    fun_stack_final.append(':error:')
                            elif item == 'or':
                                if len(fun_stack_final) >= 2:
                                    x = fun_stack_final.pop()
                                    y = fun_stack_final.pop()
                                    if x == ':true:' and y == ':true:':
                                        fun_stack_final.append(':true:')
                                    elif x == ':true:' and y == ':false:':
                                        fun_stack_final.append(':true:')
                                    elif x == ':false:' and y == ':true:':
                                        fun_stack_final.append(':true:')
                                    elif x == ':false:' and y == ':false:':
                                        fun_stack_final.append(':false:')
                                    elif x in fun_bindDict and y in fun_bindDict:
                                        if fun_bindDict[x] == ':true:' and fun_bindDict[y] == ':true:':
                                            fun_stack_final.append(':true:')
                                        elif fun_bindDict[x] == ':true:' and fun_bindDict[y] == ':false:':
                                            fun_stack_final.append(':true:')
                                        elif fun_bindDict[x] == ':false:' and fun_bindDict[y] == ':true:':
                                            fun_stack_final.append(':true:')
                                        elif fun_bindDict[x] == ':false:' and fun_bindDict[y] == ':false:':
                                            fun_stack_final.append(':false:')
                                        else:
                                            fun_stack_final.append(y)
                                            fun_stack_final.append(x)
                                            fun_stack_final.append(':error:')
                                    elif x in fun_bindDict:
                                        if fun_bindDict[x] == ':true:' and y == ':true:':
                                            fun_stack_final.append(':true:')
                                        elif fun_bindDict[x] == ':true:' and y == ':false:':
                                            fun_stack_final.append(':true:')
                                        elif fun_bindDict[x] == ':false:' and y == ':true:':
                                            fun_stack_final.append(':true:')
                                        elif fun_bindDict[x] == ':false:' and y == ':false:':
                                            fun_stack_final.append(':false:')
                                        else:
                                            fun_stack_final.append(y)
                                            fun_stack_final.append(x)
                                            fun_stack_final.append(':error:')
                                    elif y in fun_bindDict:
                                        if x == ':true:' and fun_bindDict[y] == ':true:':
                                            fun_stack_final.append(':true:')
                                        elif x == ':true:' and fun_bindDict[y] == ':false:':
                                            fun_stack_final.append(':true:')
                                        elif x == ':false:' and fun_bindDict[y] == ':true:':
                                            fun_stack_final.append(':true:')
                                        elif x == ':false:' and fun_bindDict[y] == ':false:':
                                            fun_stack_final.append(':false:')
                                        else:
                                            fun_stack_final.append(y)
                                            fun_stack_final.append(x)
                                            fun_stack_final.append(':error:')
                                    else:
                                        fun_stack_final.append(y)
                                        fun_stack_final.append(x)
                                        fun_stack_final.append(':error:')
                                else:
                                    fun_stack_final.append(':error:')
                            elif item == 'not':
                                if len(fun_stack_final) >= 1:
                                    x = fun_stack_final.pop()
                                    if x == ':true:':
                                        fun_stack_final.append(':false:')
                                    elif x == ':false:':
                                        fun_stack_final.append(':true:')
                                    elif x in fun_bindDict:
                                        if fun_bindDict[x] == ':true:':
                                            fun_stack_final.append(':false:')
                                        elif fun_bindDict[x] == ':false:':
                                            fun_stack_final.append(':true:')
                                        else:
                                            fun_stack_final.append(x)
                                            fun_stack_final.append(':error:')
                                    else:
                                        fun_stack_final.append(x)
                                        fun_stack_final.append(':error:')
                                else:
                                    fun_stack_final.append(':error:')
                            elif item == 'equal':
                                if len(fun_stack_final) >= 2:
                                    y = fun_stack_final.pop()
                                    x = fun_stack_final.pop()
                                    if type(x) == int and type(y) == int:
                                        if x == y:
                                            fun_stack_final.append(':true:')
                                        else:
                                            fun_stack_final.append(':false:')
                                    elif x in fun_bindDict and y in fun_bindDict:
                                        if type(fun_bindDict[x]) == int and type(fun_bindDict[y]) == int:
                                            if fun_bindDict[x] == fun_bindDict[y]:
                                                fun_stack_final.append(':true:')
                                            else:
                                                fun_stack_final.append(':false:')
                                        else:
                                            fun_stack_final.append(x)
                                            fun_stack_final.append(y)
                                            fun_stack_final.append(':error:')
                                    elif x in fun_bindDict:
                                        if type(fun_bindDict[x]) == int and type(y) == int:
                                            if fun_bindDict[x] == y:
                                                fun_stack_final.append(':true:')
                                            else:
                                                fun_stack_final.append(':false:')
                                        else:
                                            fun_stack_final.append(x)
                                            fun_stack_final.append(y)
                                            fun_stack_final.append(':error:')
                                    elif y in fun_bindDict:
                                        if type(x) == int and type(fun_bindDict[y]) == int:
                                            if x == fun_bindDict[y]:
                                                fun_stack_final.append(':true:')
                                            else:
                                                fun_stack_final.append(':false:')
                                        else:
                                            fun_stack_final.append(x)
                                            fun_stack_final.append(y)
                                            fun_stack_final.append(':error:')
                                    else:
                                        fun_stack_final.append(x)
                                        fun_stack_final.append(y)
                                        fun_stack_final.append(':error:')
                                else:
                                    fun_stack_final.append(':error:')
                            elif item == 'lessThan':
                                if len(fun_stack_final) >= 2:
                                    x = fun_stack_final.pop()
                                    y = fun_stack_final.pop()
                                    if type(x) == int and type(y) == int:
                                        if x > y:
                                            fun_stack_final.append(':true:')
                                        else:
                                            fun_stack_final.append(':false:')
                                    elif x in fun_bindDict and y in fun_bindDict:
                                        if type(fun_bindDict[x]) == int and type(fun_bindDict[y]) == int:
                                            if fun_bindDict[x] > fun_bindDict[y]:
                                                fun_stack_final.append(':true:')
                                            else:
                                                fun_stack_final.append(':false:')
                                        else:
                                            fun_stack_final.append(x)
                                            fun_stack_final.append(y)
                                            fun_stack_final.append(':error:')
                                    elif x in fun_bindDict:
                                        if type(fun_bindDict[x]) == int and type(y) == int:
                                            if fun_bindDict[x] > y:
                                                fun_stack_final.append(':true:')
                                            else:
                                                fun_stack_final.append(':false:')
                                        else:
                                            fun_stack_final.append(x)
                                            fun_stack_final.append(y)
                                            fun_stack_final.append(':error:')
                                    elif y in fun_bindDict:
                                        if type(x) == int and type(fun_bindDict[y]) == int:
                                            if x > fun_bindDict[y]:
                                                fun_stack_final.append(':true:')
                                            else:
                                                fun_stack_final.append(':false:')
                                        else:
                                            fun_stack_final.append(x)
                                            fun_stack_final.append(y)
                                            fun_stack_final.append(':error:')
                                    else:
                                        fun_stack_final.append(x)
                                        fun_stack_final.append(y)
                                        fun_stack_final.append(':error:')
                                else:
                                    fun_stack_final.append(':error:')
                            elif item == 'bind':
                                if len(fun_stack_final) >= 2:
                                    x = fun_stack_final.pop()
                                    y = fun_stack_final.pop()
                                    if y != ':true:' and y != ':false:' and y != 'add' and y != 'sub' and y != 'mul' and y != 'div' and y != 'rem' and y != 'neg' and y != 'pop' and y != 'swap' and y != ':error:' and y != 'and' and y != 'or' and y != 'not' and y != 'equal' and y != 'lessThan' and y != 'bind' and y != 'if' and y != 'let' and y != 'end':
                                        if x != 'add' and x != 'sub' and x != 'mul' and x != 'div' and x != 'rem' and x != 'neg' and x != 'pop' and x != 'swap' and x != ':error:' and x != 'and' and x != 'or' and x != 'not' and x != 'equal' and x != 'lessThan' and x != 'bind' and x != 'if' and x != 'let' and x != 'end':
                                            if type(y) != int and '"' not in y:
                                                if x in fun_bindDict:
                                                    fun_bindDict[y] = fun_bindDict[x]
                                                    fun_stack_final.append(':unit:')
                                                elif type(x) == str and '"' not in x and x != ':true:' and x != ':false:' and x != ':unit:':
                                                    fun_stack_final.append(y)
                                                    fun_stack_final.append(x)
                                                    fun_stack_final.append(':error:')
                                                else:
                                                    fun_bindDict[y] = x
                                                    fun_stack_final.append(':unit:')
                                            else:
                                                fun_stack_final.append(y)
                                                fun_stack_final.append(x)
                                                fun_stack_final.append(':error:')
                                        else:
                                            fun_stack_final.append(y)
                                            fun_stack_final.append(x)
                                            fun_stack_final.append(':error:')
                                    else:
                                        fun_stack_final.append(y)
                                        fun_stack_final.append(x)
                                        fun_stack_final.append(':error:')
                                else:
                                    fun_stack_final.append(':error:')
                            elif item == 'if':
                                if len(fun_stack_final) >= 3:
                                        x = fun_stack_final.pop()
                                        y = fun_stack_final.pop()
                                        z = fun_stack_final.pop()
                                        if z == ':true:' or z == ':false:':
                                            if z == ':true:':
                                                fun_stack_final.append(x)
                                            elif z == ':false:':
                                                fun_stack_final.append(y)
                                            else:
                                                fun_stack_final.append(z)
                                                fun_stack_final.append(y)
                                                fun_stack_final.append(x)
                                                fun_stack_final.append(':error:')
                                        elif z in fun_bindDict:
                                            if fun_bindDict[z] == ':true:' or fun_bindDict[z] == ':false:':
                                                if fun_bindDict[z] == ':true:':
                                                    fun_stack_final.append(x)
                                                elif fun_bindDict[z] == ':false:':
                                                    fun_stack_final.append(y)
                                                else:
                                                    fun_stack_final.append(z)
                                                    fun_stack_final.append(y)
                                                    fun_stack_final.append(x)
                                                    fun_stack_final.append(':error:')
                                        else:
                                            fun_stack_final.append(':error:')
                                else:
                                    fun_stack_final.append(':error:')
                            elif item == 'call':
                                if len(fun_stack_final) >= 2:
                                    fun_Dict.update(nestedFunCall_dict)
                                    key = fun_stack_final.pop()
                                    arg = fun_stack_final.pop()
                                    #print("key: ", key)
                                    #print("arg: ", arg)
                                    #argToBindToFunOutput.append(arg)
                                    if arg != ':error:':
                                        if key in fun_Dict:
                                            fun_stack2 = []
                                            fun_stack_final = []
                                            #print("found this function in the function dictionary")
                                            #print('Key: ', key)
                                            #print('Here is the list of instructions for this function: ', fun_Dict[key][0])
                                            #print('This argument needs to to change all ', fun_Dict[key][1], ' to ', arg)
                                            for item in fun_Dict[key][0]:
                                                #print('looking at instruction in the function dictionary: ', item)
                                                #print('Comparing to: ', fun_Dict[key][1])
                                                if item == fun_Dict[key][1]:
                                                    if fun_Dict[key][1] in fun_bindDict:
                                                        fun_stack2.append(fun_bindDict[fun_Dict[key][1]])
                                                    else:
                                                        fun_stack2.append(arg)
                                                else:
                                                    fun_stack2.append(item)
                                            del fun_Dict[key]
                                            fun_Dict[key] = fun_stack2
                                        else:
                                            fun_stack_final.append(arg)
                                            fun_stack_final.append(key)
                                            fun_stack_final.append(':error:')
                                    else:
                                        fun_stack_final.append(arg)
                                        fun_stack_final.append(key)
                                        fun_stack_final.append(':error:')
                                else:
                                    fun_stack_final.append(error)
                            elif item == 'return':
                                if len(fun_stack_final) >= 1:
                                    if is_inoutfun == True:
                                        x = argToBindToFunOutput[0]
                                        #print("x: ", x)
                                        y = fun_bindDict[y]
                                        #print("y: ", y)
                                        bindDict[x] = y
                                        if returnInFun == True:
                                            stack.append(y)
                                            stack_count += 1
                                    else:
                                        stack.append(fun_stack_final[len(fun_stack_final) - 1])
                                        stack_count += 1
                                else:
                                    stack.append(':error:')
                                    stack_count += 1
                    else:
                        stack.append(arg)
                        stack.append(key)
                        stack.append(':error:')
                        stack_count += 3
                else:
                    stack.append(arg)
                    stack.append(key)
                    stack.append(':error:')
                    stack_count += 1
            else:
                stack.append(':error:')
                stack_count += 1
        else:
            print("This is the final stack: ", stack)
            print("These are the current bound items: ", bindDict)
            print("These are the current bound items in the inner stacks: ", let_bindDict)
            print('These are the keys in the dictionary: ', let_bound_items)
            print('This is the stack_count: ', stack_count)
            print('This is the let_count: ', let_count)
            #print('This is the stack count befroe let: ', stack_count_b4_let)
            print('This is the current function dictionary: ', fun_Dict)
            print('These are the current bound items within the function: ', fun_bindDict)
            print('Is an inOut function = ', is_inoutfun)
            print('return in function = ', returnInFun)
            print('Nested call within a function = ', nestedFunCall)
            print('Nested function dictionary: ', nestedFunCall_dict)
            print('There are multiple items bound in the let dictionary here they are: ', multipleLetBoundVar_dict)
            print('The multiple bound items in let dictionary is empyt: ', multipleLetBoundVarDictIsEmpty)
            print('mlbv: ', mlbv)
            for item in stack:
                if type(item) == str:
                    answer.append(item.strip('""'))
                else:
                    answer.append(item)
            sys.stdout = open(output, 'w')
            for item in answer[::-1]:
                print(item)
            sys.stdout.close()

main("output.txt")
