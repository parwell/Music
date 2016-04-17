# MuseGen
# Generates samples of melody, chords, and rhythm

import rhythm as r
import scales as s
import melody as m

def choices():
    print("\nWhat would you like to do?")
    print("0 - Quit")
    print("1 - Rhythm")
    print("2 - Scales")
    print("3 - Melody")

def menu_loop():
    choice = None
    while choice != '0':
        choices()
        choice = input("Choice: ")
        if choice in ['0', '1', '2', '3']:
            if choice == '1':
                r.switcher()
            if choice == '2':
                s.switcher()
            if choice == '3':
                m.switcher()
        else:
            print("I'm sorry, that wasn't a choice.")

print("Welcome to MuseGen.")
menu_loop()
print("Good-bye.\n")
input()
