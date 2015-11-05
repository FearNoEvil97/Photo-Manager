__author__ = 'Josh'
import os
import time
from os import path

folder = os.path.join('C:\\', 'Users', 'Josh', 'Desktop', 'Images')


def main():
    print(folder)
    print(getListOfFiles(folder))


def getListOfFiles(folderPath):
    files = sorted(os.listdir(folderPath), key=lambda x: os.path.getctime(os.path.join(folderPath, x)))
    return files


def getTimeStamp(filePath):
    fileStats = os.stat(filePath)
    # return time.ctime(fileStats.st_ctime)
    return fileStats.st_ctime


def sortFilesByTimeStamp(fileList):
    return sorted(fileList, key=os.path.getctime)


main()
