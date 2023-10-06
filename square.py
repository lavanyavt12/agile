def square(number):
    """Calculate the square of a number."""
    return number ** 2

if __name__ == "__main__":
    num = float(input("Enter a number: "))
    result = square(num)
    print(f"The square of {num} is {result}")
