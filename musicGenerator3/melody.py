# Melody Module
# Generates a random melody in a random scale

from rhythm import *
from scaleList import *
from save import *
import sys


# Shows possible melody choices
# Asks for input and ensures proper output
def menu():
    print('What would you like to do?')
    print('0 - Note sequence')
    print('1 - Melody')
    print('2 - Tone Row')
    choice = input('Choice: ')
    if choice in ['0', '1', '2']:
        return int(choice)
    else:
        print('Invalid input.\n')
        return None


# Calls function based on user's choice
def main():
    choice = menu()
    if choice == 0:
        randomNoteSeq()
    elif choice == 1:
        showMelody()
    elif choice == 2:
        showToneRow()


# Asks user to choose a scale
# Returns a random scale if no preference is shown or if input doesn't work
def getScale():
    scale = input('Scale (enter for random): ')
    if not scale:
        return random.choice(SCALES)
    if scale not in SCALES_DICT:
        print('Unrecognized scale, using a random one.')
        return random.choice(SCALES)
    else:
        return SCALES_DICT[scale]


# Asks for a number of notes and ensures a proper output
def getNotes():
    notes = input('Number of notes (enter for 5): ')
    notes = verifyNumber(notes, 5)
    return notes


# Generates and displays a random sequence of notes
# Based on user input for scale and number of notes used
def randomNoteSeq():
    scale = getScale()
    notes = getNotes()
    sequence = []
    for note in range(notes):
        sequence.append(random.choice(scale))
    print('Scale: ' + scale[0] + ' Major')
    print('Melody: ', end='')
    for note in sequence:
        print(note, end=' ')
    sequence = '  '.join(sequence)
    askToSave(sequence, 'melody')


# Generates a random melody returned as a string
# Based on user input for scale and rhythm used
def generateMelody():
    scale = getScale()
    bar = generateBar()
    melody = []
    for beat in bar:
        currentBeat = list(beat)
        for place, note in enumerate(currentBeat):
            if note == '#':
                currentBeat[place] = random.choice(scale)
            elif note == '-':
                if random.randrange(1):
                    currentBeat[place] = random.choice(scale)
        melody.append(currentBeat)
    return melody, scale


# Creates, displays, and saves a melody
def showMelody():
    melody, scale = generateMelody()
    print('Scale: ' + scale[0] + ' Major')
    print('Melody:')
    output = ''
    for beat in melody:
        newBeat = ''
        for note in beat:
            spaces = (4 - len(note)) * ' '
            newNote = note + spaces
            newBeat += newNote
        newBeat += '\n'
        output += newBeat
    print(output)
    askToSave(output,'melody')


# Generates a random tone row and returns as a string
def toneRow():
    allNotes = ['A','A#','B','C','C#','D','D#','E','F','F#','G','G#']
    random.shuffle(allNotes)
    random.shuffle(allNotes)
    random.shuffle(allNotes)
    output = ''
    for note in allNotes:
        output += note
        output += (3 - len(note)) * ' '
    return output


# Creates, displays, and saves a tone row
def showToneRow():
    row = toneRow()
    print('Tone Row: ' + row)
    askToSave(row, 'melody')


if __name__ == '__main__':
    print('Melody Module')
    main()
    input()
    sys.exit()
