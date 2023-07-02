import os

path = './'
filelist = os.listdir(path)
print(filelist)
for file in filelist:
    chai = file.split('/')
    # chai = chai[len(chai) - 1]
    if os.path.isdir(path + file):
        if chai[len(chai) - 1][0] == '.':
            continue
        ffilelist = os.listdir(path + file)
        for ffile in ffilelist:
            filelist.append(file + '/' + ffile)
        continue
<<<<<<< HEAD
    name, ext = chai[len(chai) - 1].split('.')
    if ext != "txt":
=======
    name, ext = file.split('.')
    if ext == "exe":
>>>>>>> 54ecd946ce8ff7a4d821be7c66820a0f63f8f810
        continue
    print(file)
    f = open(path + file, "r", encoding="gbk")
    try:
        s = f.readlines()
        nf = open(path + file + ".new", "w", encoding="utf-8")
        nf.writelines(s)
    except UnicodeDecodeError:
        f.close()
