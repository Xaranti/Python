instruction = ['say hello','say how are you','abort','ask for money','saythank you','say bye']
instructionApproved = []

for instr in instruction:
    print('Adding instruction:', instr)
    instructionApproved.append(instr)
    if instr == 'abort':
        print ('aborting')
        instructionApproved.clear()
        break

print ("following actrion ll be taken:", instructionApproved)