# File Creation and Writing
with open('my_file.txt', 'w') as file:
    file.write("Hello, this is line 1.\n")
    file.write("This is line 2 with a number: 42\n")
    file.write("Line 3 is the final line.\n")

# Step 2: File Reading and Display
with open('my_file.txt', 'r') as file:  # Opens the file in read mode
    content = file.read()  # Reads all the content from the file
    print("File Contents:\n", content)  # Prints the content to the console

# Step 3: File Appending
with open('my_file.txt', 'a') as file:  # Opens 'my_file.txt' in append mode
    file.write("This is appended line 1.\n")  # Adds a new line to the end of the file
    file.write("Appending line 2: another number, 100.\n")  # Adds another line with a number
    file.write("Final appended line.\n")  # Adds the final line

# Step 4: Error Handling
try:
    # File Creation and Writing
    with open('my_file.txt', 'w') as file:
        file.write("Hello, this is line 1.\n")
        file.write("This is line 2 with a number: 42\n")
        file.write("Line 3 is the final line.\n")

    # File Reading and Display
    with open('my_file.txt', 'r') as file:
        content = file.read()
        print("File Contents:\n", content)

    # File Appending
    with open('my_file.txt', 'a') as file:
        file.write("This is appended line 1.\n")
        file.write("Appending line 2: another number, 100.\n")
        file.write("Final appended line.\n")

except FileNotFoundError:
    print("Error: The file was not found.")
except PermissionError:
    print("Error: You do not have permission to access this file.")
finally:
    print("File handling operation completed.")
