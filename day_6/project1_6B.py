import os # OS module to handle directores
from datetime import datetime # For working with date and time
import logging # For working with logging

# Input of CSV files according to the task instructions
list_of_csv = ["data1.csv", "data2.csv", "data3.csv", "data4.csv", "data5.csv", "data6.csv", "data7.csv", "data99.csv", "data10.csv"]

# Logging setup according to the task instructions
logging.basicConfig(filename="logs.txt" , level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


# Make directory for output if it doesn't exist
os.makedirs("output_files", exist_ok=True)

# Looping through the list of CSV files and using try .. except as well to handle exceptions if a file has not been found for example
for file in list_of_csv:
    try:
        if not os.path.exists(file): # Path to the file does not exist
            raise FileNotFoundError(f"The file {file} has not been found")

        # Creating output (timestamp, filename and content of each file)
        output_files = f"output_files/{datetime.now().strftime('%Y%m%d_%H%M%s')}_{file.replace('.csv', '.txt')}" # Replace format to txt according to instructions
        # Write info into file on each iteration
        with open(file, 'r') as source, open(output_files, 'w') as destination:
            destination.write(source.read()) # Reading info from source files and writing the content to output files on each iteration

        # Logging for each operation
        logging.info(f"Copied '{file}' to '{output_files}' successfully")
        print(f"{file} has been copied")

    # Handle exceptions by writing info to log files according to the task instructions
    except FileNotFoundError as e:
        logging.error(f"{file} has not been found")
        print(f"File {file} hasn't been found")

    # Handling other exceptions which we might not know about
    except Exception as e:
        logging.error(f"Can't copy {file} due to the error {str(e)}")
        print(f"File {file} error {str(e)}")

    

