import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
from pywaffle import Waffle
import os
import sys
# from login import main

directory_path = os.getcwd()
sys.path.insert(0, directory_path +"/utils")

# Call the login function
# main()

# # Check if the user is logged in
# if 'logged_in' not in st.session_state or not st.session_state['logged_in']:
#     # If the user is not logged in, display an error message and exit
#     st.error('Please log in to access this page')
#     st.stop()

# # If the user is logged in, display the page content
# st.write('Welcome to the app!')

from hits import(
    plot_pie, 
    plot_bar, 
    plot_bubble, 
    plot_waffle
    )
from outcomes import(
    outcome_plot_pie,
    outcome_plot_bar,
    outcome_plot_bubbles,
    outcome_plot_waffles
    )

# Grab the data  
tourns = st.session_state['tournament']

# Select a year
st.sidebar.title('Select A Year To Review?')
select_year = list(tourns.year.unique())
year_pick = st.sidebar.selectbox('Choose Year:', select_year)
sel_year_df = tourns[(tourns['year'] == year_pick)]

# Generate hits
@st.cache_data(show_spinner=True, max_entries=1)
def summarize_hits_by_location(tournament, sel_year_df):
    tournament = sel_year_df.loc[(sel_year_df['hit'] == '1' )]
    allSum_h = (tournament.groupby(['location'])['outcome'].count()
            .squeeze()
            .to_dict())
    return allSum_h

#Generate  outcomes
@st.cache_data(show_spinner=True, max_entries=1)
def all_outcomes_plots(tournament):
    all_contacts = tournament.groupby(['outcome'])['location'].count().squeeze().to_dict()
    return all_contacts

#Generate plotting data
hits = summarize_hits_by_location(tourns, sel_year_df)
all_contacts = all_outcomes_plots(sel_year_df)
    
# Layout Application

# Headers
st.markdown(f'<h1 style="color: #bf365b;font-size:35px;">Yearly Summaries</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color: #bf365b;font-size:25px;">View Outcomes, Hits, or Field View</h1>', unsafe_allow_html=True)

# Modify Footer
hide_streamlit_style = """
        <style>    
            footer {visibility: hidden;}
            footer:after {
            content:'Senior BatStat: Tournament'; 
                color: #bf365b;
                background-color: #bf9b36;
                font-size:20px;
                visibility: visible;
                display: block;
                position: relative;
                padding: 5px;
                top: 2px;    }
            </style>            
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.write("""
## Select Year and Chart Type

Pick a __Year__ and then select the type of chart that provides you a clear sense of your hitting. 
Below you can choose to view __Outcomes__, such as doubles or walks, or __Hits__ 
by location. Both options allow you to pick from the four chart types: pie, bar, bubble, or waffle. 
These charts offer different ways to view the same information.

## Field View

In addition to the charts, you can use the __Field View__ option to examine your hit distribution on the diamond. 
This provides a unique and visual way to analyze your performance. 
""")


## TabsBlue
tabs = st.tabs(["Outcomes", "Hits", "Field View"])
tab_outcomes, tab_hits, tab_field = tabs   
option = st.sidebar.selectbox('Chart Type:', ('Pie', 'Bar', 'Bubble', 'Waffle'))

#display_tabs(tabs_dict)

with tab_outcomes:
    container1 = st.container() 
    with container1:
        if option == 'Pie':
            st.plotly_chart(outcome_plot_pie(all_contacts, year_pick), theme="streamlit", use_container_width=True)
            st.markdown("""<hr style="height:5px;border:none;color:#bf9b36;background-color:#bf9b36;" /> """, 
                                unsafe_allow_html=True) 
        if option == 'Bar':
            st.plotly_chart(outcome_plot_bar(all_contacts, year_pick), theme="streamlit", use_container_width=True)
            st.markdown("""<hr style="height:5px;border:none;color:#bf9b36;background-color:#bf9b36;" /> """, 
                                unsafe_allow_html=True) 
        if option == "Bubble":            
            st.plotly_chart(outcome_plot_bubbles(all_contacts, year_pick), theme="streamlit", use_container_width=True)
            st.markdown("""<hr style="height:5px;border:none;color:#bf9b36;background-color:#bf9b36;" /> """, 
                                unsafe_allow_html=True)  
        if option == 'Waffle': 
            plt.figure(outcome_plot_waffles(all_contacts, year_pick))
            st.markdown("""<hr style="height:5px;border:none;color:#bf9b36;background-color:#bf9b36;" /> """, 
                                unsafe_allow_html=True)   
                

with tab_hits:
    container1 = st.container() 
    with container1:
        if option == 'Pie':
            st.plotly_chart(plot_pie(hits, year_pick), theme="streamlit", use_container_width=True)
            st.markdown("""<hr style="height:5px;border:none;color:#bf9b36;background-color:#bf9b36;" /> """, 
                                unsafe_allow_html=True)
        if option == 'Bar':            
            st.plotly_chart(plot_bar(hits, year_pick), theme="streamlit", use_container_width=True)
            st.markdown("""<hr style="height:5px;border:none;color:#bf9b36;background-color:#bf9b36;" /> """, 
                                unsafe_allow_html=True) 
        if option == 'Bubble':
            st.plotly_chart(plot_bubble(hits, year_pick), theme="streamlit", use_container_width=True)
            st.markdown("""<hr style="height:5px;border:none;color:#bf9b36;background-color:#bf9b36;" /> """, 
                                unsafe_allow_html=True) 
        if option == 'Waffle': 
            plt.figure(plot_waffle(hits, year_pick))
            st.markdown("""<hr style="height:5px;border:none;color:#bf9b36;background-color:#bf9b36;" /> """, 
                                unsafe_allow_html=True)           
                

with tab_field:
    container1 = st.container()
    with container1: 
        st.markdown(f'<h2 style="color: #bf365b;font-size:25px;">{"Summary for " + str(year_pick) }</h2>', 
                            unsafe_allow_html=True)

    from summaryimage import imageSummary        
    imageSummary(sel_year_df)  

