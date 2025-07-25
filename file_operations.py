try:
    # Write initial data
    text = input("Enter text to write to the file: ")
    with open('output.txt', 'w') as file:
        file.write(text)
    print("Data written to output.txt.")

    # Append additional data
    more_text = input("Enter more text to add: ")
    with open('output.txt', 'a') as file:
        file.write(more_text)
    print("Data added to output.txt.")

    # Show the content
    with open('output.txt', 'r') as file:
        print("Content of output.txt:")
        print(file.read())

except:
    print("Something went wrong with the file.")