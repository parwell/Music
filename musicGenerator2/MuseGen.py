# MuseGen
# Generates samples of melody, chords, and rhythm


import rhythm
import scales
import melody
import sys


# Gets the user's choice on what to do
def getChoice():
    print('What would you like to do?')
    print('0 - Rhythm')
    print('1 - Scales')
    print('2 - Melody')
    answer = input('Choice (enter to quit): ')
    if answer:
        if answer == '0':
            rhythm.main()
        elif answer == '1':
            scales.main()
        elif answer == '2':
            melody.main()
        else:
            print('Invalid input.\n')
        getChoice()
    sys.exit()

# The main program loop
def main():
    print('Welcome to MuseGen.')
    getChoice()


if __name__ == '__main__':
    main()
