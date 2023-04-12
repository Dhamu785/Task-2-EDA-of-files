import os
import pathlib 

Path = "F:\\Laptop coding\\Alfa TKG\\Alfa AI Team\\Lap code\\Task 2 EDA of files"
path = pathlib.Path(Path)

folders = []
for files in os.listdir(path):
    if os.path.isfile(files):
        continue
    else:
        folders.append(files)
        
folders_and_files_count = dict()
for folder in folders:
    images = len(list(path.glob(folder+'/*')))
    folders_and_files_count[folder] = images

for details in folders_and_files_count.keys():
    print(f'Folder name: {details}, Contains: {folders_and_files_count[details]} images')