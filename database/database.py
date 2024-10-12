import sqlite3
import json
from tqdm import tqdm

class WordDatabase:
    def __init__(self, db_name="words.db"):

        self.words_json_file_path= "database/words.json"
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.create_table()

    def create_table(self):
        """Create a table to store words if it doesn't exist."""
        with self.conn:
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS words (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    word TEXT NOT NULL
                );
            """)

    def insert_words(self, words):
        """Insert a list of words into the database."""
        with self.conn:
            self.conn.executemany("INSERT INTO WORDS (word) VALUES (?);", [(word,) for word in words])

    def get_random_word(self):
        """Fetch a random word from the database."""
        cursor = self.conn.cursor()
        cursor.execute("SELECT word FROM words ORDER BY RANDOM() LIMIT 1;")
        return cursor.fetchone()[0]

    def get_random_words(self, count):
        """Fetch multiple random words from the database."""
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT word FROM words ORDER BY RANDOM() LIMIT {count};")
        return [row[0] for row in cursor.fetchall()]

    def populate_word_database_from_json(self, db_path="words.db"):
        """Load the words from a JSON file and insert the keys (words) into the database."""
        # Load the JSON file
        with open(self.words_json_file_path, 'r') as f:
            data = json.load(f)

        # Extract keys (words)
        word_list = list(data.keys())

        # Initialize the database and insert words
        word_db = WordDatabase(db_path)
        word_db.insert_words(word_list)
        word_db.close()

    def close(self):
        self.conn.close()


