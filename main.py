import streamlit as st
import pandas

st.set_page_config(layout = 'wide') #view wider
col1, col2= st.columns(2) # spliting two parts ryt side is image left side is contant

with col1:
    st.image("images/photo.png")

with col2:
    st.titile('Ardit Sulce')
    content = """
    Hi, I'm Ardit!, I'm a Python developer
    """
    st.write(content) # write content in the web or st.info used for highlight the content
    #st.info(content)

# we need to show the title from the data
df = pandas.read_csv('data.csv',sep=';')

with col3:
    for index, row in df[:10].iterrows(): # extracting only title from the data
        st.header(row['title']) # makeing header the title
        st.write(row['description'])
        st.image('images/'+ row['image'])
        st.write(f"[Source code] ({row['url']}")

#above code extract only 10 rows from the data there are 20
# which should show in the right side
# 1st 10 in left and next 10 in left below code

with col4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('images/' + row['image'])
        st.write(f"[Source code] ({row['url']}")

#page 2 web app inn contact_us.py