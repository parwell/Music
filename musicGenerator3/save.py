# Save Module
# for saving anything generated by the program to a .txt


# Asks a user whether or not to save generated content
# Does so if the user wants
def askToSave(content, fileName):
    answer = input('\nSave? (y/n): ')
    while answer != 'y' and answer != 'n':
        answer = input('Save? (y/n): ')
    if answer == 'y':
        save(content, fileName)
        print('Saved.')
    else:
        print('Ok.')


# Saves each piece of generated content in a .txt file
def save(content, fileName):
    with open(fileName + '.txt', 'a') as saved:
        saved.write(str(content) + '\n\n')
        saved.write('------------------------------------------------------------\n\n')


if __name__ == '__main__':
    print('Save Module')
    input()