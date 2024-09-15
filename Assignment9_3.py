import os

def main():
   
    source_filename = input("Enter the name of the source file you want to copy from: ")
    
   
    if not os.path.exists(source_filename):
        print(f"Source file '{source_filename}' does not exist.")
        return

   
    destination_filename = "Demo.txt"
    
   
    if os.path.exists(destination_filename):
        print(f"File '{destination_filename}' already exists. Cannot create new.")
    else:
        
        with open(destination_filename, "x") as dest_file:
            print("New file created successfully!")

        
        with open(source_filename, "r") as source_file:
           
            data = source_file.read()

        
        with open(destination_filename, "w") as dest_file:
            dest_file.write(data)
        
        print(f"Contents copied from '{source_filename}' to '{destination_filename}' successfully.")

if __name__ == "__main__":
    main()
