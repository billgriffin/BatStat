import streamlit as st
import pandas as pd
import plotly.express as px
from pywaffle import Waffle
import matplotlib.pyplot as plt

# Hits for Yearly_Summary
#Define the function for pie plot
def plot_pie(hits, year_pick):
    labels_pie = list(hits.keys())
    sizes_pie = list(hits.values())

    all_hits_pie = px.pie(values = sizes_pie, 
                        names = labels_pie, 
                        title = 'Location of hits'  + " in " + str(year_pick),   
                        color_discrete_sequence = px.colors.qualitative.G10,
                        hole = .25)
    all_hits_pie.update_traces(textposition='inside', 
                               textinfo='percent+label',
                               textfont_color="black")
    all_hits_pie.update_layout(
                               title_font_color="#bf365b",
                               legend=dict(title='Hit Locations'),
                               legend_title_font_color="black",
                               legend_font_color = "black"
                               )
    return all_hits_pie

#Define the function for bar plot
def plot_bar(hits, year_pick):
    bar_x = dict(sorted(hits.items(), key=lambda item:item[1], reverse=True))
    
    bar_labels = list(bar_x.keys())
    bar_values = list(bar_x.values())
    
    bar_values_sum = sum(bar_values)
    bar_values_sum = sum(bar_values)
    bar_values_percent = [value/bar_values_sum for value in bar_values]
    bar_values_percent_format = [f"{value:2.1%}" for value in bar_values_percent]
    
    all_hits_bar = px.bar(x = bar_labels, 
                        y = bar_values,
                        text_auto = 'True',
                          title = 'Frequency of hits' + " in " + str(year_pick),
                      color = bar_labels,                    
                      text = bar_values_percent_format,
                      labels = {'y': 'Frequency of Outcome', 
                                'x': 'Outcomes',
                                'text': 'bar_values_percent'},                    
                      color_discrete_sequence = 
                      px.colors.qualitative.G10)
    all_hits_bar.update_traces(textfont_color='black')
    all_hits_bar.update_layout(
        title_font_color="#bf365b",
        legend=dict(title='Hit Locations'), 
        legend_title_font_color="black",
        legend_font_color="black",        
        xaxis=dict(
            title_font=dict(
                color='black'
            ),
            tickfont=dict(
                color='black'
            )
        ),
        yaxis=dict(
            title_font=dict(
                color='black'
            ),
            tickfont=dict(
                color='black'
            )
        )
    )    
    return all_hits_bar

# Bubble
def plot_bubble(hits, year_pick):
    bubble_x = dict(sorted(hits.items(), key=lambda item:item[1], reverse=True))
    bubble_labels = list(bubble_x.keys())
    bubble_values = list(bubble_x.values())

    bubble_values_sum = sum(bubble_values)
    bubble_values_percent = [value/bubble_values_sum for value in bubble_values]
    bubble_values_percent_format = [f"{value:2.1%}" for value in bubble_values_percent]
    bubbles = pd.DataFrame(list(zip(bubble_labels, bubble_values, bubble_values_percent_format)), 
                           columns = ['location','frequency','percent'])

    bubbles['Y'] = [1]*len(bubbles)
    list_x = list(range(0,len(bubbles)))
    bubbles['X'] = list_x

    #create a label list for each bubble 
    label = [i+'<br>'+str(j)+'<br>'+str(k)+'%' for i,j,k in zip(bubbles.location,
                                                                bubbles.frequency,
                                                                bubbles.percent)]

    all_hits_bubbles = px.scatter(bubbles, x='X', y='Y',
                title = 'Frequency and Percentage of Hits by Location '
                + " in " + str(year_pick),                              
                 color='location', color_discrete_sequence=px.colors.qualitative.G10,
                 size='frequency', text=label, size_max=90
                )
    all_hits_bubbles.update_layout(width=900, height=320,
                  margin = dict(t=50, l=0, r=0, b=0),
                  showlegend=False,
                  title_font_color="#bf365b",
                  font_color= "black"
                 )
    all_hits_bubbles.update_traces(textposition='top center')
    all_hits_bubbles.update_xaxes(showgrid=False, zeroline=False, visible=False)
    all_hits_bubbles.update_yaxes(showgrid=False, zeroline=False, visible=False)
    return all_hits_bubbles

def plot_waffle(hits, year_pick):
    # plot setup
    plt.style.use('fivethirtyeight')
    plt.rcParams.update({
            "font.size": 16,
        "font.family": "serif",
        "font.serif": "Ubuntu",
        "font.monospace": "Ubuntu Mono",
        "axes.labelsize": 14,
        "axes.labelweight": "bold",
        "axes.titlesize": 14,
        "axes.facecolor": 'gray',
        "xtick.labelsize": 12,
        "ytick.labelsize": 12,
        "legend.fontsize": 12,
        "figure.titlesize": 16,
        "figure.titleweight": "bold",
        "figure.figsize": [10, 7.5],
        "figure.autolayout": True,
        "figure.facecolor": 'gray',
        "figure.edgecolor": "#bf365b"
        })           
    waffle_x = dict(sorted(hits.items(), key=lambda item:item[1], reverse=True))

    waffle_labels = list(waffle_x.keys())  #####
    waffle_values = list(waffle_x.values()) 

    waffle_values_sum = sum(waffle_values)
    waffle_values_percent = []
    waffle_values_percent_format = []  
    waffle_values_percent = [((value/waffle_values_sum)) for value in waffle_values]
    for value in (waffle_values_percent):
        waffle_values_percent_format.append(f"{value:2.1%}")

    ### Create df ###
    waffles = pd.DataFrame(list(zip(waffle_labels, 
                                                 waffle_values,                            
                                                 waffle_values_percent_format)), 
                                        columns = ['location','frequency','percent'])

    waffles['Y'] = [1]*len(waffles)
    waffles_list = list(range(0,len(waffles)))
    waffles['X'] = waffles_list


    #create a label list for each bubble 
    label = [i+'('+str(j)+')'+':'+str(k) for i,j,k in zip(waffles.location,
                                                              waffles.frequency,
                                                                    waffles.percent)]                


    colour = ['#3366CC', '#DC3912', '#FF9900', '#109618', '#990099', '#0099C6', 
              '#DD4477', '#66AA00', '#B82E2E', '#316395']


    colours = colour[:int(len(waffle_labels))]

    fig = plt.figure(FigureClass=Waffle, figsize=(10,10), rows=5, columns = 20, 
                         title={
                    'label': "Hits in " + str(year_pick),
                        'color': '#bf365b',
                        'loc': 'left',
                        'fontdict': {
                            'fontsize': 20,
                                'fontweight': 'bold',
                        }
                        },                                
                values=waffle_values, 
                   colors=colours, 
                   labels= label,
                   facecolor='#DDDDDD',
                   legend={
                       'loc': 'lower left',
                           'bbox_to_anchor': (0, -0.4),
                           'framealpha': 0,
                           'ncol': len(colours),
                           'fontsize': 12,
                   } )         
    plt.rcParams.update({'axes.facecolor':'gray'}) #this get ignored; why
    st.pyplot(fig)   
    plt.clf() 
    plt.close() 


