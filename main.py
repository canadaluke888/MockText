import argparse
import os
from mock_data_generator.mock_data_generator import MockDataGenerator


def main():
    # Create the argument parser
    parser = argparse.ArgumentParser(description="Generate mock data text files with random words.")

    # Add arguments for number of files and words per file
    parser.add_argument('--num_files', type=int, help="Number of files to generate.")
    parser.add_argument('--words_per_file', type=int, help="Number of random words per file.")

    # Add the --init argument for initializing the database with words from the JSON file
    parser.add_argument('--init', action='store_true',
                        help="Initialize the word database with words from the JSON file.")

    # Parse the arguments
    args = parser.parse_args()

    # Initialize the mock data generator
    generator = MockDataGenerator()

    # Handle database initialization if --init is provided
    if args.init:
        print("Initializing the database with words from the JSON file...")
        generator.db.populate_word_database_from_json()  # Populate the database
        print("Database initialized.")
        return  # Exit after initialization

    # Generate mock data files if --num_files and --words_per_file are provided
    if args.num_files and args.words_per_file:
        generator.generate_mock_data_files(args.num_files, args.words_per_file)
    else:
        print("Please provide both --num_files and --words_per_file to generate files.")

    # Close the database connection
    generator.close()


if __name__ == "__main__":
    main()
