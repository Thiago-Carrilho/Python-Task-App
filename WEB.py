import streamlit as st
import functions1

todos = functions1.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    functions1.write_todos(todos)


st.title("My Task App")

st.write("This app wil increase your productivity ")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)

    if checkbox:
        todos.pop(index)
        functions1.write_todos(todos)
        del st.session_state[todo]
        st.rerun()
st.text_input(label="", placeholder="Add a new Task...",
              on_change=add_todo, key="new_todo")
"\n"
"\n"
st.write("This app was built by Thiago Carrilho")
