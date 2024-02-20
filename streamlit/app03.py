import streamlit as st

h = st.header('My Web Site on Diffusion')
s = st.subheader('เว็บไซต์ส่วนตัวของฉัน')
p = st.write('เว็บไซต์นี้แลกมาด้วยหยาดเหงื่อและความอดทน')
banner = st.image('./banner.jpg')
b = st.button('click me')
text = st.text_input('prompt: ')

if text:
    st.image('./banner.jpg')
    #text
    st.write(f'กำลังโหลด.... "{text}"')
    b = st.button('จะไปต่อหรือ...')