import os
import pathlib 
import sys

Path = "F:\\Laptop coding\\Alfa TKG\\Alfa AI Team\\Lap code\\Task 2 EDA of files"
path = pathlib.Path(Path)

folders = []
for files in os.listdir(path):
    if os.path.isfile(files):
        pass
    elif files == ".git":
        pass
    else:
        folders.append(files)
        
folders_and_files_count = dict()
for folder in folders:
    images = list(path.glob(folder+'/*'))
    folders_and_files_count[folder] = images

for details in folders_and_files_count.keys():
    print(f'Folder name: {details}, Contains: {len(folders_and_files_count[details])} images')
    
# print(os.path.getsize(Path+"\\Img-data 1"))
dict_size = dict()
for i in folders_and_files_count.keys():
    Total_size = 0
    for j in folders_and_files_count[i]:
        Total_size = Total_size + os.path.getsize(j)
    dict_size[i] = Total_size
    
print(dict_size)