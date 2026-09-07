from os import listdir, path
from random import randint
from playsound3 import playsound

import config
from config import *

# Prepare list of files containing quotes
filePaths = []
for file in listdir('quotes'):
    filePaths.append(path.join('quotes', file))
filePaths.sort() # ensure numeric order

# Add quotes to a matrix
# entry = [quote(str), video(int), line(int)]
quotes = []
for i in range(len(filePaths)):
    with open(filePaths[i]) as f:
        foo = f.read().splitlines()
    for j in range(len(foo)):
        quotes.append((foo[j], i, j))

quotes = tuple(quotes)

sel = quotes[randint(0, len(quotes)-1)]
bar   = sel[0]
book  = sel[1]
verse = sel[2]

# assemble output text
output = ""
if config.showBookVerseNumber:
    output += f'[{book+1},{verse+1}] '
output += bar

print(output)

if config.playSound:
    soundFile = path.join('sound', f'{book}/df_{book}_{verse}.mp3')
    if path.exists(soundFile):
        playsound(soundFile)
    else:
        print('Sound does not exist:', soundFile)
