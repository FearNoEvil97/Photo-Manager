__author__ = 'Josh'
import os
import tkinter
import tkinter as tk
from tkinter import filedialog

# Currently, the folder is determined programmatically. This method puts slashes between the terms.
# folder = os.path.join('C:\\', 'Users', 'Josh', 'Desktop', 'Images')


def main():
    # Collect a name from the user to name the files with
    #Get the root folder from the user.
    folder = getFolderPath()
    # Get a string from the user to use as a new file name.
    newName = input("Please input a name for your photos: ")
    # Get the list of reordered files
    listOfFiles = getListOfFiles(folder)
    # Rename the list of files with the new name
    renameFiles(listOfFiles, newName, folder)
    # Print a confirmation message!
    print("The images have been renamed!")

# This function returns all the listings in the directory(folderPath) and sorts them by the creation time using a dynamic(lambda) function.
def getListOfFiles(folderPath):
    files = sorted(os.listdir(folderPath), key=lambda x: os.path.getctime(os.path.join(folderPath, x)))
    return files


# This function renames all the files in the input list with the new name.
def renameFiles(list, newName, folder):
    for file in list:
        # Seperate the filename from the extension. We need the extension in the next line.
        root, extension = os.path.splitext(file)
        # Rename the source(1st argument) path/file with the value of the second argument. The second argument adds the path to the new name, the order number, and the collected extenstion.
        os.rename(os.path.join(folder, file), os.path.join(folder, newName + ' #' + str(list.index(file) + 1) + extension))


def getFolderPath():
    folderPath = ''
    print("Please select a folder:")
    root = tk.Tk()
    root.withdraw()
    folderPath = filedialog.askdirectory()
    while folderPath == "":
        print("You must select a folder. Try again.")
        folderPath = filedialog.askdirectory()
    return folderPath


main()
