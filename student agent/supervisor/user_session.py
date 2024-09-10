import logging

class UserSession:
    def __init__(self):
        # Set up logging
        logging.basicConfig(filename='logs/user_logs.log', level=logging.INFO)

    def log_query(self, query):
        logging.info(f"User Query: {query}")

    def log_response(self, response):
        logging.info(f"System Response: {response}")
