age = int(input("Enter your age: "))

if age <= 12:
    category = "Child"
elif age > 12 and age <= 19:
    category = "Teenager"
elif age > 19 and age <= 59:
    category = 'Adult'
else:
    category = 'Senior'

print(f"You are a {category}.")