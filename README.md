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


2. **Install the required packages:**

Use the requirements.txt file to install all necessary dependencies:
    ```sh
    pip install -r requirements.txt

