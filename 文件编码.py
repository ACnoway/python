import os

path = './'
filelist = os.listdir(path)
for file in filelist:
    print(file)
    if file == '.git':
        continue
    if os.path.isdir(path + file):
        ffilelist = os.listdir(path + file)
        for ffile in ffilelist:
            filelist.append(file + '/' + ffile)
        continue
    f = open(path + file, "r")
