input_age = int(input("Enter your age: "))

if input_age >= 18:
    print("You can vote!")
elif input_age > 0 and input_age <= 17:
    print("Too young to vote.")
else:
    print("You are a time traveller.")