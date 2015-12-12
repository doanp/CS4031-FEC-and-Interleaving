import numpy as np

def Interleave(input):

    data = input.split(' ')
    resMatrix = []

    for item in data:
     resMatrix.append(item)
     temp = map(None, *resMatrix)

    final = np.array(temp)
    #return column by column matrix
    return final

def deInterleave(input):

    resMatrix = []

    for item in input:
     resMatrix.append(item)
     temp = map(None, *resMatrix)

    final = np.array(temp)
    return final

#usage
# print interleave(['hello'])
bits = '01101000 01100101 01101100 01101100 01101111'
interleave =  Interleave(bits)
print "interleave = " , interleave
deinterleave = deInterleave(interleave)
print "deinterleave" ,deinterleave

#Results=====
"""interleave =  [['0' '0' '0' '0' '0']
 ['1' '1' '1' '1' '1']
 ['1' '1' '1' '1' '1']
 ['0' '0' '0' '0' '0']
 ['1' '0' '1' '1' '1']
 ['0' '1' '1' '1' '1']
 ['0' '0' '0' '0' '1']
 ['0' '1' '0' '0' '1']]
deinterleave [['0' '1' '1' '0' '1' '0' '0' '0']
 ['0' '1' '1' '0' '0' '1' '0' '1']
 ['0' '1' '1' '0' '1' '1' '0' '0']
 ['0' '1' '1' '0' '1' '1' '0' '0']
 ['0' '1' '1' '0' '1' '1' '1' '1']] """
