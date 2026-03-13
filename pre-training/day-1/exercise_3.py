def print_multiplication_table(n):
    print(f"\nMultiplication table for {n}:")
    for i in range(1, 13):
        result = n * i
        print(f"{n:>3} x {i:>2} = {result:>4}")


while True:
    try:
        number = int(input("Enter a number between 1 and 12: "))
        if 1 <= number <= 12:
            break
        else:
            print("Please try again number must be between 1 and 12.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

print_multiplication_table(number)

print("\n--- Bonus: All tables from 1 to 12 ---")
for n in range(1, 13):
    print_multiplication_table(n)
