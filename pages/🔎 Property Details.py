import pandas as pd
import streamlit as st
import plotly.express as px

# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Sydney Airbnb Listings",
                   page_icon="🔎",)
st.title("Property Details")








###df1 = pd.read_csv(r".\calendar_dec18.csv",
##                  usecols=["listing_id", "date", "price"]).dropna()

##df2 = pd.read_csv(r".\listings_dec18.csv",
 #                 usecols=["id", "listing_url", "name", "city"])

#df3 = pd.read_csv(r".\reviews_dec18.csv")

#df12 = df1.merge(df2, left_on='listing_id', right_on='id')

#col1, col2 = st.columns((2))
#df1["date"] = pd.to_datetime(df1["date"])

# selected period
#startDate = pd.to_datetime(df1["date"]).min()
#endDate = pd.to_datetime(df1["date"]).max()

#with col1:
#    date1 = pd.to_datetime(st.date_input("Start Date", startDate))

#with col2:
#    date2 = pd.to_datetime(st.date_input("End Date", endDate))

#df1 = df1[(df1["date"] >= date1) & (df1["date"] <= date2)].copy()




#st.dataframe(df1)
#st.dataframe(df2)
#st.dataframe(df3)

