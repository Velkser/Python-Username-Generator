import pytest
import os

def pytest_addoption(parser):
    """
    Adds a custom command line option for specifying the test data file.

    Args:
        parser (argparse.ArgumentParser): The argument parser object used by pytest.
    """
    parser.addoption("--test_data", action="store", default="test_data.txt", help="Path to the test data file")

def setup_test_data(test_data_path):
    """
    Sets up the necessary input files based on the test data file.

    Args:
        test_data_path (str): The path to the test data file.
    """
    with open(test_data_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if line and not line.startswith('#'):
                file_name, data = line.split(':', 1)
                with open(file_name, 'a', encoding='utf-8') as data_file:
                    data_file.write(f'{data}\n')

def cleanup_test_data(test_data_path):
    """
    Cleans up files that were created during the test setup.

    Args:
        test_data_path (str): The path to the test data file.
    """
    with open(test_data_path, 'r', encoding='utf-8') as file:
        files_to_remove = set()
        for line in file:
            line = line.strip()
            if line and not line.startswith('#'):
                file_name = line.split(':', 1)[0]
                files_to_remove.add(file_name)
                
    for file in files_to_remove:
        if os.path.exists(file):
            os.remove(file)

@pytest.fixture(scope='module')
def setup_files(pytestconfig):
    """
    Pytest fixture to set up and tear down test files.

    Args:
        pytestconfig: Pytest configuration object to access command line arguments.
    """
    test_data_path = pytestconfig.getoption('test_data')
    setup_test_data(test_data_path)
    yield
    cleanup_test_data(test_data_path)
