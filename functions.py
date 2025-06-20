#1. built-in functions/ standard library functions
x = max(67, 89, 90, 23, 76, 45)
print("the maximum number is", x)


y = min(67, 89, 90, 23, 76, 45)
print("the minimum number is", y)


z= pow(2, 3)
print("the power of 2 is", z)

#2. user defined functions
def greeting():
    print("Hello, world!")

greeting()  #calling a function


def school():
    print("My coding school is Emobilis")

school()



#parameter and arguments
def add(num1, num2):
    print(num1 + num2)

add(5, 10)
add(20, 10)

def student(fullname, course, gender):
    print(fullname, course, gender)

student("Mary Mbotella", "MIT", "Female")
student("James Kamau", "Software Development", "Male")
student("Maurice Kyles", "Data SCience", "Male")
student("Reina Wedny", "Software Development", "Female")

print()



#python program that displays details of 5 employees at Fintech using parameters and argument. display fullname, email address, age, position,salary( as a decimal value), marriage status
def employee(fullname, emailaddress, age, position, salary,marital_status):
    print(fullname, emailaddress, age, position, salary, marital_status)

employee("James Kyles", "Software Development", 30, "CEO", 30000.00, "married")
employee("James Kyles", "Software Development", 30, "CEO", 30000.00, "married")
employee("James Kyles", "Software Development", 30, "CEO", 30000.00, "married")
employee("James Kyles", "Software Development", 30, "CEO", 30000.00, "married")
employee("James Kyles", "Software Development", 30, "CEO", 30000.00, "married")
