# Rhythm Generator
# Generates one quarter note at a time for a full measure of music

import random

def menu():
    print("\nWhat would you like to do?")
    print("0 - Random bar (straight feel)")
    print("1 - Random bar (triplet feel)")
    print("2 - Random bar (user input template)")
    choice = input("Choice: ")
    if choice in ['0', '1', '2']:    
        return int(choice)
    else:
        print("I'm sorry, that wasn't a choice.\n\n")
        return None

def switcher():
    choice = menu()
    if choice == 0:
        rand_bar(4)
    elif choice == 1:
        rand_bar(3)
    elif choice == 2:
        template_bar()
    else:
        print()

def rand_bar(value):
    empty_note = "-" * value
    time_sig = int(input("\n\nHow many beats? (1-16): "))
    if time_sig < 1 or time_sig > 16:
        print("I'm sorry, I cannot use that value.\n\n")
    else:
        bar = []
        value = get_probability() + 1
        for x in range(time_sig):
            new = ""
            for i in range(len(empty_note)):
                if random.randrange(100)+1 <= value:
                    new += "#  "
                else:
                    new += empty_note[i]
                    new += '  '
            bar.append(new)
        for i in bar:
            print("Bar: " + i)

def get_probability():
    print("More or less notes?")
    print("0 - Less")
    print("1 - Equiprobable")
    print("2 - More")
    choice = input("Choice: ")
    if choice == '0':
        return 30
    elif choice == '1':
        return 50
    elif choice == '2':
        return 70
    else:
        return 50

def template_bar():
    template = ''
    template = input("Type in a default rhythm for each note: ")
    time_sig = int(input("How many notes? (1-16): "))
    if time_sig < 1 or time_sig > 16:
        print("I'm sorry, I cannot use that value.\n\n")
    else:
        bar = []
        for x in range(time_sig):
            new = ""
            for i in range(len(template)):
                if i == '!':
                    new += '!  '
                else:
                    if random.randrange(2) == 1:
                        new += "!  "
                    else:
                        new += template[i]
                        new += '  '
            bar.append(new)
        for i in bar:
            print("Bar: " + i)




if __name__ == "__main__":
    print("This is only a module!")
    input()
