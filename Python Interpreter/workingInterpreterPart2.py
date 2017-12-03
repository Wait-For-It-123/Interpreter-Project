# This project is creating an Interpreter. This project will be broken into 3 parts. All parts will be built off
# one another and placed into this python interpreter file
import sys


def interpreter(input, output):
    # The input list will take everything from the input file and put it into a list to begin with
    input_list = []
    # Finalized list that will be used for stack
    finalized_values_list = []
    # Main stack for the interpreter
    stack = []
    # This dictionary is used to keep track of which items are bound to eachother
    let_bound_items = []
    # This is the list of keys, so that I can delete them from the dictionary when all let...ends are finished
    bindDict = {}
    # Keep track of bound iteams in the inner stack
    let_bindDict = {}
    # This is used at the end to get rid of quotes for strings
    answer = []
    # Keep track of how many items are in the final stack to be able to preform checks
    stack_count = 0
    # Keep track of the number of items in the finalized_values_list so that when let is called I can keep track of where I left off in reading through the finalized_values_list
    input_list_count = 0
    # Keep track of the number of inner stacks I have for let...end
    let_count = 0
    # Help with math when calling the end of let...end
    stack_count_b4_let = 0
    # Read line by line and place everything into the initial list
    line_to_interpret = open(input, 'r')
    for line in line_to_interpret:
        input_list.append(line.rstrip('\n'))

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
            else:
                finalized_values_list.append(item.strip(' push'))
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
        elif item == 'fun':
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
        #print("current stack: ", stack)
        input_list_count += 1
        if type(item) == int:
            stack.append(item)
            stack_count += 1
        elif item != ':error:' and item != ':true:' and item != ':false:' and item != 'add' and item != 'neg' and item != 'mul' and item != 'sub' and item != 'div' and item != 'rem' and item != 'swap' and item != 'pop' and item != 'and' and item != 'or' and item != 'not' and item != 'equal' and item != 'lessThan' and item != 'bind' and item != 'if' and item != 'let' and item != 'end' and item != 'quit':
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
                #print('In the let looking at: ', item)
                if type(item) == int:
                    finalized_values_list.remove(item)
                    tempStack.append(item)
                elif item != ':error:' and item != ':true:' and item != ':false:' and item != 'add' and item != 'neg' and item != 'mul' and item != 'sub' and item != 'div' and item != 'rem' and item != 'swap' and item != 'pop' and item != 'and' and item != 'or' and item != 'not' and item != 'equal' and item != 'lessThan' and item != 'bind' and item != 'if' and item != 'let' and item != 'end' and item != 'quit':
                    finalized_values_list.remove(item)
                    tempStack.append(item)
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
                                    elif type(x) == str and '"' not in x and x != ':true:' and x != ':false:' and x != ':unit:':
                                        stack.append(y)
                                        stack.append(x)
                                        stack.append(':error:')
                                        stack_count += 1
                                    else:
                                        let_bound_items.append(y)
                                        let_bindDict[y] = x
                                        tempStack.append(':unit:')
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
                elif item == 'end':
                    finalized_values_list.remove(item)
                    if stack_count == let_count:
                        if let_count > 1:
                            elementTransfer = tempStack[len(tempStack) - 1]
                            tempStack = stack[let_count - 2]
                            tempStack.append(elementTransfer)
                            del stack[let_count - 1]
                            let_count -= 1
                            stack_count -= 1
                        elif let_count == 1:
                            elementTransfer = tempStack[len(tempStack) - 1]
                            stack.append(elementTransfer)
                            del stack[let_count - 1]
                            let_count -= 1

                            for item in let_bound_items:
                                if item in let_bindDict:
                                    del let_bindDict[item]
                            break
                    elif stack_count_b4_let > 1:
                        if let_count > 1:
                            elementTransfer = tempStack[len(tempStack) - 1]
                            tempStack = stack[let_count]
                            tempStack.append(elementTransfer)
                            del stack[let_count + 1]
                            let_count -= 1
                            stack_count -= 1
                        elif let_count == 1:
                            elementTransfer = tempStack[len(tempStack) - 1]
                            stack.append(elementTransfer)
                            del stack[let_count + 1]
                            let_count -= 1
                            for item in let_bound_items:
                                if item in let_bindDict:
                                    del let_bindDict[item]
                            break
                    else:
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
                            break
                elif item == 'let':
                    break
        else:
            print("This is the final stack: ", stack)
            print("These are the current bound items: ", bindDict)
            print("These are the current bound items in the inner stacks: ", let_bindDict)
            print('These are the keys in the dictionary: ', let_bound_items)
            print('this is the stack_count: ', stack_count)
            print('this is the let_count: ', let_count)
            print('this is the stack count befroe let: ', stack_count_b4_let)
            for item in stack:
                if type(item) == str:
                    answer.append(item.strip('""'))
                else:
                    answer.append(item)
            sys.stdout = open(output, 'w')
            for item in answer[::-1]:
                print(item)
            sys.stdout.close()


#interpreter("in2_updated.txt", "output.txt")
