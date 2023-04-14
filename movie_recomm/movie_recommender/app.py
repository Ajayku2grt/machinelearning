import pandas as pd
import streamlit as st
import pickle
import pandas as pd

movies_list = pickle.load(open('movies_dict.pkl', 'rb'))
movies=pd.DataFrame(movies_list)

st.title("Movie Recommender Systems")

option = st.selectbox(
    'How would you like to be contacted?',
    movies['title'].values)

if st.button('Recommend Related Movie'):
    st.write('Movie :', option)

