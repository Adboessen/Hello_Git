# three data type at input

# string
phrase = input("Enter a string: ")
print("You said " + phrase)
print(f"You said {phrase}")

# float
someFloat = float(input("Enter an float: "))
print("YOu entered float: " + str(someFloat))
print(f"YOu entered float: {someFloat}")

# int
someInt = float(input("Enter a int: "))
print("You entered int: " + str(someInt))
print(f"You entered int: {someInt}")

# string interpolation is sweet
print(f"Do Python inline like this: {someFloat} * {someInt} = {someFloat * someInt}")
