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
    # Keep track of how many items are in the final stack to be able to preform checks
    stack_count = 0
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
                finalized_values_list.append(needed_value.strip('""'))
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
        if type(item) == int:
            stack.append(item)
            stack_count += 1
        elif item != ':error:' and item != ':true:' and item != ':false:' and item != 'add' and item != 'neg' and item != 'mul' and item != 'sub' and item != 'div' and item != 'rem' and item != 'swap' and item != 'pop' and item != 'quit':
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
        else:
            sys.stdout = open(output, 'w')
            for item in stack[::-1]:
                print(item)
            sys.stdout.close()


# interpreter("sample_input6.txt", "output.txt")
