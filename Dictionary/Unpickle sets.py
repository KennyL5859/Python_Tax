

import pickle


def main():

    filename = input('Enter the file name to read student names for a class: ')

    inputFile = open(filename, 'rb')
    endOfFile = False

    while not endOfFile:

        try:
            classNames = pickle.load(inputFile)
            print('Displaying class: ')

            for name in classNames:
                print('\t' + name)

        except EOFError:
            endOfFile = True



    inputFile.close()

    






main()