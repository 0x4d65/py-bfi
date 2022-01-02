#BrainFuckInterpreter by 0x4d65
#Currently doesn't support nested loops
import sys

#initialize variables
pointer = 0
cells = [0]
looplist = []
buffer = []
loopBypass = False
for x in range(30000):
    cells.append(0)

#load code to ram
filename = sys.argv[1]
file = open(filename, 'rt')
code = file.read()
code = list(code)

#main code interpretation
for x in code:
    if x == '+' and loopBypass == False:
        cells[pointer] += 1
    if x == '-' and loopBypass == False:
        cells[pointer] -= 1
    if x == '.' and loopBypass == False:
        buffer.append(chr(cells[pointer]))
    if x == ',' and loopBypass == False:
        output = '';
        output = output.join(buffer)
        print(output)
        buffer.clear()
        cells[pointer] = int(ord(input()))
    if x == '>' and loopBypass == False:
        pointer += 1
    if x == '<' and loopBypass == False:
        pointer -= 1
    if x == '[' and loopBypass == False:
        loopBypass = True
        continue
    if x != ']' and loopBypass:
        looplist.append(x)
    if x == ']':
        loopBypass = False
        while cells[pointer] != 0:
            for y in looplist:
                if y == '+':
                    cells[pointer] += 1
                if y == '-':
                    cells[pointer] -= 1
                if y == '.':
                    buffer.append(chr(cells[pointer]))
                if y == ',':
                    cells[pointer] = ord(input())
                    output = '';
                    output = output.join(buffer)
                    buffer.clear()
                    print(output)
        
                if y == '>':
                    pointer += 1
                if y == '<':
                    pointer -= 1
        looplist.clear() 

'''
Output buffering so instead of:
H
e
l
l
o

w
o
r
l
d
!
we get
Hello world!
'''
output = '';
output = output.join(buffer)
print(output)
        





