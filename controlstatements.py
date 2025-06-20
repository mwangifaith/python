#Program1

age = int(input("Enter your age: "))

if age >=18:
    print("you are a voter")
else:
    print("you are not a voter")


#prog2
temperature = float(input("Enter current room temperature e.g 23.0: "))
if temperature > 25.0:
    print("it is too hot")
elif temperature < 25.0:
    print("it is too cold")
else:
    print("normal temperature")

    print()

#prog3
first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
third = int(input("Enter third number: "))

if first > second or first > third:
    print(first, "is the largest number")
elif second > third or second > first:
    print(second, "is the largest number")
else:
    print(third, "is the largest number")