# Program that asks the user sales numbers of sold products from a store for each day of the week and keep those numbers as a list. 

# 1. Create a list of each day of the week
days_of_week: list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# 2. Get sales for each day
sales_list: list = [] # Empty for the beginning

# 3. Calculate the total of the week
for day in days_of_week:
    sale: float = float(input(f"Enter the sale for {day}: "))
    
    # Append each sale to the sales list
    sales_list.append(sale)

 # Total
total: float = sum(sales_list)
print(f"The total sales for the whole week: {total}")

# 4. Sort and print the results
sales_list.sort()
print("\nSales (in ascending order)")
for item in sales_list:
    print(item)






