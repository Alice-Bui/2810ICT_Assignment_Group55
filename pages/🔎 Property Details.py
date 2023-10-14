import pandas as pd
import streamlit as st
import plotly.express as px

# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Sydney Airbnb Listings",
                   page_icon="🔎",)
st.title("Property Details")
st.sidebar.success("Select a page above")
@st.cache_data
def load_data(url):
    df = pd.read_csv(url)
    return df
df1 = load_data(r"./calendar_dec18.csv").dropna()

if 'df2' not in st.session_state: #in case homepage has not been clicked/not finished loading the data
    df2 = load_data(r"./listings_dec18.csv")
    st.session_state['df2'] = df2
else:
    df2 = st.session_state['df2']

#selected period & city
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

    #search button:
    searched = st.form_submit_button("Search", type="primary")

if searched:
    if date1 and date2:
        selected_period = df1[(df1["date"] >= date1) & (df1["date"] <= date2)]
        selected_id = selected_period['listing_id'].unique()
        selected_df = df2[df2['id'].isin(selected_id)][['id', 'listing_url', 'city', 'description', ]]
        if not city:
            output = selected_df
        else:
            output = selected_df[selected_df["city"].isin(city)]

        st.subheader("Price Range")
        fig = px.histogram(selected_period, x = "price", nbins=70)
        st.plotly_chart(fig, use_container_width=True, height=200)

        st.subheader("Available AirBnB Listings:")
        st.dataframe(output)
    else:
        st.markdown(st.markdown("You have not chosen your desired period"))
