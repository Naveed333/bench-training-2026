name = "Naveed"
age = 25
drinks_coffee = False
salary = 75000.0

print(f"My name is {name}, I am {age} years old, I drink coffee: {drinks_coffee}, and my salary is Rs. {salary}.")

retirement_age = 60
years_until_retirement = retirement_age - age
print(f"Years until retirement: {years_until_retirement}")

cups_per_day = 3
price_per_cup = 150
weekly_coffee_budget = cups_per_day * price_per_cup * 7
if drinks_coffee:
    print(f"Weekly coffee budget: Rs. {weekly_coffee_budget}")
else:
    print("No coffee budget needed.")
