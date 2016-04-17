# Scales
# Chooses a random scale for composer to use

import random

def choices():
    print("\nWhat would you like to do?")
    print("0 - Find a scale")
    print("1 - Random scale")
    
def switcher():
    choices()
    choice = input("Choice: ")
    if choice in ['0', '1']:
        if choice == '0':
            find_scale()
        if choice == '1':
            rand_scale()

def find_scale():
    # Natural scales
    A = ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#']
    B = ['B', 'C#', 'D#', 'E', 'F#', 'G#', 'A#']
    C = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
    D = ['D', 'E', 'F#', 'G', 'A', 'B', 'C#']
    E = ['E', 'F#', 'G#', 'A', 'B', 'C#', 'D#']
    F = ['F', 'G', 'A', 'Bb', 'C', 'D', 'E']
    G = ['G', 'A', 'B', 'C', 'D', 'E', 'F#']
    
    # Sharp scales
    As = ['A#', 'B#', 'C##', 'D#', 'E#', 'F##', 'G##']
    Bs = ['B#', 'C##', 'D##', 'E#', 'F##', 'G##', 'A##']
    Cs = ['C#', 'D#', 'E#', 'F#', 'G#', 'A#', 'B#']
    Ds = ['D#', 'E#', 'F#', 'G#', 'A#', 'B#', 'C##']
    Es = ['E#', 'F##', 'G##', 'A#', 'B#', 'C##', 'D##']
    Fs = ['F#', 'G#', 'A#', 'B', 'C#', 'D#', 'E#']
    Gs = ['G#', 'A#', 'B#', 'C#', 'D#', 'E#', 'F##']

    # Flat scales
    Ab = ['Ab', 'Bb', 'C', 'Db', 'Eb', 'F', 'G']
    Bb = ['Bb', 'C', 'D', 'Eb', 'F', 'G', 'A']
    Cb = ['Cb', 'Db', 'Eb', 'Fb', 'Gb', 'Ab', 'Bb']
    Db = ['Db', 'Eb', 'F', 'Gb', 'Ab', 'Bb', 'C']
    Eb = ['Eb', 'F', 'G', 'Ab', 'Bb', 'C', 'D']
    Fb = ['Fb', 'Gb', 'Ab', 'Bbb', 'Cb', 'Db', 'Eb']
    Gb = ['Gb', 'Ab', 'Bb', 'Cb', 'Db', 'Eb', 'F']

    SCALES = [A, B, C, D, E, F, G, \
              As, Bs, Cs, Ds, Es, Fs, Gs, \
              Ab, Bb, Cb, Db, Eb, Fb, Gb]

    results = []
    print("\nChoose some notes to search for: ", end='')
    criteria = input()
    criteria = criteria.split()
    print(criteria)
    for scale in SCALES:
        if set(criteria).issubset(scale):
            results.append(scale)
    print("The following scales meet your criteria:")
    for scale in results:
        print(scale[0] + ": ", end='')
        for note in scale:
            print(note, end=' ')
        print("\n")
    
def rand_scale():
    # Natural scales
    A = ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#']
    B = ['B', 'C#', 'D#', 'E', 'F#', 'G#', 'A#']
    C = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
    D = ['D', 'E', 'F#', 'G', 'A', 'B', 'C#']
    E = ['E', 'F#', 'G#', 'A', 'B', 'C#', 'D#']
    F = ['F', 'G', 'A', 'Bb', 'C', 'D', 'E']
    G = ['G', 'A', 'B', 'C', 'D', 'E', 'F#']
    
    # Sharp scales
    As = ['A#', 'C', 'D', 'D#', 'F', 'G', 'A']
    Bs = ['B#', 'C##', 'D##', 'E#', 'F##', 'G##', 'A##']
    Cs = ['C#', 'D#', 'E#', 'F#', 'G#', 'A#', 'B#']
    Ds = ['D#', 'E#', 'G', 'G#', 'A#', 'C', 'D']
    Es = ['E#', 'F##', 'G##', 'A#', 'B#', 'C##', 'D##']
    Fs = ['F#', 'G#', 'A#', 'B', 'C#', 'D#', 'F']
    Gs = ['G#', 'A#', 'C', 'C#', 'D#', 'F', 'G']

    # Flat scales
    Ab = ['Ab', 'Bb', 'C', 'Db', 'Eb', 'F', 'G']
    Bb = ['Bb', 'C', 'D', 'Eb', 'F', 'G', 'A']
    Cb = ['Cb', 'Db', 'Eb', 'Fb', 'Gb', 'Ab', 'Bb']
    Db = ['Db', 'Eb', 'F', 'Gb', 'Ab', 'Bb', 'C']
    Eb = ['Eb', 'F', 'G', 'Ab', 'Bb', 'C', 'D']
    Fb = ['Fb', 'Gb', 'Ab', 'Bbb', 'Cb', 'Db', 'Eb']
    Gb = ['Gb', 'Ab', 'Bb', 'Cb', 'Db', 'Eb', 'F']

    SCALES = [A, B, C, D, E, F, G, \
              As, Bs, Cs, Ds, Es, Fs, Gs, \
              Ab, Bb, Cb, Db, Eb, Fb, Gb]

    scale =  random.choice(SCALES)
    print("\nYour scale is: " + str(scale[0]) + " major.")
    print("Notes:")
    for i in scale:
        print(i)
    input()


if __name__ == "__main__":
    find_scale()
    input()
#    print("This is only a module!")
#    input()
