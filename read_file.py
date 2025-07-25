import sys

try:
    with open('sample.txt', 'r') as file:
        print("Reading file content:")
        for line_number, line in enumerate(file, 1):
            print(f"line {line_number}: {line}", end='')
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.", file=sys.stderr)