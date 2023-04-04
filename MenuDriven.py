import os

def search_file():
    filename = input("Enter the name of the file to search: ")
    if os.path.isfile(filename):
        print(f"The file '{filename}' exists in the current directory.")
    else:
        print(f"The file '{filename}' does not exist in the current directory.")

def create_file():
    filename = input("Enter the name of the file to create: ")
    with open(filename, "w") as file:
        print(f"The file '{filename}' has been created.")

def read_file():
    filename = input("Enter the name of the file to read: ")
    try:
        with open(filename, "r") as file:
            contents = file.read()
            print(contents)
    except FileNotFoundError:
        print(f"The file '{filename}' does not exist in the current directory.")

def write_file():
    filename = input("Enter the name of the file to write: ")
    if os.path.isfile(filename):
        mode = input("Enter 'a' to append or 'w' to overwrite: ")
        if mode == "a":
            with open(filename, "a") as file:
                text = input("Enter the text to append: ")
                file.write(text)
        elif mode == "w":
            with open(filename, "w") as file:
                text = input("Enter the text to write: ")
                file.write(text)
        else:
            print("Invalid mode.")
    else:
        print(f"The file '{filename}' does not exist in the current directory.")

def delete_file():
    filename = input("Enter the name of the file to delete: ")
    if os.path.isfile(filename):
        os.remove(filename)
        print(f"The file '{filename}' has been deleted.")
    else:
        print(f"The file '{filename}' does not exist in the current directory.")

while True:
    print("""
    1. Search a file
    2. Create a file
    3. Read a file
    4. Write to a file
    5. Delete a file
    6. Exit
    """)

    choice = input("Enter your choice: ")

    if choice == "1":
        search_file()
    elif choice == "2":
        create_file()
    elif choice == "3":
        read_file()
    elif choice == "4":
        write_file()
    elif choice == "5":
        delete_file()
    elif choice == "6":
        break
    else:
        print("Invalid choice.")
