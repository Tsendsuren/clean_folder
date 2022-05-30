import os
import shutil
from shutil import move

mydir = os.chdir('/home/tsende/Downloads') # indicate the folder you want cleaning

# this program will list all the items in the indicated directory.
with os.scandir(mydir) as root_dir:
    ext_list = []
    for entry in root_dir:
        files = entry.name
        filename, extension = os.path.splitext(files)
        filename = filename[0:]
        extension = extension[1:]
        ext_list.append(extension)
        new_ext_list = list(dict.fromkeys(ext_list))

# prints list of file extensions in your folder.
# print(new_ext_list)

# using remove() command, empty string is removed from list
# when a folder is present in your current directories, I can cause empty file extension
while('' in new_ext_list) :
    new_ext_list.remove('')

N = len(new_ext_list)

# create new directories for each file extension
for i in range(N):
    ext_name = new_ext_list[i]
    base_filename = 'Files' 
    dir_name = os.path.join(base_filename+'_'+ext_name)
    os.makedirs(dir_name, exist_ok=True)

src_path = os.listdir(mydir) # file list in the indicated directory.
file_dir = os.getcwd() # getting current working directory which includes your messy files


for i in range(N):
    # converting file extension into readable string by "endswith()" function.
    file_type = os.path.join('.'+new_ext_list[i]) 
    file_type = ('{}'.format(file_type))

    dest_path = os.path.join(file_dir+'/Files_'+new_ext_list[i]) # destination directory/folder where your mess will be sent to

    for file in src_path: 
        if file.endswith(file_type):
            shutil.move(os.path.join(file_dir,file), os.path.join(dest_path,file))
