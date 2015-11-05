__author__ = 'Josh'
import os
import time
from os import path

folder = os.path.join('C:\\', 'Users', 'Josh', 'Desktop', 'Images')


def main():
    newName = input("Please input a name for your photos")
    print(folder)
    listOfFiles = getListOfFiles(folder)
    print(listOfFiles)
    renameFiles(listOfFiles, newName)


def getListOfFiles(folderPath):
    files = sorted(os.listdir(folderPath), key=lambda x: os.path.getctime(os.path.join(folderPath, x)))
    return files


def renameFiles(list, newName):
    for file in list:
        root, extension = os.path.splitext(file)
        os.rename(os.path.join(folder, file), os.path.join(folder, newName + ' #' + str(list.index(file)) + extension))

main()
