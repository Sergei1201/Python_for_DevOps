# This is a Python test file
def greetings(first_name: str, last_name: str, age: int) -> str:
    return f"Greetings to you {first_name} {last_name}. You are {age} years old"

if __name__ == "__main__":
    print(greetings("John", "Doe", 25))