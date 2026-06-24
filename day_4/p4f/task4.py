# Python script that creates a directory and moves text files into it.
# Should execute from the terminal with a directory name as an argument to the script

# Import sys module
# Import pathlib module
import sys
from pathlib import Path

# Get the command-line argument from the directory name to move files to
d_name = sys.argv[1]

# Make directory using that directory name from the comand-line argument
Path(d_name).mkdir(exist_ok=True)

# Move files from the current directory (txt files). Loop through all files c txt extension and move them to the newly created directory
for file in Path.cwd().glob("*.txt"):
    file.rename(Path(d_name) / file.name)


