from llm.llm_agent import LLMAgent
from adapter.book_database import BookDatabase

class Adapter:
    def __init__(self):
        self.llm_agent = LLMAgent()
        self.book_db = BookDatabase()

    def process_query(self, query):    
        db_response = self.book_db.query_books(query)
        if db_response:
            return db_response

        return self.llm_agent.query_llm(query)
