__author__ = 'Josh'
import os
import tkinter as tk
from tkinter import filedialog

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
    root = tk.Tk()
    root.withdraw()
    folderPath = filedialog.askdirectory()
    return folderPath
