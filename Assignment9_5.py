import os

def count_string_frequency(filename, target_string):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            frequency = content.count(target_string)
            return frequency
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return 0

def main():
    filename = input("Enter the filename: ")
    target_string = input("Enter the string to count: ")

    frequency = count_string_frequency(filename, target_string)

    print(f"The frequency of '{target_string}' in '{filename}' is: {frequency}")

if __name__ == "__main__":
    main()
