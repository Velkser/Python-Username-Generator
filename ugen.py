import argparse
import os
import sys

def parse_record(line):
    """
    Parses a single line of input file.

    Args:
        line (str): A line from the input file.

    Returns:
        list: A list containing the parsed fields [ID, forename, middle name, surname, department].

    Raises:
        ValueError: If the line does not contain exactly 5 fields separated by colons.
    """
    parts = line.strip().split(':')
    if len(parts) != 5:
        raise ValueError("Incorrect input format. Each line must have exactly 5 fields separated by colons.")
    return parts

def create_username(forename, middle_name, surname):
    """
    Generates a base username from the forename, middle name (if available), and surname.

    Args:
        forename (str): The forename of the user.
        middle_name (str): The middle name of the user (can be an empty string).
        surname (str): The surname of the user.

    Returns:
        str: The generated base username.
    """
    username = (forename[0] + (middle_name[0] if middle_name else '') + surname).lower()
    return username

def process_input_files(output_file, input_files):
    """
    Processes all input files and writes the generated data to the output file.
    Ensures usernames are unique by appending numbers if necessary.

    Args:
        output_file (str): The path to the output file.
        input_files (list): A list of paths to the input files.
    """
    user_data = []
    username_counter = {}

    for input_file in input_files:
        if os.path.exists(input_file):
            with open(input_file, 'r', encoding='utf-8') as file:
                for line in file:
                    if line.strip():  # Skip empty lines
                        user_data.append(parse_record(line))
        else:
            print(f"Warning: File {input_file} does not exist and will be skipped.", file=sys.stderr)

    with open(output_file, 'w', encoding='utf-8') as out_file:
        for user in user_data:
            user_id, forename, middle_name, surname, department = user
            base_username = create_username(forename, middle_name, surname)
            username = base_username
            counter = username_counter.get(base_username, 0)

            # Ensure the username is unique
            while username in username_counter:
                counter += 1
                username = f"{base_username}{counter}"

            username_counter[base_username] = counter
            username_counter[username] = 0

            out_file.write(f"{user_id}:{username}:{forename}:{middle_name}:{surname}:{department}\n")

def main():
    """
    Main function to parse command-line arguments and process the input files.
    """
    parser = argparse.ArgumentParser(description='Generate usernames from input files.')
    parser.add_argument('-o', '--output', required=True, help='Output file')
    parser.add_argument('input_files', nargs='+', help='Input files')

    try:
        args = parser.parse_args()

        if not args.output or not args.input_files:
            parser.print_help()
            sys.exit(1)

        process_input_files(args.output, args.input_files)
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        parser.print_help()
        sys.exit(1)

if __name__ == '__main__':
    main()
