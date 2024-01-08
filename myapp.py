import streamlit as st
st.set_page_config(page_title='cats')
st.header("Types of Cats")
col1,col2=st.columns(2)
with col1:
  st.subheader("persian Cat")
  st.image("./persian cat.jpeg",caption="persian Cat",width=300,use_column_width=True)
  st.write("persians cats are cute")
with col2:
  st.subheader("ocicat")
  st.image("./ocicat.jpg",caption="ocicat",width=300,use_column_width=True)
  st.write("oci cats are proud")
  
