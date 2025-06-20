courses = ["Fullstack", "DataScience", "CyberSecurity"]
print(courses)

#Accessing an element
print(courses[2])

#looping through an array
for course in courses:
    print(course)

#adding a new element
courses.append("UI/UX")
print(courses)

#removing an element
courses.remove("Fullstack")
print(courses)