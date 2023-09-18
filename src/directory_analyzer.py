# Import libraries and modules
# os module is used for interacting with the operating system
# time module is used for getting file modification times
import os
import time

# Function to scan a directory and return a list of files and subdirectories
# This function takes a directory path as input and returns a list of all files and subdirectories within it.
def scan_directory(directory_path):
    try:
        # os.listdir() returns a list containing the names of the entries in the directory given by path.
        entries = os.listdir(directory_path)
        return entries
    except Exception as e:
        # Return any exception that occurs as a string
        return str(e)

# Function to filter files based on multiple criteria
# This function takes a file list and several optional parameters for filtering.
# extension: to filter by file extension (e.g., '.txt')
# min_size and max_size: to filter files that are within a specified size range
# modified_after: to filter files that were modified after a certain time
def filter_files(file_list, directory_path, extension=None, min_size=None, max_size=None, modified_after=None):
    filtered_files = []
    for file in file_list:
        # Create a full file path by joining the directory path and the file name
        file_path = os.path.join(directory_path, file)
        
        # Check if the file extension matches the criteria
        if extension and not file.endswith(extension):
            continue
        
        # Check if the file size matches the criteria
        if min_size or max_size:
            # os.path.getsize() returns the size of the file in bytes
            file_size = os.path.getsize(file_path)
            if min_size and file_size < min_size:
                continue
            if max_size and file_size > max_size:
                continue
        
        # Check if the file modification time matches the criteria
        if modified_after:
            # os.path.getmtime() returns the time of last modification of path
            file_time = os.path.getmtime(file_path)
            if file_time < modified_after:
                continue
        
        # If the file meets all the criteria, add it to the filtered_files list
        filtered_files.append(file)
    return filtered_files
