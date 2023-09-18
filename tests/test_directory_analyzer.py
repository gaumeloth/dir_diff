import pytest
from src.directory_analyzer import scan_directory, filter_files

# Test per la funzione scan_directory
def test_scan_directory_valid_path():
    result = scan_directory('.')
    assert isinstance(result, list), f"Expected list, got {type(result)}"
    
def test_scan_directory_invalid_path():
    result = scan_directory('invalid_path')
    assert "No such file or directory" in result

# Test per la funzione filter_files
@pytest.mark.parametrize("file_list, directory_path, extension, min_size, max_size, modified_after, expected", [
    (['file1.txt', 'file2.py'], '.', '.txt', None, None, None, ['file1.txt']),
    (['file1.txt', 'file2.py'], '.', '.py', None, None, None, ['file2.py']),
    (['file1.txt', 'file2.py'], '.', None, 0, 100, None, ['file1.txt', 'file2.py']),
])
def test_filter_files(file_list, directory_path, extension, min_size, max_size, modified_after, expected):
    result = filter_files(file_list, directory_path, extension, min_size, max_size, modified_after)
    assert result == expected, f"Expected {expected}, got {result}"
