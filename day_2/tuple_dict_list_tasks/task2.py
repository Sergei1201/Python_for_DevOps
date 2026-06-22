# Program that clears a list of IP-addresses
# There's a list of unfiltered IP-addresses. Write a script that strips all the spaces from both sides of strings, strips out the localhost address from the list, empty elements, and duplicates. The result should be sorted alphabetically.

# Unfiltered list of IP-addresses.
list_of_ips: str = [" 192.168.1.1 ", "", "127.0.0.1", " 192.168.1.2 ", "0.0.0.0 ", "10.0.0.1 ", "0.0.0.0"]

# Test the output
print(f"The original list of IPS: {list_of_ips}")

# First of all, strip all spaces
stripped_ips: list = [ip.strip() for ip in list_of_ips]

# Test the output
print(f"The stripped list of IPs: {stripped_ips}")

# Then remove the localhost and empty strings from the stripped list
filtered: list = [ip for ip in stripped_ips if ip and ip != "127.0.0.1"]

# Test the output
print(f"Filtered list of IPs: {filtered}")

# Remove duplicates (convert to set because their elements are unique and then back to a list)
unique_ips: list = list(set(filtered))

# Test the output
print(f"Unique list of IPs: {unique_ips}")

# Sort the unique list of IPs in the ascend order (the sorted function returns a new list and does not modify the original one)
sorted_list_of_ips: list = sorted(unique_ips)

# Test the output
print(f"Sorted list of IPs: {sorted_list_of_ips}")

