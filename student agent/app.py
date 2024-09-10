import streamlit as st
from supervisor.supervisor import Supervisor

supervisor = Supervisor()

st.title("Student Management System")

# User input for querying the system
user_input = st.text_input("Ask a question related to books or topics:")

# If user submits a query
if st.button("Submit"):
    response = supervisor.handle_query(user_input)
    st.write(response)
