age = input("Print your age: ")
try:
    age = int(age)
    if age >= 18:
        print("beer")
    else:
        print("Coca-cola")
except ValueError:
    print("You have input a letter")