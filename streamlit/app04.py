import torch
import streamlit as st
from diffusers import DiffusionPipeline as dp
from PTL import Image

h = st.header('My Web Site on Diffusion')
s = st.subheader('เว็บไซต์ส่วนตัวของฉัน')
p = st.write('เว็บไซต์นี้แลกมาด้วยหยาดเหงื่อและความอดทน')
#banner = st.image('./banner.jpg')
b = st.button('click me')
text = st.text_input('prompt: ')

if text:
    dp = dp.from_pretranined("runwayml/stable-diffusion-v1-5",torch_dtype = torch.float16)
    #st.image('./banner.jpg')
    #text
    st.write(f'กำลังโหลด.... "{text}"')
    b = st.button('จะไปต่อหรือ...')
    
    #https://github.com/Palmmy2547/Palmmy2547.github.io