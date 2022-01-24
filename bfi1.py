#BrainFuckInterpreter by 0x4d65
#Currently doesn't support nested loops
import sys

#initialize variables
pointer = 0
cells = [0]
looplist = []
buffer = []
lsp = 0
cp = 0
loopBypass = False
for x in range(30000):
    cells.append(0)

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
        lsp = cp
    if code[cp] == ']':
        if cells[pointer] != 0:
            cp = lsp
    cp += 1
try:
    if sys.argv[2] == '--memmap':
        print('[', end='')
        for y in range(int(sys.argv[3])):
            print(str(cells[y]), end = '],[')
except:
    print('')
