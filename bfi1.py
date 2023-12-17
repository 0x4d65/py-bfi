#BrainFuckInterpreter by 0x4d65
#i wrote this 2 years ago and now im trying to add some comments
#no idea if the loops finally work it's been almost 2 years since i tried to fix them 
import sys

#initialize variables
pointer = 0
cells = [0]
looplist = []
buffer = []
lsp_lib = [] # no idea what this is, something to do with loops
cp = 0 # code pointer (index)  
ln = 0 # loop number
loopBypass = False
for x in range(30000):
    cells.append(0)
for x in range(30000):
    lsp_lib.append(0)
#load code to ram
filename = sys.argv[1]
file = open(filename, 'rt')
code = file.read()
code = list(code)

#main code interpretation
while cp != len(code):
    if code[cp] == '+':
        cells[pointer] += 1
    if code[cp] == '-': 
        cells[pointer] -= 1
    if code[cp] == '.': 
        print(chr(cells[pointer]), end = "")
    if code[cp] == ',': 
        cells[pointer] = int(ord(input()))
        print("")
    if code[cp] == '>': 
        pointer += 1
    if code[cp] == '<': 
        pointer -= 1
    if code[cp] == '[':
        ln += 1     
        lsp_lib[ln] = cp 
    if code[cp] == ']':
        if cells[pointer] != 0:
            cp = lsp_lib[ln]
        else:
            ln -= 1

            
    cp += 1
try:
    if sys.argv[2] == '--memmap':
        print('[', end='')
        for y in range(int(sys.argv[3])):
            print(str(cells[y]), end = '],[')
except:
    print('')
