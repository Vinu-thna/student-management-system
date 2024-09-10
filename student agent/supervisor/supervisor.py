from adapter.adapter import Adapter
from supervisor.user_session import UserSession

class Supervisor:
    def __init__(self):
        self.adapter = Adapter()
        self.user_session = UserSession()

    def handle_query(self, query):
        self.user_session.log_query(query)

        response = self.adapter.process_query(query)

        self.user_session.log_response(response)

        return response
