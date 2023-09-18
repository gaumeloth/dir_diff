import pytest
from src.file_comparator import hash_file, compare_files, text_diff

# Test per la funzione hash_file
def test_hash_file_valid_file():
    result = hash_file('some_valid_file_path')
    assert len(result) == 32, f"Expected 32 characters long MD5 hash, got {len(result)}"

def test_hash_file_invalid_file():
    result = hash_file('invalid_file_path')
    assert "No such file or directory" in result

# Test per la funzione compare_files
def test_compare_files_identical():
    result = compare_files('file1_path', 'file2_path')
    assert result == True

def test_compare_files_different():
    result = compare_files('file1_path', 'file3_path')
    assert result == False

# Test per la funzione text_diff
def test_text_diff_identical():
    result = text_diff('file1_path', 'file2_path')
    assert result == []

def test_text_diff_different():
    result = text_diff('file1_path', 'file3_path')
    assert len(result) > 0
