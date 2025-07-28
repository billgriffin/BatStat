import streamlit as st
import pandas as pd
import base64
import os   
from st_aggrid import AgGrid
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode, ColumnsAutoSizeMode, AgGridTheme
from st_aggrid.shared import GridUpdateMode, JsCode

# Store the data for tournaments in the 'tourns' variable
tourns = st.session_state['tournament']

# Display a header title for the tournament review
st.markdown("<h1 style='color: #bf365b;font-size:35px;'>BatStat Tournament Review</h1>", unsafe_allow_html=True)

# Pick a tournament and year using the Streamlit sidebar
st.sidebar.markdown("<p style='font-family:sans-serif; color:#bf365b; font-size: 24px;'>Pick A Tournament</p>", unsafe_allow_html=True)
select_year = list(tourns.year.unique()) # list of unique years in 'tourns'
year_pick = st.sidebar.selectbox('Choose Year:', select_year) # Select a year from the list
selYear_df = tourns[(tourns['year'] == year_pick)] # Filter 'tourns' by selected year

select_tournys = list(selYear_df.tournament.unique()) # list of unique tournaments in filtered 'tourns'
tourny_pick = st.sidebar.selectbox('Choose Tournament:', select_tournys) # Select a tournament from the list

# Display the entries for the selected tournament
# Show filtered dataframe with selected tournament

field_names = ['tournament',
                        'day',
                         'game',
                         'atbat', 
                         'ball',
                         'outcome',
                         'location'
                         ]
                            
relevant_data = selYear_df.loc[(selYear_df['tournament'] == str(tourny_pick))]
view_data = pd.DataFrame(relevant_data, columns = field_names)

####################
red_light = "#bf365b"
##################
columns = ["tournament","day", "game", "atbat", "ball", "outcome", "location"]

gb = GridOptionsBuilder.from_dataframe(view_data)

for col in columns:
    header_name = col.capitalize().replace("_", " ")
    gb.configure_column(col, header_name=header_name, editable=False)
    
gb.configure_default_column(cellStyle={'color':red_light, 'font-size': '14px'}, 
                            suppressMenu=True, 
                            wrapHeaderText=True, 
                            autoHeaderHeight=True,
                            suppressSizeToFit=True,
                            )

custom_css = {".ag-header-cell-text": {"font-size": "16px", 
                                       'text-overflow': 'revert;', 
                                       'font-weight': 700},
              ".ag-theme-streamlit": {'transform': "scale(0.8)", 
                              "transform-origin": '0 0'}
              }

gridOptions = gb.build()

gridOptions['suppressHorizontalScroll'] = True # set suppressHorizontalScroll option to True


AgGrid(
    view_data,
    gridOptions=gridOptions,
    custom_css=custom_css,
    #allow_unsafe_jscode=True,
    columns_auto_size_mode=ColumnsAutoSizeMode.FIT_CONTENTS,    
    theme=AgGridTheme.BALHAM, 
    height=350    
    )
#####################

    #width='100%',
st.subheader("This is a scrollable table showing the Tournament you have selected.")

# Hide the Streamlit footer and replace with custom text
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






