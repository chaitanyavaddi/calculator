import streamlit as st
st.title('calculator')
with st.container(border=True):
    a = st.text_input('Enter First Number', placeholder='Eg. 25')
    b = st.text_input('Enter second number', placeholder='Eg. 30')
    operation = st.radio('Operation', ['Add', 'Substract', 'Multiply', 'Divide'], horizontal=True)
    x = st.button('Calculate', type='primary')
    if x:
        if operation == 'Add':
            st.header(int(a) + int(b))
        if operation == 'Substract':
            st.header(int(a) - int(b))
        if operation == 'Multiply':
            st.header(int(a) * int(b))
        if operation == 'Divide':
            st.header(int(a) / int(b))