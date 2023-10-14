import pandas as pd
import streamlit as st
import re
import plotly.express as px

# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Sydney Airbnb Listings",
                   page_icon="💬",)
st.title("Reviews & Comments")
st.sidebar.success("Select a page above")

@st.cache_data
def load_data(url):
    df = pd.read_csv(url)
    return df

df3 = load_data(r"./reviews_dec18.csv")

if 'df2' not in st.session_state: #in case homepage/property details has not been clicked/not finished loading the data
    df2 = load_data(r"./listings_dec18.csv")
    st.session_state['df2'] = df2
else:
    df2 = st.session_state['df2']

#selected id & city & keyword
with st.form("filtering"):
    col1, col2 = st.columns((2))
    with col1:
        property_id = st.text_input("Property ID Search:")
    with col2:
        # cleanliness = 'clean|dirt|trash|messy|untidy|hygiene|tidy|neat|sanitary|'
        keyWord = st.text_input("Comment search:")

    # search button:
    searched = st.form_submit_button("Search", type="primary")


if searched:
    if property_id:
        selected_comment = df3[df3['listing_id'] == int(property_id)][['listing_id','date','reviewer_name','comments']]
        if not keyWord:
            selected_comment = selected_comment
        else:
            selected_comment = selected_comment[selected_comment['comments'].str.contains(keyWord, na=False, flags=re.IGNORECASE, regex=True)]

        property_score = df2[df2['id'] == int(property_id)]
        rating_score = float(property_score['review_scores_rating'])
        cleanliness_score = float(property_score['review_scores_cleanliness'])
        communication_score = float(property_score['review_scores_communication'])
        location_score = float(property_score['review_scores_location'])
        value_score = float(property_score['review_scores_value'])

        star_clean = ":star:" * int(round(cleanliness_score/2, 0))
        star_communication = ":star:" * int(round(communication_score/2, 0))
        star_location = ":star:" * int(round(location_score/2, 0))
        star_value = ":star:" * int(round(value_score/2, 0))

        st.subheader(f"Review Score: {rating_score}")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.caption(f"Cleanliness: {cleanliness_score} {star_clean}")
        with col2:
            st.caption(f"Communication: {communication_score} {star_communication}")
        with col3:
            st.caption(f"Location: {location_score} {star_location}")
        with col4:
            st.caption(f"Property Value: {value_score} {star_value}")


        st.dataframe(selected_comment)
    else:
        st.markdown(st.markdown("You have not chosen your desired period"))


