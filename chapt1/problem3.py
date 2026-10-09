import os
# specify the directory path you want to list
directory_path = '/'
# list all files and directories in the specified path
contents = os.listdir(directory_path)
# print the contents of the directory
for item in contents:
    print(item)