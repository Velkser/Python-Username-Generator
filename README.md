# Python-Username-Generator
This project is a Python application for generating usernames based on input records. It includes a command-line tool and unit tests to ensure the functionality of the username generation process. 

## Project Structure

- `ugen.py`: Contains the main logic for generating usernames from user records.
- `test_ugen.py`: Contains unit tests for `ugen.py`.
- `conftest.py`: Contains pytest configuration and fixtures for setting up and tearing down test data.
- `test.py`: A script for running pytest with custom options, such as specifying the test data file.

## Installation

To set up the project, you will need to install the necessary Python packages. It is recommended to use a virtual environment for this purpose.

1. **Create and activate a virtual environment:**

   ```sh
   python -m venv .venv
   source .venv/bin/activate  # Linux/MacOS
   .\.venv\Scripts\activate   # Windows
   ```

2. **Install the required packages:**

Use the requirements.txt file to install all necessary dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage
### Command-Line Tool

To run the username generator script (`ugen.py`), you need to provide an output file and one or more input files. The input files should contain user records, and the output file will contain the generated usernames along with the original records.

Example usage:

 ```sh
   python3 ugen.py --output output_file.txt input_file1.txt input_file2.txt

   ```
## Testing

To run the unit tests for the project, use the test.py script. This script uses pytest to run tests with the specified test data file.

Example usage:

 ```sh
   python3 test.py ugen.py test_data.txt

   ```

## Generating Reports

Test results are automatically saved in a JUnit XML report file named report.xml. You can review this file to analyze the test results.

Example usage:

 ```sh
   python3 test.py ugen.py test_data.txt

   ```

## Requirements

The project requires the following Python packages, listed in requirements.txt:

`pytest`: For running the unit tests.

You can install these dependencies using the command:

 ```sh
   pip install -r requirements.txt

   ```
   
## End.