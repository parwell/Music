# Generates a random melody in a random scale

import random

def menu():
    print("\nWhat would you like to do?")
    print("0 - Note sequence (random scale)")
    print("1 - Note sequence (choose major scale)")
    print("2 - Melody (random scale, random straight rhythm)")
    print("3 - Melody (random scale, random triplet rhythm)")
    choice = input("Choice: ")
    if choice in ['0', '1', '2', '3']:
        return int(choice)
    else:
        print("I'm sorry, that wasn't a choice.\n\n")
        return None

def switcher():
    choice = menu()
    if choice == 0:
        rand_note_seq(rand_scale())
    elif choice == 1:
        rand_note_seq(choose_scale())
    elif choice == 2:
        rand_melody(rand_scale(), rand_bar(4))
    elif choice == 3:
        rand_melody(rand_scale(), rand_bar(3))
    else:
        print()

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
    return scale

def choose_scale():
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

    SCALES = ['A', 'B', 'C', 'D', 'E', 'F', 'G', \
              'A#', 'B#', 'C#', 'D#', 'E#', 'F#', 'G#', \
              'Ab', 'Bb', 'Cb', 'Db', 'Eb', 'Fb', 'Gb']

    SCALES_CON = {'A':A, 'B':B, 'C':C, 'D':D, 'E':E, 'F':F, 'G':G, \
                  'A#':As, 'B#':Bs, 'C#':Cs, 'D#':Ds, \
                  'E#':Es, 'F#':Fs, 'G#':Gs, \
                  'Ab':Ab, 'Bb':Bb, 'Cb':Cb, \
                  'Db':Db, 'Eb':Eb, 'Fb':Fb, 'Gb':Gb}
    
    print("\n\nWhich major scale would you like to use?")
    scale = input("Scale: ")
    if scale not in SCALES:
        print("I'm sorry, I don't know that scale.\n")
        return None
    else:
        return SCALES_CON[scale]

def rand_note_seq(scale):
    if scale == None:
        print()
    else:
        notes = int(input("How many notes? (1-16): "))
        if notes < 1 or notes > 16:
            print("I'm sorry, I cannot use that value.\n\n")
        else:
            melody = []
            for x in range(notes):
                melody.append(random.choice(scale))
            print("Scale: " + scale[0] + " Major")
            print("Melody:")
            for i in melody:
                print(i, end=" ")
            print("\n\n")

def rand_bar(value):
    note = '-' * value
    bar = [note]
    time_sig = int(input("\n\nHow many quarter notes? (1-16): "))
    if time_sig < 1 or time_sig > 16:
        print("I'm sorry, I cannot use that value.\n\n")
        return None
    else:
        bar *= time_sig
        return bar

def rand_note(scale):
    note = random.choice(scale)
    return note

def rand_melody(scale, bar):
    print("Here is your random melody.")
    print("Scale: " + scale[0] + " Major")
    print("Melody:")
    new_bar = []
    for i in bar:
        new = ""
        for x in range(len(i)):
            if random.randrange(2) == 1:
                note = rand_note(scale)
                new += note
                if len(note) == 3:
                    new += ' '
                elif len(note) == 2:
                    new += '  '
                else:
                    new += '   '
            else:
                new += '-   '
        new_bar.append(new)
    for i in new_bar:
        print(i)
    ask_save(new_bar)

def ask_save(content):
    ans = input("\nWould you like to save this? (y/n): ")
    if ans == 'y':
        save(content)
        print("Saved.")
    else:
        print("Alright.")
    
def save(content):
    f = open("saved.txt", 'a')
    for item in content:
        f.write(str(item) + '\n')
    f.write("\n\n")
    f.close()

if __name__ == "__main__":
    print("Melody Module for MuseGen")
    input()
