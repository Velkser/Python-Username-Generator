import pytest
from ugen import parse_record, create_username, process_input_files
import os

def test_parse_record():
    """
    Tests the parse_record function.

    Validates that the function correctly parses various input lines and handles errors for invalid lines.

    Raises:
        AssertionError: If the function does not behave as expected.
    """
    assert parse_record('1234:Jozef:Miloslav:Hurban:Legal') == ['1234', 'Jozef', 'Miloslav', 'Hurban', 'Legal']
    assert parse_record('4563:Pista::Hufnagel:Sales') == ['4563', 'Pista', '', 'Hufnagel', 'Sales']
    with pytest.raises(ValueError):
        parse_record('incorrect:line:format')
    with pytest.raises(ValueError):
        parse_record('1234:Too:Many:Fields:In:This:Line:Legal')

def test_create_username():
    """
    Tests the create_username function.

    Validates the username generation based on provided names.

    Raises:
        AssertionError: If the function does not produce expected usernames.
    """
    assert create_username('Jozef', 'Miloslav', 'Hurban') == 'jmhurban'
    assert create_username('Milan', 'Rastislav', 'Stefanik') == 'mrstefanik'
    assert create_username('Pista', '', 'Hufnagel') == 'phufnagel'

def test_process_input_files(setup_files):
    """
    Tests the process_input_files function to ensure correct processing and output.

    Args:
        setup_files: Fixture to set up and clean up test files.
    
    Raises:
        AssertionError: If the function does not produce the expected output.
    """
    input_files = ['input_file1.txt', 'input_file2.txt']
    output_file = 'output_file.txt'

    process_input_files(output_file, input_files)

    with open(output_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        assert len(lines) == 5
        assert '1234:jmhurban:Jozef:Miloslav:Hurban:Legal\n' in lines
        assert '4567:mrstefanik:Milan:Rastislav:Stefanik:Defence\n' in lines
        assert '4563:jmurgas:Jozef::Murgas:Development\n' in lines
        assert '1111:phufnagel:Pista::Hufnagel:Sales\n' in lines
        assert '4563:phufnagel1:Pista::Hufnagel:Sales\n' in lines

def test_process_input_files_with_incorrect_data(setup_files):
    """
    Tests the process_input_files function with incorrect data to ensure proper error handling.

    Args:
        setup_files: Fixture to set up and clean up test files.

    Raises:
        ValueError: If the function does not handle incorrect data gracefully.
    """
    input_files = ['incorrect_file.txt']
    output_file = 'output_file.txt'

    with pytest.raises(ValueError):
        process_input_files(output_file, input_files)
