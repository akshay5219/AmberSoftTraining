filename = "example.txt"

with open(filename, "r") as file:
    text = file.read()

word_count = len(text.split())
print(f"The file '{filename}' contains {word_count} words.")
