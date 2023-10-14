import pandas as pd
import streamlit as st
import plotly.express as px
from streamlit_option_menu

st.set_page_config(
    page_title="Sydney Airbnb Listings",
    page_icon="🏘",
)
st.title("Sydney Airbnb Listings")
st.sidebar.success("Select a page above")

if ""