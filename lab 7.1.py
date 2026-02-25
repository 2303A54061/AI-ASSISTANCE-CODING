#Task1: Provide a Python snippet with a missing parenthesis in a print statement (e.g., print "Hello"). Use AI to detect and fix the syntax error.
def greet():
	print("Hello, AI Debugging Lab!")
greet()

# Task2: Supply a function where an if-condition mistakenly uses = instead of ==. Let AI identify and fix the issue.
def check_number(n):
    if n == 10:
        return "Ten"
    else:
        return "Not Ten"


# Task3: Provide code that attempts to open a non-existent file and crashes. Use AI to apply safe error handling.
def read_file(filename):
    try:
        with open(filename, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return f"File '{filename}' not found."

print(read_file("nonexistent.txt"))

# Task4: Give a class where a non-existent method is called (e.g., obj.undefined_method()). Use AI to debug and fix.
class Car:
	def start(self):
		return "Car started"
my_car = Car()
print(my_car.start())



#Task5: Provide code that adds an integer and string ("5" + 2) causing a TypeError. Use AI to resolve the bug.
def add_five(value):
	return int(value) + 5
print(add_five("10"))