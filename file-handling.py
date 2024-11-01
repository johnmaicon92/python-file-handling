"""
1. Exploring Python's OS Module
Objective: The goal of this assignment is to deepen your understanding of the OS module in Python.

Task 1: Directory Inspector:

Problem Statement: Create a Python script that lists all files and subdirectories in a given directory. Your script should prompt the user for the directory path and then display the contents.

Code Example:
    import os

    def list_directory_contents(path):
        # List and print all files and subdirectories in the given path

Expected Outcome: The script should correctly list all files and subdirectories in the specified directory. Handle exceptions for invalid paths or inaccessible directories.
"""

import os

def list_directory_contents(path):
    try:
        if not os.path.exists(path):
            print(f"Error: Directory '{path}' does not exist.")
            return

        for entry in os.scandir(path):
            if entry.is_file():
                print(f"File: {entry.name}")
            elif entry.is_dir():
                print(f"Directory: {entry.name}")
    except FileNotFoundError:
        print("The specified directory does not exist.")
    except PermissionError:
        print("You do not have permission to access this directory.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

