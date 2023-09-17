# Project: Folder Difference Analyzer

## Objectives

The primary objective is to develop a Python tool that allows users to analyze and compare the file structures of two specified folders. The tool will perform a recursive scan of folders and files, and provide a detailed report of the differences between corresponding files, along with statistics and metadata about the operation.

---

## Features

1. **Folder Selection**: The user will provide paths to the folders to be compared.
2. **Recursive Analysis**: The tool will perform a recursive scan of folders and subfolders.
3. **File Comparison**: Corresponding files in the two structures will be compared.
4. **Log Files**: Generation of detailed log files stored in a dedicated folder.
5. **Statistics**: Provision of aggregate statistics related to the file differences.
6. **Execution Metadata**: Details such as date, time, and paths to compared folders will be included.

---

## Tools Used

- **Python**: The primary programming language, chosen for its readability, modularity, and extensive standard library.
- **Git**: For version control and collaboration.
- **Unit Testing Framework**: For writing and running unit tests.

---

## Project Structure and Justifications

The project structure is modularized into several files and modules to promote code readability, reusability, and ease of maintenance.

```plaintext
ProjectRoot/
|-- main.py                  (Entry point)
|-- directory_analyzer.py    (Directory analysis)
|-- file_comparator.py       (File comparison)
|-- log_writer.py            (Log writing)
|-- statistics.py            (Statistics calculation)
|-- utils/                   (Utility functions)
|   |-- __init__.py
|   |-- utility_functions.py
|-- tests/                   (Unit tests)
|   |-- __init__.py
|   |-- test_directory_analyzer.py
|   |-- test_file_comparator.py
|   |-- test_log_writer.py
|   |-- test_statistics.py
```

### Justifications:

- **Modularity**: Each component is isolated in a separate module to facilitate maintenance and testing.
- **Reusability**: Modules can be easily reused in other projects or contexts.
- **Collaboration**: A modularized structure facilitates collaboration between developers.
- **Scalability**: Adding new features is easier with a modular structure.

---

With this approach, the project will be well-organized and easily extendable, allowing for easier maintenance and the addition of new features over time.
