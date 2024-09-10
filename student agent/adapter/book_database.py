class BookDatabase:
    def __init__(self):
        # Initialize book database or load data
        self.books = {
            "python": "Python is a high-level, interpreted programming language...",
            "machine learning": "Machine learning is a field of artificial intelligence..."
        }

    def query_books(self, query):
        # Simple keyword-based search in book database
        for topic, info in self.books.items():
            if topic in query.lower():
                return info
        return None
