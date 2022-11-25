import os

path = './'
filelist = os.listdir(path)
for file in filelist:
    if file == '.git':
        continue
    print(file)
    if os.path.isdir(path + file):
        ffilelist = os.listdir(path + file)
        for ffile in ffilelist:
            filelist.append(file + '/' + ffile)
        continue
    name, ext = file.split('.')
    if ext == "exe":
        continue
    f = open(path + file, "r", encoding="utf-8")
    print(f.readline())
