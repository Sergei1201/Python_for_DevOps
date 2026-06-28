# Script for creating a function which builds a query string from any number of arguments and sorts them alphabetically

# Function that creates a query string (using keyword arguments kwargs)
def query_string(**kwargs) -> str:
    return '&'.join(f"{k}={v}" for k, v in sorted(kwargs.items())) # Capture arguments as a dictionary, sort key-value pairs alphabetically by the keys, concatenate items with join function using & symbol

# Input
print(query_string(category="books", genre="thriller", author="Stephen_King"))
print(query_string(name="John", last_name="Doe", age=25, occupation="web_designer"))



