# Python script that reads data from a csv file, processes it, calculates the total, shows some columns and saves data to a new file

# Import csv module
import csv
# Import sleep module for imitating delays
from time import sleep

# Process order by reading a csv file, calculate Total, show some columns and save results to a file

def process_csv() -> None:
     
    # Read the CSV
    print("Reading data from CSV...")
    sleep(3) # Delay for some time to show messages on the screen
    print("=" * 30) # For better formatting

    # Initialize an empty list for data read from the file
    order_data = []
    with open("orderdata_sample.csv", 'r') as file: # Open file for reading data
       csv_reader: object = csv.DictReader(file)
       # print(type(csv_reader))
       for row in csv_reader: # Read data from the file row by row

           # Convert string to numbers
           row["Quantity"] = int(row["Quantity"])
           row["Price"] = float(row["Price"])
           row["Freight"] = float(row["Freight"])

           # Calculate our total column
           row["Total"] = (row["Quantity"] * row["Price"]) + row["Freight"]

           # Append all data to the list
           order_data.append(row)
   # print(order_data)

        # Display some records with selected columns
    print(f"Displaying 20 first records with selected columns: ")
    sleep(3) # Delay for some time for the user to see the message
    print("=" * 90)

    # Select columns to display
    columns_selected: list = ["OrderID", "CustomerID", "Quantity", "Price", "Freight", "Total"]

    # Format the header
    header = "{:<12} {:<12} {:<10} {:<10} {:<10} {:<12}"
    print(header.format(*columns_selected)) # Passing a list to the format method with *
    print("-" * 90)

    # Print rows
    for order in order_data[:20]: # Print only 20 first records
                print(header.format(
                order["OrderID"],
                order["CustomerID"],
                order["Quantity"],
                order["Price"],
                order["Freight"],
                f"{order["Total"]:.2f}"
                ))

    # Save all data to a new CSV file
    print("-" * 90)
    print("Saving data to processed_data.csv file...")
    sleep(3) # Delay for some time for the user to see the message
    print("-" * 90)
    
    columns_to_save: list = ["OrderID", "CustomerID", "ManagerID", "Quantity", "Price", "Freight", "Total", "OrderDate", "ShippedDate"]
    # Write data to a new file
    with open("processed_data.csv", 'w', newline='') as file: # newline='' is the recommended param for CSV file according to the Python docs
          writer: object = csv.DictWriter(file, fieldnames=columns_to_save)
          writer.writeheader() # Writes header to the file 
          writer.writerows(order_data) # Write records to the file
    
    print(f"{len(order_data)} records have been writted to processed_data.csv")
    sleep(3) # Delay for some time for the user to see the message
    print(f"\nColumns in the file: ")
    for column in columns_to_save:
          print(f" --- {column}")

    print("=" * 90)
    print("\nThe process is complete...")
    print("=" * 90)


if __name__ == "__main__":
    process_csv()


