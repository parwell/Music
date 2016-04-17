# Scales
# Chooses a random scale for composer to use

import random
from scaleList import *
import sys


# Gets criteria to find a scale and checks for availability
def main():
    criteria = input('Choose notes to search for (enter for random scale): ')
    if not criteria:
        showRandomScale()
    else:
        findScale(criteria)


# Finds a scale based on criteria and shows it to the user
def findScale(criteria):
    criteria = criteria.split()
    results = []
    for scale in SCALES:
        if set(criteria).issubset(scale):
            results.append(scale)
    if results:
        print('The following scales meet your criteria:')
        for scale in results:
            print(scale[0] + ' Major: ', end='')
            for note in scale:
                print(note, end=' ')
            print('\n')
    else:
        print('No scales found.')


# Finds a random scale and prints it
def showRandomScale():
    scale =  random.choice(SCALES)
    print('Your scale is: ' + str(scale[0]) + ' major.')
    print('Notes: ', end='')
    for note in scale:
        print(note, end=' ')
    print('\n')


if __name__ == '__main__':
    print('Scales Module')
    main()
    input()
    sys.exit()
