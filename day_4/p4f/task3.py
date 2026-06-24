# Task 3. Using the pathlib module to create files and directories

# INSTRUCTIONS
# 1. Create a new directory
# 2. In the new directory add new files, for examples 3 text files and file image file
# 3. Create one more directory inside the first one
# 4. Move the image file into the new directory

# Import Path modules
from pathlib import Path

# Home method
home = Path.home()

# Create a path to the new directory
my_folder = home / "my_folder"

# Create directory if does not exist
if not my_folder.exists():
    my_folder.mkdir()

# Create a new file
file1 = my_folder / "file1.txt"
file1.touch()
(my_folder / "file2.txt").touch()
my_folder.joinpath("image.png").touch()

# Create a directory to move files to
(my_folder / "images").mkdir(exist_ok=True)

# Moving files
for f in my_folder.glob('*.png'):
    path_destination = Path(my_folder /"images") / f.name
    f.replace(path_destination)


