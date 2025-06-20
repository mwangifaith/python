#A python program that checks whether a number is even or odd
num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))




#A python prog that checks whether a letter is a vowel or a consonant
letter = input("Enter a letter: ").lower()
if letter in ['a', 'e', 'i', 'o', 'u']:
    print(letter, "is a vowel")
else:
    print(letter, "is not a vowel")






#A python program that returns the perimeter of a rectangle
def calculate_rectangle_perimeter(length, width):
  """
  Calculates the perimeter of a rectangle.

  Args:
    length: The length of the rectangle.
    width: The width of the rectangle.

  Returns:
    The perimeter of the rectangle.
  """
  perimeter = 2 * (length + width)
  return perimeter

if __name__ == "__main__":
  try:
    # Get input from the user for length and width
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))

    # Calculate the perimeter using the function
    perimeter_result = calculate_rectangle_perimeter(length, width)

    # Display the result
    print(f"The perimeter of the rectangle with length {length} and width {width} is: {perimeter_result}")

  except ValueError:
    print("Invalid input. Please enter numerical values for length and width.")

