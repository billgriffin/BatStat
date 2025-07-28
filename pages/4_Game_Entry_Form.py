import streamlit as st
import base64
from csv import DictWriter
import datetime

def add_bg_from_local(image_file):
          with open(image_file, "rb") as image_file:
                    encoded_string = base64.b64encode(image_file.read())
          st.markdown(
              f"""
    <style>
    .stApp {{
    background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
    background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )


title = '<p style="font-family:sans-serif; color:#bf365b; font-size: 24px;">Tournament Information</p>'
st.sidebar.markdown(title, unsafe_allow_html=True)
with st.sidebar.form( key = 'my_person'):
          first_name = st.text_input("Enter your first name", placeholder = '-*-')
          last_name = st.text_input("Enter your last name", placeholder = '-*-') 
          ### Name information should be pulled for login ###
          tourny_name = st.text_input('Tournament Name ', placeholder = '-*-')
          tourny_date = st.date_input('Tournament Date')
          tourn_data = st.form_submit_button('Submit Tournament Information', help = 'Tournament Information')


st.markdown(f'<h1 style="color: #bf365b;font-size:35px;">{"Game Entry Form"}</h1>', unsafe_allow_html=True)
st.write('After completing the **Tournament Information** section on the left, use the data entry form below '
         'to enter game information for each at-bat during the tournament.  When you complete each column, remember to submit '
         'your entries using the button at the bottom of the section. When you finish, review your entries '
         'by pressing the **Review Entries** button in the third column.  Review them carefully.  If they appear correct, then use '
         'the **Submit Game** button '
         'to load your game data into the Tournament database.')

###### Modify footer ### 
hide_streamlit_style = """
            <style>    
    footer {visibility: hidden;}
    footer:after {Car and Driver used cars
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

col1, col2, col3  = st.columns(3)
separate = '\n '
                      
with col1:  
          title = '<p style="font-family:sans-serif; color:#bf365b; font-size: 21px;">Game Details</p>'
          st.write(title, unsafe_allow_html=True)    
          with st.form('Game Details'):
                    day = st.selectbox('Day',  
                                       ['-*-','1','2','3','4'], 
                                       key = 'day',)
                    game = st.selectbox('Game', 
                                        ['-*-','1','2','3','4','5','6','7','8'], 
                                        key = 'game')
                    atbat = st.selectbox('At Bat', 
                                         ['-*-','1','2','3','4','5','6','7','8','9','10'], 
                                         key = 'atbat')                
                    submit_details = st.form_submit_button('Submit Game Details',
                                                           help = 'Game Information')
                    #if not submit_details:
                              #st.error("Game Details not submitted")

                
with col2: 
          title = '<p style="font-family:sans-serif; color:#bf365b; font-size: 21px;">Bat Outcomes</p>'
          st.write(title, unsafe_allow_html=True)  
              
          with st.form('Bat Outcomes'):
                    ball = st.selectbox('Ball Flight', 
                                           ['Enter', 'Walk', 'Fly', 'Pop Up', 'Line Drive',
                                            'Grounder',  'Strike Out', 'Fielder\'s Choice'],
                                           key = 'ball')                        
                    
                    outcome = st.selectbox('Bat Outcome', 
                                           ['Enter', 'Walk', 'Single', 'Double',\
                                            'Triple', 'Home Run', 'Out',  'Sacrifice'],
                                           key=('out'))      
                                                                  
                    location = st.selectbox('Field Location', 
                                        ['Enter', 'Walk', 'Left', 'Left-center',
                                         'Center', 'Right-center','Right', 'Strike Out'],
                                        key = 'loc')   
                    
                    
                     #error checking 
                    if outcome == "Out" and location == 'Strike Out':  
                              ball = 'Strike Out'                                 
                    elif outcome == 'Walk':                    
                              location = 'Walk'
                              ball = 'Walk'   
                    
                    
                    submit_outcomes = st.form_submit_button('Submit Bat Outcomes', 
                                                            help ='At Bat Information')
                    
                    #if not submit_outcomes:
                                                  #st.error("Game Outcomes not submitted")                    
    
with col3:
          title = '<p style="font-family:sans-serif; color:#bf365b; font-size: 21px;">Summary*</p>'
          st.write(title, unsafe_allow_html=True)  
          subtitle = '<p style="font-family:sans-serif; color:#bf365b; font-size: 15px;\
          ">*Remember to enter your submit buttons prior to reviewing entries </p>'
          st.write(subtitle, unsafe_allow_html=True)  
          
                    
          with st.form('Summary'): 
                    #if not submit_details:
                              #st.error("Game Details not submitted")   
                    #if not submit_outcomes:
                              #st.error("Game Outcomes not submitted")                            
                    review_Summary = st.form_submit_button('Review Entries') #on_click=callback
                    
          if review_Summary:
                    st.write(
                         f'**First**: **_{first_name}_** ' , separate,
                         f'**Last**: **_{last_name}_** ' , separate,
                         f'**Tournament**: {tourny_name} ', separate,
                         f'**Date**: {tourny_date} ', separate,
                         f'**Year**: {datetime.date.today().year} ', separate,
                         f'**Day**: {day} ', separate,
                         f'**Game**: {game} ',  separate,
                         f'**At Bat**: {atbat} ', separate, 
                         f'**Ball**: {ball} ', separate,
                         f'**Outcome**: {outcome} ', separate,
                         f'**Location**: {location} '                         
                         ) 
                    
          # creat dict fields
          field_names = ['first_name', 
                         'last_name',  
                         'tournament',
                         'date',
                         'year',
                         'day',
                         'game',
                         'atbat', 
                         'ball',
                         'outcome',
                         'location',
                         ]   
          
          # grab the variable values
          # create dictionary
          game_entry = {'first_name':first_name,
                              'last_name':last_name,             
                
                              'tournament':tourny_name,
                              'date':tourny_date,
                              'year':datetime.date.today().year,
                              'day':day,
                               'game':game,
                               'atbat':atbat,
                               'ball':ball,
                               'outcome':outcome,
                               'location':location,                                                                                       
                               }
     
          form = st.form(key='my-entry')
          submit = form.form_submit_button('Submit Game')    
          if submit:                    
                    with open('./data/game_entry'+ 
                              tourny_name+
                              tourny_date +'.csv', 'a') as f_object: 
                                        dictwriter_object = DictWriter(f_object, fieldnames=field_names)
                                        dictwriter_object.writerow(game_entry)
                                        f_object.close()
          
         

