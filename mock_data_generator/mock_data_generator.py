from database.database import WordDatabase
from tqdm import tqdm
import os

class MockDataGenerator:
    def __init__(self, db_path="words.db", output_dir="output"):
        self.db = WordDatabase(db_path)
        self.output_dir = output_dir
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def generate_random_words(self, count):
        """Generate 'count' random words and return them as a comma-separated string."""
        random_words = self.db.get_random_words(count)
        return ', '.join(random_words)

    def generate_mock_data_files(self, num_files, words_per_file):
        """Generate 'num_files' text files, each containing 'words_per_file' random words."""
        for i in tqdm(range(1, num_files + 1), desc="Generating Files", unit="Files"):
            # Generate a set of random words
            random_words = self.generate_random_words(words_per_file)

            # Create a file and write the random words
            file_name = os.path.join(self.output_dir, f"mock_data_{i}.txt")
            with open(file_name, 'w') as file:
                file.write(random_words)

    def close(self):
        self.db.close()
