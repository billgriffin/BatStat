import streamlit as st
import pandas as pd
import os
import csv

from st_aggrid import AgGrid
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode, ColumnsAutoSizeMode, AgGridTheme
from st_aggrid.shared import GridUpdateMode, JsCode

###### Modify footer ### 
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

folder_path = './data/'

### Create a 'holding' dataset ###

############### How to get the correct tourny & date 
def submitting_data():
    return pd.read_csv(
            "./data/game_entry.csv", index_col=None
        )    


################## Grab the data  ##################
st.markdown(f'<h1 style="color: #bf365b;font-size:35px;">{"Tournament Review Form"}</h1>', unsafe_allow_html=True)

field_names = ['tournament',
                        'day',
                         'game',
                         'atbat', 
                         'ball',
                         'outcome',
                         'location'
                         ]
red_light = "#bf365b"

# grab the data
review_dat0= submitting_data() #data
review_dat = pd.DataFrame(review_dat0, columns = field_names) #reduce columns

gb = GridOptionsBuilder.from_dataframe(review_dat)

columns = ["tournament","day", "game", "atbat", "ball", "outcome", "location"]
for col in columns:
    header_name = col.capitalize().replace("_", " ")
    gb.configure_column(col, header_name=header_name, editable=True)
    
gb.configure_default_column(cellStyle={'color':red_light, 'font-size': '14px'}, 
                            suppressMenu=True, 
                            wrapHeaderText=True, 
                            autoHeaderHeight=True,
                            suppressSizeToFit=True,
                            )

custom_css = {".ag-header-cell-text": {"font-size": "16px", 
                                       'text-overflow': 'revert;', 
                                       'font-weight': 700},
              ".ag-theme-balham": {'transform': "scale(0.8)", 
                              "transform-origin": '0 0'}
              }

gridOptions = gb.build()
gridOptions['suppressHorizontalScroll'] = True # set suppressHorizontalScroll option to True

# insert it into AgGrid
submit_data = AgGrid(
            review_dat,
            gridOptions=gridOptions,
            editable = True,
            custom_css=custom_css,
            #allow_unsafe_jscode=True,
            columns_auto_size_mode=ColumnsAutoSizeMode.FIT_CONTENTS,    
            theme=AgGridTheme.BALHAM, 
            height=300
            )



# modified from review
modified_data = submit_data["data"]


st.write('Above are the hitting data that you entered using the **Game Entry Form** for a specific tournament.   Closely review the table.  If you need to make any changes, '
         'this is the place to make them.    If you are satisfied with the tournament information -- everything is accurate and complete -- then press the **Submit Tournament Data** below.'
         '  After pressing the button, your data are entered into the larger database and your **Game Entry Form** data for a specific tournament are cleared. ')
       

if st.button("📥  Submit Tournament Data"):
    modified_data.to_csv(os.path.join(folder_path, "game_submit.csv"), 
                         header = False,
                         index=False)    
    
    # appending clean data to bat.csv
    modified_data.to_csv(os.path.join(folder_path,"bat.csv"),index=False,header=False,mode="a")       
                                   
    # create new  game_entry file
    colheaders = ['first','last','tournament','date','year','day','game','atbat','ball','outcome','location']
    
    with open(os.path.join(folder_path, "game_entry.csv"), 'w') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)         
        # writing the fields
        csvwriter.writerow(colheaders)  
        
#view cleaned game_entry file
review_dat = submitting_data() 

    
    
    
    

