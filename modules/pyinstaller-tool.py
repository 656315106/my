import os
import shutil
os.chdir(os.path.dirname(__file__))
command = input("enter file :")
command += " -F" #打包为单个文件

#如果有ico文件 作为图标打包
for i in os.listdir("."):
    if i[-4:] == ".ico":
        command += " -i " + i
        break


_file = command.split()[0]

dirname  = os.path.dirname(_file)
filename = os.path.basename(_file)
filename_no_ext,ext = os.path.splitext(filename)
exefile = filename_no_ext+".exe"

os.system("pyinstaller %s"%command)

try:
    shutil.move("dist\\"+exefile,exefile)
except:pass

try:
    shutil.rmtree("dist")
except:pass

try:
    shutil.rmtree("build")
except:pass

try:
    shutil.rmtree("__pycache__")
except:pass

try:
    os.remove(filename_no_ext+".spec")
except:pass
