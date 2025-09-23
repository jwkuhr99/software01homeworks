numbers = []

while True:
    user_input = input("Enter a number (or enter nothing to finish): ")
    if user_input == "":
        break
    number = float(user_input)
    numbers.append(number)

numbers.sort(reverse=True)

print("Top five greatest numbers: ")
for num in numbers[:5]:
    print(num)