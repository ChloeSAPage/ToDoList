import streamlit as st
import functions

todo_list = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"].strip().capitalize() + "\n"
    todo_list.append(todo)
    functions.write_todos(todo_list)
    st.session_state["new_todo"] = ""

st.title("My ToDo App")
st.subheader("this is my todo app")
st.write("tell Alex I love him")

for index, todo in enumerate(todo_list):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todo_list.pop(index)
        functions.write_todos(todo_list)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Add a new todo", placeholder=("Add a new ToDo..."), 
              label_visibility="collapsed", on_change=add_todo, key="new_todo")
