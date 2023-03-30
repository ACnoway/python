import os
import codecs

list_name = []

path = os.path.join(os.getcwd(), "shuju")
print(path)


def get_files(dir_path):
    for file in os.listdir(dir_path):
        file_path = os.path.join(dir_path, file)
        if os.path.isdir(file_path):
            get_files(file_path)
        else:
            print(file_path)
            list_name.append(file_path)


get_files(path)
print(list_name)

# 输入文件的编码类型
encode_in = 'utf-8'

# 输出文件的编码类型
encode_out = 'gb2312'
for filename_in in list_name:
    # with codecs.open(filename=filename_in, mode='r', encoding=encode_in) as fi:
    fi = open(filename_in, 'r', encoding=encode_in)
    try:
        data = fi.read()
    except UnicodeDecodeError:
        fi = open(filename_in, 'r', encoding=encode_out)
        data = fi.read()
    filename_out = filename_in.replace("shuju", "dist")
    with open(filename_out, mode='w', encoding=encode_out) as fo:
        fo.write(data)
        fo.close()
