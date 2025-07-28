import streamlit as st
import pandas as pd
import base64
import numpy as np

LOGO_IMAGE = "softball1.png"

def run():
    st.set_page_config(layout="wide", page_title="Welcome to BatStat: Tournament")

    # Inject custom styling for sidebar and main background
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #f4f6f9;
        }
        section[data-testid="stSidebar"] {
            background-color: #e8eaf6;
        }
        .container {
            display: flex;
        }
        .logo-text {
            font-weight:700 !important;
            font-size:50px !important;
            color: #ffffff !important;
            background-color: #691bf9 !important;
            padding: 10px 20px;
            border-radius: 8px;
            margin-left: 10px;
            margin-top: 75px !important;
        }
        .logo-img {
            float:right;
        }
        footer {visibility: hidden;}
        #MainMenu {visibility: hidden;}
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class="container">
            <img class="logo-img" src="data:image/png;base64,
            {base64.b64encode(open(LOGO_IMAGE, "rb").read()).decode()}">
            <p class="logo-text">BatStat</p>
        </div>
        """,
        unsafe_allow_html=True
    )        

    st.write("# Welcome to BatStat: Tournament.")
    st.write("## Understanding and visualizing your hitting!")    

    st.markdown(
        """
        __BatStat was developed for the senior softball player. Just enter your information about each at-bat. 
        After analyzing the data, BatStat illustrates your performance in the tournament.
        You can review your hitting by location, type of hit, on-base percentage, or simply view your batting average.
        With this information, it's easy to compare tournaments.__

        __Single game information is seldom helpful. The benefit from BatStat becomes apparent only at the Tournament level. 
        You need a lot of at-bats to generate meaningful visual representations of your hitting performance.__
        """
    )

    @st.cache_data()
    def hitting_data():
        return pd.read_csv("./data/exampleDataReducedStream.csv")

    result = hitting_data()

    # Categorize outcome types
    conditions = [
        (result['outcome'] == 'Single'),
        (result['outcome'] == 'Double'),
        (result['outcome'] == 'Triple'),
        (result['outcome'] == 'Home Run'),
        (result['outcome'] == 'Out'), 
        (result['outcome'] == "Fielder's Choice"),
        (result['outcome'] == 'Walk'), 
        (result['outcome'] == 'Sacrifice')
    ]
    values = ['1', '1', '1', '1', '0', '0','2', '3']
    result['hit'] = np.select(conditions, values, default='0')

    st.session_state['tournament'] = result

if __name__ == "__main__":  
    run()
