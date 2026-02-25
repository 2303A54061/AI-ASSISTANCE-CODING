'''# Task1: Provide a Python snippet with a missing parenthesis in a print statement (e.g., print "Hello"). Use AI to detect and fix the syntax error
def greet():
	print("Hello, AI Debugging Lab!")

greet()'''

'''# Task2: Supply a function where an if-condition mistakenly uses = instead of ==. Let AI identify and fix the issue.
def check_number(n):
	if n == 10:
		return "Ten"
	else:
		return "Not Ten"

print(check_number(10))
print(check_number(5))'''

#Task3: Provide code that attempts to open a non-existent file and crashes. Use AI to apply safe error handling.
def read_file(filename):
	try:
		with open(filename, 'r') as f:
			return f.read()
	except FileNotFoundError:
		return "File not found."

print(read_file("nonexistent.txt"))

