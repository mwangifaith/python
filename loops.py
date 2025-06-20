#while loops
number = 20

while number <= 25 :
   print(number)
   number += 1

   print()

   #decreamenting
count = 105
while count >= 100 :
   print("number is", count)
   count -= 1

print()

#Break and continue
a = 20
while a <= 25 :
   print(a)
   a += 1


counter = 35
while counter <= 40:
    if counter == 37:
        counter += 1
        continue
    print(counter)
    counter += 1

   #forloop
languages = ["python", "java", "c++", "PHP"]
for lang in languages:
            print(lang)

print()

for num in range(5):
    print(num)

    print()

for x in range(10,15):
    print(x)

    print()

for z in range(10,20,3):
    print(z)