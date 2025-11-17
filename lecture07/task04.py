# Function that returns a new list with all odd numbers removed
def remove_odd_numbers(numbers):
    even_list = []
    for n in numbers:
        if n % 2 == 0:
            even_list.append(n)
    return even_list

# Main program for testing
def main():
    original_list = [3, 6, 9, 12, 15, 18, 21, 24]
    filtered_list = remove_odd_numbers(original_list)

    print("Original list:", original_list)
    print("Even-number list:", filtered_list)

# Run the test program
main()