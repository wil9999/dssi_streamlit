# Author: Wilson Tan
# version: 3.0
# Jun 2023

import streamlit as st
# other libs
import numpy as np
import pandas as pd
from sklearn import datasets
import matplotlib.pyplot as plt
import seaborn as sns

# -- Set page config
apptitle = 'Solution Implementation'

st.set_page_config(page_title=apptitle, page_icon='random', layout= 'wide', initial_sidebar_state="expanded") 
# layout: "centered" or "wide"
# random icons in the browser tab
# sidebar: "expanded" or "collapsed"
st.title('Toy App-1 on the go..')
st.balloons() 

######################## section-1 ##################
# Let's add a sub-title
# refer: https://docs.streamlit.io/library/cheatsheet

st.write("A **_cool_** toy application")


# Let's load and display a data set
st.subheader('**1. A random dataset**')

df1 = pd.DataFrame(np.random.randn(10, 20), columns=('col %d' % i for i in range(20)))

st.dataframe(df1.style.highlight_max(axis=0))
st.write('source: https://docs.streamlit.io/en/stable/api.html#display-data')

########################## section-2 #####################

st.subheader('**2. Boston Housing Data**')
boston = datasets.load_boston()
df2 = pd.DataFrame(boston.data, columns=boston.feature_names)
# st.dataframe(df2)

# let us try some plotting
fig, ax = plt.subplots(figsize=(6, 3))
# sns.boxplot(data=df2)
# st.pyplot(fig)

col1, col2 = st.columns((1,1))
with col2:
	df2
with col1:
	sns.boxplot(data=df2)
	st.pyplot(fig)

########################## section-3 ##########################
# try to load diabetes dataset and plot histogram for age of patients
st.subheader('**3. Diabetes Data**')
db = datasets.load_diabetes()

df3 = pd.DataFrame(db.data, columns=db.feature_names)

st.dataframe(df3)

st.table(df3)

st.write(df3)

########################## section-4 ##########################
# try some interactivity
st.subheader('**Activity 01C**')
df4 = pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [5, 6, 7, 8]
     })
if st.checkbox('show/hide data'):
     df4

option = st.selectbox(
     'which number do you like best?',
     df4['second column'])

'You selected: ', option

option = st.selectbox(
     'which number do you like best?', 
     df4.unstack().reset_index(drop=True))

'You selected: ', option

chosen = st.radio(
        'ISS new courses',
        ('DSSI', 'XAI', 'AMLFin', 'Credit Scoring'))

st.write(f'You opted to learn: {chosen}!')

########################## section-5 ##########################
# Know this place?

map_data = pd.DataFrame(
    np.random.randn(100, 2)/ [20, 20] + [1.3521, 103.8198], 
    columns = ['lat', 'lon'])

st.map(map_data)

