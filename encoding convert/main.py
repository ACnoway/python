import os

list_name = []

path = os.getcwd()
out_path = os.path.join(os.getcwd(), "out")
try:
    os.mkdir(out_path)
except FileExistsError:
    pass
print(out_path)

# 要统一转换成的编码
print("choose one")
print("1. utf-8")
print("2. gb2312")
print("please input: ")
encodes = ['utf-8', 'gb2312']
encode_in = ""
encode_out = encodes[int(input()) - 1]
if encode_out == 'utf-8':
    encode_in = 'gb2312'
else:
    encode_in = 'utf-8'
print(encode_out)


def get_files(dir_path, second):
    global encode_in, encode_out
    for file in os.listdir(dir_path):
        file_path = os.path.join(dir_path, file)
        if os.path.isdir(file_path):
            second = os.path.join(second, file)
            print(os.path.join(out_path, second))
            try:
                os.mkdir(os.path.join(out_path, second))
            except FileExistsError:
                pass
            get_files(file_path, second)
        else:
            print(file)
            fi = open(file_path, 'r', encoding=encode_in)
            try:
                data = fi.read()
            except UnicodeDecodeError:
                fi = open(file_path, 'r', encoding=encode_out)
                data = fi.read()

            filename_out = os.path.join(out_path, os.path.join(second, file))
            with open(filename_out, mode='w', encoding=encode_out) as fo:
                fo.write(data)
                fo.close()

            list_name.append(file_path)


get_files(path, "")
