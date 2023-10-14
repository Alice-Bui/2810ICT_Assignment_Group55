import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Sydney Airbnb Listings",
    page_icon="🏘",
)
st.title("Sydney Airbnb Listings")
st.sidebar.success("Select a page above")
@st.cache_data
def load_data(url):
    df = pd.read_csv(url)
    return df

if 'df2' not in st.session_state: #in case homepage has been clicked first
    df2 = load_data(r"./listings_dec18.csv")
    st.session_state['df2'] = df2
else:
    df2 = st.session_state['df2']
st.dataframe(df2)

