import streamlit as st
import fns

todos = fns.get_todos()


def add_todo():
    todo_g = st.session_state['new_todo'] + '\n'
    todos.append(todo_g)
    fns.write_todos(todos)


st.title('My Todo App')
st.subheader('Enter todo')
st.write('This app is meant to help you stay on truck')

for index, todo in enumerate(todos):
    st.checkbox(todo, key=todo)
    if st.session_state[todo]:
        todos.pop(index)
        fns.write_todos(todos)
        del st.session_state[todo]
        st._rerun()


st.text_input(label='Input Todo', placeholder='Enter your todo',
              key='new_todo', on_change=add_todo)

st.session_state
