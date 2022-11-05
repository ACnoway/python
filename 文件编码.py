import os

path = './'
filelist = os.listdir(path)
for file in filelist:
    f = open(path + file, "r")
    
