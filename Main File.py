__author__ = 'Josh'
import fileMgr

def main():
    # Collect a name from the user to name the files with
    #Get the root folder from the user.
    folder = fileMgr.getFolderPath()
    # Get a string from the user to use as a new file name.
    newName = input("Please input a name for your photos: ")
    # Get the list of reordered files
    listOfFiles = fileMgr.getListOfFiles(folder)
    # Rename the list of files with the new name
    fileMgr.renameFiles(listOfFiles, newName, folder)
    # Print a confirmation message!
    print("The images have been renamed!")


main()