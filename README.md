# student-management-system
Developed this system using Streamlit for the front end and an open-source LLM agent for the backend processing. The system features an architecture with clear boundaries across supervisor, adapter and LLM layers which ensures the effective handling of book related queries and follow up questions. User interactions are logged for seamless tracking and improving of future responses.
The system is structured into 3 distinct layers:
1. SUPERVISOR LAYER: This layer manages user interactions and also logs in the queries to track for continuous learning and improving.
2. ADAPTER LAYER: Acts as a bridge between supervisor layer and LLm. This layer decides wheather a query can be answered using pre-existing data from local database or if it needs to be forwarded to the LLM agent for more complex responses.
3. LLM LAYER: This layer uses a model GPT-2 hosted by the hugging face transformer library genrating intelligent and context-aware response to the queries. This layer makes sure that the system can provide relavent answers to the questions.
  
  After this we uses a "LOGGING SYSTEM" that records all the user interactions which allows the system to track query history and refine its response over time.
