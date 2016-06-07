import sys

'''
00 - End program
01 - End of instr
02 - Push
03 - Pop
04 - Print
05 - Add
06 - Subtract
'''
stack = []
OP_EOP = "00"
OP_EOI = "01"
OP_PUSH = "02"
OP_POP = "03"
OP_PRINT = "04"
OP_ADD = "05"
OP_SUB = "06"
OP_MUL = "07"
OP_DIV = "08"

def load_program(argv):
    f = open(argv)
    lines = f.read().replace("\n", " ")
    lines = lines.split(" ")
    f.close()
    return lines

def do_EOP():
    print "EOP"

def do_PUSH(i, l):
    topush = int(l[i+1], 16)
    stack.append(topush)

def do_POP():
    stack.pop()

def do_PRINT(stack):
    print stack[-1]

def do_ADD(stack):
    num1 = stack[-1]
    num2 = stack[-2]
    total = num1 + num2
    stack.pop()
    stack.pop()
    stack.append(total)

def do_SUB(stack):
    num1 = stack[-1]
    num2 = stack[-2]
    diff = num1 - num2
    stack.pop()
    stack.pop()
    stack.append(diff)

def do_MUL(stack):
    num1 = stack[-1]
    num2 = stack[-2]
    mult = num1 * num2
    stack.pop()
    stack.pop()
    stack.append(mult)
def do_DIV(stack):
    num1 = stack[-1]
    num2 = stack[-2]
    div = num2 / num1
    stack.pop()
    stack.pop()
    stack.append(div)

def execute_program(l):
    loop = 1
    i = 0
    while loop:
        instruction = l[i]
        if instruction == OP_EOP:
            do_EOP()
            loop = 0
        elif instruction == OP_PUSH:
            do_PUSH(i, l)
        elif instruction == OP_POP:
            do_POP()
        elif instruction == OP_PRINT:
            do_PRINT(stack)
        elif instruction == OP_ADD:
            do_ADD(stack)
        elif instruction == OP_SUB:
            do_SUB(stack)
        elif instruction == OP_MUL:
            do_MUL(stack)
        elif instruction == OP_DIV:
            do_DIV(stack)

        i += 1


def run_program(argv):

    l = load_program(argv)
    execute_program(l)

def main(argv):
    run_program(argv[1])
    return 0

def target(*args):
    return main, None

if __name__ == '__main__':
    main(sys.argv)