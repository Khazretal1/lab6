import os

def check_path(path):

    if os.path.exists(path):

        print(f"\nPath: {path}")

        print("Path exists!")

        print("Directory:", os.path.dirname(path))

        print("Filename:", os.path.basename(path))

    else:

        print("Error: The specified path does not exist.")

specified_path = input("Enter the file or directory path: ")

check_path(specified_path)