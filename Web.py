import streamlit as st
import functions

todo_list = functions.get_todos()

st.title("My ToDo App")
st.subheader("this is my todo app")
st.write("tell Alex I love him")

for todo in todo_list:
    st.checkbox(todo)

st.text_input(label="new todo", placeholder=("Add a new ToDo..."), 
              label_visibility="collapsed")