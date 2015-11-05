__author__ = 'Josh'
import os
import time
from os import path

folder = os.path.join('C:\\', 'Users', 'Josh', 'Desktop', 'Images')


def main():
    newName = input("Please input a name for your photos")
    print(folder)
    print(getListOfFiles(folder))


def getListOfFiles(folderPath):
    files = sorted(os.listdir(folderPath), key=lambda x: os.path.getctime(os.path.join(folderPath, x)))
    return files


main()
