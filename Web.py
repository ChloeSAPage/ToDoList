import streamlit as st
import functions

todo_list = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todo_list.append(todo)
    functions.write_todos(todo_list)



st.title("My ToDo App")
st.subheader("this is my todo app")
st.write("tell Alex I love him")

for todo in todo_list:
    st.checkbox(todo, key=todo)

st.text_input(label="Add a new todo", placeholder=("Add a new ToDo..."), 
              label_visibility="collapsed", on_change=add_todo, key="new_todo")

st.session_state