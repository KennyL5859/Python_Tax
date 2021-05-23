
"""
In class exercise to demonstrate use of picking sets of student names for a class
"""

import pickle

# Function to take a file, create a set of student names and save the file through serialization
def saveClassNames(fileVar):
    # create an empty set
    classNames = set()

    name = input('Enter the student name (DONE to end): ')

    while name.upper() != 'DONE':
        classNames.add(name)
        name = input('Enter another student name (DONE to end): ')

    # use pickle.dump method to write data to file preserving structure
    pickle.dump(classNames, fileVar)


def main():

    fileName = input('Enter the file name to store student names for classes: ')

    # opne file in binary mode for writing
    outputFile = open(fileName, 'wb')
    again = 'y'

    while again.lower() == 'y':

        # get and save all names for class
        saveClassNames(outputFile)
        again = input('Do you want to add another class of students? (y/n) ')

    outputFile.close()

main()


