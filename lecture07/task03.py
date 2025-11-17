# Function that returns the sum of a list of integers
def sum_list(numbers):
    total = 0
    for n in numbers:
        total += n
    return total

# Main program for testing
def main():
    my_list = [3, 7, 10, -2, 5]
    result = sum_list(my_list)
    print("The sum of the list is:", result)

# Run the test program
main()