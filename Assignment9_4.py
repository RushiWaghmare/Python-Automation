import os

def main():
   
    file1 = input("Enter the name of the first file: ")
    file2 = input("Enter the name of the second file: ")

    
    if not (os.path.exists(file1) and os.path.exists(file2)):
        print("Both files must exist for comparison.")
        return

    
    try:
        with open(file1, "r") as f1, open(file2, "r") as f2:
            content1 = f1.read()
            content2 = f2.read()
    except Exception as e:
        print(f"An error occurred: {e}")
        return

   
    if content1 == content2:
        print("Success: Both files have the same contents.")
    else:
        print("Failure: Contents of both files are different.")

if __name__ == "__main__":
    main()
