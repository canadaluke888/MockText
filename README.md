## Optimized Mock Text File Generator

This version of the mock text generator uses SQLite for a faster way of getting the random words from the large dataset

## Prerequisites
- **Python 3.9+**
- **Install dependencies:** `pip install -r requirements.txt`

## Usage

Use the `python` command for Windows and the `python3` command for Linux.

1. **Setting up the database:** `python3 main.py --init`
2. **Generating mock data files:** `python3 main.py --num_files <number of files to generate> --words_per_file <number of words per text file>`
3. **Extracting the output data:** The outputted files will be contained in a directory called 'output' in the working directory of the main application.
