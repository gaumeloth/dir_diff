# Import libraries and modules
# hashlib is used for generating file hashes
# difflib is used for text-based file comparison
import hashlib
import difflib

# Function to generate a hash for a specific file
# This function takes a file path and an optional hashing algorithm as inputs.
# The default hashing algorithm is MD5.
def hash_file(file_path, algorithm='md5'):
    try:
        # Open the file in binary mode and read its content
        with open(file_path, 'rb') as f:
            bytes = f.read()
            
        # Generate the hash using the specified algorithm
        if algorithm == 'md5':
            hash_object = hashlib.md5(bytes)
        elif algorithm == 'sha1':
            hash_object = hashlib.sha1(bytes)
        elif algorithm == 'sha256':
            hash_object = hashlib.sha256(bytes)
        else:
            return 'Invalid algorithm'
        
        # Convert the hash object to a hexadecimal digest string
        file_hash = hash_object.hexdigest()
        return file_hash
    except Exception as e:
        # Return any exception that occurs as a string
        return str(e)

# Function to compare the hashes of two files
# This function takes the paths of two files and an optional hashing algorithm as inputs.
# It returns True if the files are identical (based on their hashes), otherwise False.
def compare_files(file1_path, file2_path, algorithm='md5'):
    hash1 = hash_file(file1_path, algorithm)
    hash2 = hash_file(file2_path, algorithm)
    return hash1 == hash2

# Function to perform text-based diff between two files
# This function takes the paths of two files as inputs and returns a list of differences between them.
# It uses Python's difflib module to perform the comparison.
def text_diff(file1_path, file2_path):
    try:
        # Open the files in text mode and read their lines
        with open(file1_path, 'r') as f1, open(file2_path, 'r') as f2:
            lines1 = f1.readlines()
            lines2 = f2.readlines()
            
        # Create a Differ object and perform the comparison
        differ = difflib.Differ()
        diff = list(differ.compare(lines1, lines2))
        return diff
    except Exception as e:
        # Return any exception that occurs as a string
        return str(e)
