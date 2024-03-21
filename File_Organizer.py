import os
import shutil as sh

#path = 'C:\DemoFolder'
#I have used a folder named demoFold in C drive. You can use any folder of your choice.
#for user input folder path, use the below line of code
#path = input("Enter the path:")
path = "/"
files = os.listdir(path)

for file in files:
    filename, extension = os.path.splitext(file)
    extension = extension[1:]

    if os.path.exists(path + '/' + extension):
        sh.move(path + '/' + file, path + '/' + extension + '/' + file)
    else:
        os.makedirs(path+'/'+extension)
        sh.move(path+'/'+file, path+'/' +extension+'/'+file)