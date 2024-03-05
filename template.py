import os
from pathlib import Path


print(os.getcwd())


file_list = [
    'Dockerfile',
    'requirements.txt',
    'src/__init__.py',
]

for file in file_list:
    file_path = Path(file)
    file_dir, file_name = os.path.split(file_path)
    if file_dir!='':
        os.makedirs(file_dir, exist_ok=True)

    if (not os.path.exists(file_path)) or (os.path.getsize(file_path)==0):
        with open(file_path,'w') as f:
            pass

    else:
        print("File is already present")