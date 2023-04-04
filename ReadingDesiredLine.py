filename = "example.txt"
line_number = 5  # change this to the line number you want to read

with open(filename, "r") as file:
    lines = file.readlines()

if line_number <= len(lines):
    print(lines[line_number-1])
else:
    print("Line number out of range.")