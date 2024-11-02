import os.path
from dataclasses import dataclass
import re
import sys
import pathlib


# Two struct-type objects, make it easier to transfer specific data between functions.
# Flags - For sending the command-line flags to functions.
@dataclass
class flags:
    executables = False
    spreadsheets = False
    filepath = ""

# header - Struct for matching the header with the bytes at a certain offset (The offset is not implemented yet.)
@dataclass
class header:
    hexRepresent: str
    offset: int
    description: str

# Common headers for spreadsheets
spreadsheetHeaders = [
    header("09 08 10 00 00 06 05 00", 512, "MS Office excel sheet"),
    header("50 4B 03 04", 512, "ZIP, APK, ODT, and MORE!"),
    header("D0 CF 11 E0 A1 B1 1A E1", 512, "Object linking and embedding file. Best determined by extension.")
]

executableHeaders = [
    header("D0 CF 11 E0 A1 B1 1A E1", 512, "Object linking and embedding file. Best determined by extension."),
    header("4D 5A", 512, "Windows executable")
]

# Show an intro message.
def showFileHoundIntro():
    print("FileHound file scraper")

# Print a help message (Used a bunch in a lot of places.)
def printHelp():
    print("main.py -(s)(x) directory")

# Core of the program. A recursive function which drops
# down the file directory structure to view individual files and compare their headers.
# Takes in the flags and target directory for iteration.
def runIteration(flags : flags):
    # Open the path for the directory (We already know it exists)
    path = pathlib.Path(flags.filepath)
    # Get the largest header we're going to be working with, so we don't scan extra bytes.
    largest = getLargestHeader(flags)

    # for each child item in the directory,
    for child in path.iterdir():

        # If the child is a directory, recurse downward.
        if (child.is_dir()):
            prev = flags.filepath
            flags.filepath = child.absolute()
            runIteration(flags)
            flags.filepath = prev
        else:
            # if it's a file, try to open it.
            try:
                file = open(child, "rb")
                output = file.read(largest)

                # If the file matches any of our requested flags, tell the user.
                if (flags.executables):
                    for header in executableHeaders:
                        if (header.hexRepresent == output.hex()[:len(header.hexRepresent)]):
                            print("File: " + child.name + " matches description, is of type "+ header.description + "\nHex: " + output.hex())
                            
                if (flags.spreadsheets):
                    for header in spreadsheetHeaders:
                        if (header.hexRepresent == output.hex()[:len(header.hexRepresent)]):
                            print("File: " + child.name + " matches description, is of type "+ header.description + "\nHex: " + output.hex())
            except FileNotFoundError:
                # the file was moved? Tell the user. (This might also trigger when $ signs are in files, I'm not certain.)
                print("A file was deleted or moved: " + str(child.absolute()))

# Get the largest header that is requested.
# slight optimization function so we don't end up reading too many bytes.
def getLargestHeader(inFlags :flags):
    largest = 0
    # Iterate through all requested headers looking for the largest.
    if (inFlags.executables):
        for header in executableHeaders:
            if (largest < len(header.hexRepresent)):
                largest = len(header.hexRepresent)
    if (inFlags.spreadsheets):
        for header in executableHeaders:
            if (largest < len(header.hexRepresent)):
                largest = len(header.hexRepresent)
    # Return the largest.
    return largest



def formatHeaders():
    # Change the format of all headers to be in standardized hex, so they're easy to compare.
    for header in executableHeaders:
        header.hexRepresent = header.hexRepresent.replace(" ", "").lower()
    for header in spreadsheetHeaders:
        header.hexRepresent = header.hexRepresent.replace(" ", "").lower()

# Parse the command-line arguments.
def parseArgs():
    # Create a variable for flags.
    ourFlags = flags()

    # If we don't have the right number of arguments, print help and exit.
    if (len(sys.argv) != 3):
        printHelp()
        sys.exit(1)
    

    # Form a REGEX function to check if there are any repeats, or non-standard characters
    # in the input string.
    stringProper = re.match("^-(?:([(s|e|h)])(?!.*\1))*$", sys.argv[1])

    # If the input matches proper, the string is correct and we can operate on it.
    if (stringProper != None):
        if ('h' in sys.argv[1]):
            # If the user used the help flag, send the help message.
            printHelp()
            sys.exit(0)
        if ('s' in sys.argv[1]):
            # Switch s for spreadsheets
            ourFlags.spreadsheets = True
        if ('e' in sys.argv[1]):
            # Switch e for executables.
            ourFlags.executables = True

        if (os.path.isdir(sys.argv[2])):
            # if the input path is a directory, return it.
            ourFlags.filepath = sys.argv[2]
            return ourFlags
        else:
            # Otherwise, tell the user and send an error message.
            print("Filepath is not a directory!\n")
            printHelp()
            sys.exit(1)

        
    else:
        # If the args are wrong, send the help message.
        printHelp()
        sys.exit(1)



        

if __name__ == '__main__':
    formatHeaders()
    flag = parseArgs()
    runIteration(flag)





