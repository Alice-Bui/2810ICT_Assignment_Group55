import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Sydney Airbnb Listings",
    page_icon="🏘",
)
st.title("Sydney Airbnb Listings")
st.sidebar.success("Select a page above")
@st.cache_data
def load_data(url, dtype):
    df = pd.read_csv(url, dtype=dtype)
    return df

if 'df2' not in st.session_state:
    dtype = {
        'zipcode': str,
        'weekly_price': str,
        'monthly_price': str,
        'license': object,
    }
    df2 = load_data(r"./listings_dec18.csv", dtype=dtype)
    df2.dropna(axis=1, how='all', inplace=True)
    st.session_state['df2'] = df2
else:
    df2 = st.session_state['df2']
st.dataframe(df2)

