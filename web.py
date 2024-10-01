import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("My todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

for index, existing_todo in enumerate(todos):
    checkbox = st.checkbox(existing_todo, key=existing_todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[existing_todo]
        st.rerun()

st.text_input(label="The label", placeholder="Add new todo...",
              on_change=add_todo, key="new_todo") # label_visibility=False,
