# src/my_module.py

# Greeting
def greet(name):
    return f"Hello, {name}!"

# Function to check if a number is even
def is_even(number):
    return number % 2 == 0

# Main part of the program
if __name__ == "__main__":
    name = input("Enter your name: ")
    print(greet(name))

    # Input a number
    number = int(input("Enter a number: "))

    # Check if the number is even
    if is_even(number):
        print(f"{number} is an even number.")
    else:
        print(f"{number} is an odd number.")

    # Loop to print numbers from 1 to 5
    print("Numbers from 1 to 5:")
    for i in range(1, 6):
        print(i)
