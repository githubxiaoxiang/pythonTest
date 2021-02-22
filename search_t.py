import os
from pathlib import Path

serarchPath = r'F:\pythonSpace\pythonTest'
str = 'p_t.png'
filePathArr = []
def search_file(path,str,flag=-1):  #flag传-1时为相对路径，否则为绝对路径
    for file in os.listdir(path):
        this_path = os.path.join(path,file)
        if os.path.isfile(this_path):
            if this_path.find(str)!=-1:
                if flag==-1:
                     this_path = this_path.replace(searchPath,'')[1:]
                     filePathArr.append(this_path)
                else:
                    filePathArr.append(this_path)
        else:
            search_file(this_path,str,flag)
    return filePathArr
print(search_file(serarchPath,str,1))

