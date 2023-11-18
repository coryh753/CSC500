try:
    num1 = float(input("Enter an integer: "))
    num2 = float(input("Enter another integer: "))
    print("")
    print("Part One:")
    print(f"{num1} + {num2} = {num1 + num2}")
    print(f"{num1} - {num2} = {num1 - num2}")
    print("")
    print("Part 2:")
    print(f"{num1} * {num2} = {num1 * num2}")
    print(f"{num1} / {num2} = {num1 / num2}")

except ValueError:
    print("Hey, that's not an integer!")