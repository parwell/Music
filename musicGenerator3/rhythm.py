# Rhythm Module
# Generates one beat at a time for a bar of music

import random
from save import *
import sys

# Asks for and verifies basics about rhythm
def getBarDetails():
    beat = input('Default beat rhythm (enter for \'----\': ')
    beat = verifyBeat(beat)
    beats = input('Number of beats (enter for 4): ')
    beats = verifyNumber(beats,4)
    return beat, beats


# Verifies an integer input
def verifyNumber(number, default):
    if not number:
        return default
    try:
        number = int(number)
        return number
    except:
        print('Invalid input, using default ({}).'.format(default))
    return default


# Verifies an input for a default beat pattern
def verifyBeat(beat):
    for note in list(beat):
        if note not in ['#','-']:
            print('Invalid input, using default (----).')
            return '----'
    if beat:
        return beat
    return '----'


# Generates a bar of rhythm based on user input
def generateBar():
    beat, beats = getBarDetails()
    if not beat and not beats:
        return None
    bar = []
    for i in range(beats):
        currentBeat = list(beat)
        for place, note in enumerate(currentBeat):
            if note == '-':
                if random.randrange(2) == 1:
                    currentBeat[place] = '#'
        currentBeat = ''.join(currentBeat)
        bar.append(currentBeat)
    return bar


# Shows and asks to save a bar of rhythm based on user input
def printBar():
    bar = generateBar()
    output = ''
    for beat in bar:
        currentBeat = ''
        for note in beat:
            currentBeat += note + '   '
        currentBeat += '\n'
        output += currentBeat
    print(output)
    askToSave(output, 'rhythm')


# The main function of the module
def main():
    printBar()


if __name__ == '__main__':
    print('Rhythm Module')
    main()
    input()
    sys.exit()

