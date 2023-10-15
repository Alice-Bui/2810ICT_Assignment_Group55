import pandas as pd
import streamlit as st
import plotly.express as px
import re
# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Sydney Airbnb Listings",
                   page_icon="🔎",)
st.title("Property Details")
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
df1 = load_data(r"./calendar_dec18.csv", None).dropna()
#selected period & city & keyword
with st.form("filtering"):
    col1, col2 = st.columns((2))
    df1["date"] = pd.to_datetime(df1["date"])
    startDate = pd.to_datetime(df1["date"]).min()
    endDate = pd.to_datetime(df1["date"]).max()
    with col1:
        date1 = pd.to_datetime(st.date_input("Start Date", value=None, min_value=startDate, max_value=endDate))
    with col2:
        date2 = pd.to_datetime(st.date_input("End Date", value=None, min_value=startDate, max_value=endDate))
    city = st.multiselect("Select the Suburb:", df2["city"].unique())
    keyWord = st.text_input("Description Keyword")
    #search button:
    searched = st.form_submit_button("Search", type="primary")
if searched:
    if date1 and date2:
        selected_period = df1[(df1["date"] >= date1) & (df1["date"] <= date2)]
        selected_id = selected_period['listing_id'].unique()
        selected_df = df2[df2['id'].isin(selected_id)][['id', 'listing_url', 'city', 'description', ]]
        if not city:
            selected_df = selected_df
        else:
            selected_df = selected_df[selected_df["city"].isin(city)]

        if not keyWord:
            output = selected_df
        else:
            output = selected_df[selected_df['description'].str.contains(keyWord, na=False, flags=re.IGNORECASE, regex=True)]

        st.subheader("Price Range in the Selected Period")
        fig = px.histogram(selected_period, x="price", nbins=70)
        st.plotly_chart(fig, use_container_width=True, height=200)

        st.subheader("Available AirBnB Listings:")
        st.dataframe(output)
    else:
        st.markdown("You have not chosen your desired period")

