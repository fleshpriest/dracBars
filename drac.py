from os import listdir, path
from random import randint

import config
from config import *

# assemble a matrix of all drac quotes
quoteMatrix = []
for file in listdir('quotes'):
    filepath = path.join('quotes', file)
    with open(filepath) as f:
        quoteMatrix.append(f.read().splitlines())

# get random drac quote from matrix
book = randint(0, len(quoteMatrix)-1)
verse = randint(0, len(quoteMatrix[book])-1)

# assemble output text
output = ""
if config.showBookVerseNumber:
    output += f'[{book},{verse}] '
output += quoteMatrix[book][verse]

print(output)





