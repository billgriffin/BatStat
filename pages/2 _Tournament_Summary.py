import pandas as pd
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
from pywaffle import Waffle
import os
import sys
directory_path = os.getcwd()
sys.path.insert(0, directory_path +"/utils")

from tourny_hits import(
    tourny_pie_plot, 
    tourny_bar_plot, 
    tourny_bubbles_plot, 
    tourny_waffles_plot
    )
from tourny_outcomes import( 
    tourny_all_pie, 
    tourny_all_bar, 
    tourny_all_bubbles, 
    tourny_all_waffle
    )

# Grab the data
tourns = st.session_state['tournament']

# Pick a Tournament / Year
st.sidebar.title('Select A Tournament To Review?')
select_year = list(tourns.year.unique())
year_pick = st.sidebar.selectbox('Choose Year :', select_year)
selYear_df = tourns[(tourns['year'] == year_pick)] 
select_tournys = list(selYear_df.tournament.unique())
tourny_pick = st.sidebar.selectbox('Choose Tournament :', select_tournys)

# Hits by Tournament
@st.cache_data(show_spinner=True, max_entries=1)
def hits_by_loc_by_tourny_yr(tournament, selYear_df):
    tourn = selYear_df.loc[(selYear_df['tournament'] == str(tourny_pick)) & (selYear_df['hit'] == '1')]
    allSum_hits = (tourn.groupby(['location'])['outcome'].count().squeeze().to_dict())
    return allSum_hits

hits = hits_by_loc_by_tourny_yr(tourny_pick, selYear_df)
   
    
# Outcomes by Tournament 
@st.cache_data(show_spinner=True, max_entries=1)
def all_outcomes(tournament):
    tourn = tourns.loc[(tourns['tournament'] == str(tournament))]
    all_contacts = (
    tourn.groupby(['outcome'])['location'].count()
    .squeeze()
    .to_dict()
    )
    return all_contacts

out_com = all_outcomes(tourny_pick)


st.markdown(
    '<h1 style="color: #bf365b;font-size:35px;">Tournament Play</h1>',
    unsafe_allow_html=True
)
st.markdown(
    '<h1 style="color: #bf365b;font-size:25px;">View Outcomes, Hits, or Field View</h1>',
    unsafe_allow_html=True
)

hide_streamlit_style = """
<style>    
    footer {visibility: hidden;}
    footer:after {
    content:'Senior BatStat: Tournament'; 
        color: #bf365b;
        background-color: #bf9b36;
        font-size:20rpx;
        visibility: visible;
        display: block;
        position: relative;
        padding: 5px;
        top: 2px;    }
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

##############

st.write("""
Pick the __Year__ and __Tournament__ you want to view and then select a format.  Options include __Outcome__ type (e.g., Double, Walk)
or __Hits__ by location, both allow you to pick four chart types:  __Pie__, __Bar__, __Bubble__ or __Waffle__.  These are different ways to view the same
information.  And finally, **Field View** shows your distribution of hits on the diamond. 
""")

tabs = st.tabs(["Outcomes", "Hits", "Field View"])
tab_outcomes, tab_hits, tab_field = tabs

st.sidebar.title('Chart Type: Pie, Bar, Bubble or Waffle?')
option = st.sidebar.selectbox('Options:', ('Pie', 'Bar', 'Bubble', 'Waffle'))

with tab_outcomes:
    container1 = st.container() 
    with container1:
        if option == 'Pie':
            st.plotly_chart(tourny_all_pie(out_com, tourny_pick, year_pick), theme="streamlit", use_container_width=True)
            st.markdown("""<hr style="height:5px;border:none;color:#bf9b36;background-color:#bf9b36;" /> """, 
                                unsafe_allow_html=True) 
        if option == 'Bar':
            st.plotly_chart(tourny_all_bar(out_com, tourny_pick, year_pick), theme="streamlit", use_container_width=True)
            st.markdown("""<hr style="height:5px;border:none;color:#bf9b36;background-color:#bf9b36;" /> """, 
                                unsafe_allow_html=True) 
        if option == 'Bubble':    
            st.plotly_chart(tourny_all_bubbles(out_com, tourny_pick, year_pick), theme="streamlit", use_container_width=True)
            st.markdown("""<hr style="height:5px;border:none;color:#bf9b36;background-color:#bf9b36;" /> """, 
                                unsafe_allow_html=True)     
        if option == 'Waffle': 
            plt.figure(tourny_all_waffle(out_com, tourny_pick, year_pick))
            st.markdown("""<hr style="height:5px;border:none;color:#bf9b36;background-color:#bf9b36;" /> """, 
                                unsafe_allow_html=True)       
                   

with tab_hits:
    container1 = st.container() 
    with container1:
        if option == 'Pie':
            st.plotly_chart(tourny_pie_plot(hits, tourny_pick, year_pick), theme="streamlit", use_container_width=True)
            st.markdown("""<hr style="height:5px;border:none;color:#bf9b36;background-color:#bf9b36;" /> """, 
                                unsafe_allow_html=True)
        if option == 'Bar':    
            st.plotly_chart(tourny_bar_plot(hits, tourny_pick, year_pick), theme="streamlit", use_container_width=True)
            st.markdown("""<hr style="height:5px;border:none;color:#bf9b36;background-color:#bf9b36;" /> """, 
                                unsafe_allow_html=True) 
        if option == 'Bubble':   
            st.plotly_chart(tourny_bubbles_plot(hits, tourny_pick, year_pick), theme="streamlit", use_container_width=True)
            st.markdown("""<hr style="height:5px;border:none;color:#bf9b36;background-color:#bf9b36;" /> """, 
                                unsafe_allow_html=True) 
        if option == 'Waffle': 
            plt.figure(tourny_waffles_plot(hits, tourny_pick, year_pick))
            st.markdown("""<hr style="height:5px;border:none;color:#bf9b36;background-color:#bf9b36;" /> """, 
                                unsafe_allow_html=True)                   
with tab_field:
    container1 = st.container()
    with container1:
        st.markdown(f'<h2 style="color: #bf365b;font-size:25px;">{"Summary for " + str(tourny_pick) + ": " + str(year_pick) }</h2>',
                    unsafe_allow_html=True)

        from imagetournaments import imagetournaments

        imagetournaments(selYear_df.loc[(selYear_df['tournament'] == str(tourny_pick))])




