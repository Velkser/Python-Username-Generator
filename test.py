import pytest
import sys
import os

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python3 test.py ugen.py test_data.txt")
        sys.exit(1)

    test_data_file = sys.argv[2]

    #! Debug information
    # print(f"Python version: {sys.version}")
    # print(f"Current directory: {os.getcwd()}")
    # print(f"Test data file path: {os.path.abspath(test_data_file)}")
    # print(f"File exists: {os.path.isfile(test_data_file)}")

    # Ensure the test_data_file exists
    if not os.path.isfile(test_data_file):
        print(f"Test data file '{test_data_file}' not found.")
        sys.exit(1)

    # Run pytest with the test data file as an option
    pytest_args = [
        '-v', 
        '--tb=short', 
        f'--test_data={test_data_file}', 
        'test_ugen.py', 
        '--junitxml=report.xml'
    ]
    sys.exit(pytest.main(pytest_args))
