import streamlit as st
import pandas as pd
import plotly.express as px
from pywaffle import Waffle
import matplotlib.pyplot as plt

# For bar
def outcome_plot_bar(hits, year_pick):
    bar_x = dict(sorted(hits.items(), key=lambda item:item[1], reverse=True))
    bar_labels = list(bar_x.keys())
    bar_values = list(bar_x.values())
    bar_values_sum = sum(bar_values)
    bar_values_percent = [(value/bar_values_sum) for value in bar_values]
    bar_values_percent_format = [f"{value:2.1%}" for value in bar_values_percent]
    all_outcomes_bar = px.bar(x=bar_labels, 
                              y=bar_values,
                              title='Outcomes' + " in " + str(year_pick),
                              color=bar_labels,
                              text=bar_values_percent_format,
                              labels={'y': 'Total', 'x': 'Outcome', 'text': 'Percent'},
                              color_discrete_sequence=px.colors.qualitative.G10                              
                              )
    all_outcomes_bar.update_traces(textfont_color='black')
    all_outcomes_bar.update_layout(title_font_color="#bf365b",
                                   legend=dict(title='Outcomes'),                                   
                                   legend_title_font_color="black",
                                   legend_font_color="black")
    all_outcomes_bar.update_layout(
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
           
    return all_outcomes_bar


# For pie 
def outcome_plot_pie(hits, year_pick):
    pie_labels = list(hits.keys())
    pie_values = list(hits.values())    
    all_outcomes_pie = px.pie(values=pie_values, 
                              names=pie_labels,
                              title='Outcomes' + " in " + str(year_pick),
                              color_discrete_sequence=px.colors.qualitative.G10, 
                              hole=.25)
    all_outcomes_pie.update_traces(textposition='inside', 
                                   textinfo='percent+label',
                                   insidetextorientation='horizontal',
                                   textfont_color="black")                                   
    all_outcomes_pie.update_layout(title_font_color="#bf365b",                                   
                                legend=dict(title='Outcomes'), 
                                legend_title_font_color="black",
                                legend_font_color = "black")  
    return all_outcomes_pie

# For  bubbles
def outcome_plot_bubbles(hits, year_pick):
    bubble_x_outcomes = dict(sorted(hits.items(), key=lambda item:item[1], reverse=True))
    bubble_outcome_labels = list(bubble_x_outcomes.keys())
    bubble_outcome_values = list(bubble_x_outcomes.values())
    bubble_outcome_values_sum = sum(bubble_outcome_values)
    bubble_outcome_values_percent = [(value/bubble_outcome_values_sum) for value in bubble_outcome_values]
    bubble_outcome_values_percent_format = [f"{value:2.1%}" for value in bubble_outcome_values_percent]
    
    bubbles_outcomes = pd.DataFrame(list(zip(bubble_outcome_labels, 
                                             bubble_outcome_values, 
                                             bubble_outcome_values_percent_format)), 
                           columns = ['location','frequency','percent'])

    bubbles_outcomes['Y'] = [1] * len(bubbles_outcomes)
    list_outcomes = list(range(0, len(bubbles_outcomes)))
    bubbles_outcomes['X'] = list_outcomes

    label = [i + '<br>' + str(j) + '<br>' + str(k) + '%' for i, j, k in zip(bubbles_outcomes.location,
                                                                           bubbles_outcomes.frequency,
                                                                           bubbles_outcomes.percent)]

    all_outcomes_bubbles = px.scatter(bubbles_outcomes, x='X', y='Y',
                                      title = 'Frequency and Percentage of Outcomes' + " in " + str(year_pick),
                                      color='location', color_discrete_sequence=px.colors.qualitative.G10,
                                      size='frequency', text=label, size_max=80)
    all_outcomes_bubbles.update_layout(width=900, height=320,
                      margin = dict(t=30, l=0, r=0, b=0),
                      showlegend=False,
                      title_font_color="#bf365b",
                      font_color= "black")
    all_outcomes_bubbles.update_traces(textposition='top center')
    all_outcomes_bubbles.update_xaxes(showgrid=False, zeroline=False, visible=False)
    all_outcomes_bubbles.update_yaxes(showgrid=False, zeroline=False, visible=False)

    return all_outcomes_bubbles

# For Waffles
def outcome_plot_waffles(hits, year_pick):
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
    waffle_x_outcomes = dict(sorted(hits.items(), key=lambda item:item[1], reverse=True))

    waffle_outcome_labels = list(waffle_x_outcomes.keys())  
    waffle_outcome_values = list(waffle_x_outcomes.values()) 

    waffle_outcome_values_sum = sum(waffle_outcome_values)
    waffle_outcome_values_percent = []
    waffle_outcome_values_percent_format = []  
    waffle_outcome_values_percent = [((value/waffle_outcome_values_sum)) for value in waffle_outcome_values]
    for value in (waffle_outcome_values_percent):
        waffle_outcome_values_percent_format.append(f"{value:2.1%}")

    # Create df 
    waffles_outcomes = pd.DataFrame(list(zip(waffle_outcome_labels, 
                                                 waffle_outcome_values,                            
                                                 waffle_outcome_values_percent_format)), 
                                        columns = ['location','frequency','percent'])

    waffles_outcomes['Y'] = [1]*len(waffles_outcomes)
    list_outcomes = list(range(0,len(waffles_outcomes)))
    waffles_outcomes['X'] = list_outcomes


    #List for each waffle 
    label = [i+'('+str(j)+')'+':'+str(k) for i,j,k in zip(waffles_outcomes.location,
                                                              waffles_outcomes.frequency,
                                                                    waffles_outcomes.percent)]                


    colour = ['#3366CC', '#DC3912', '#FF9900', '#109618', 
              '#990099', '#0099C6', '#DD4477', '#66AA00', '#B82E2E', '#316395']


    colours = colour[:int(len(waffle_outcome_labels))]
    
    waffle_length = int(len(waffle_outcome_labels))
    print(waffle_length)

    fig = plt.figure(FigureClass=Waffle, figsize=(10,10), rows= 7, columns = 25, 
                         title={
                    'label': "Outcomes in " + str(year_pick),
                        'color': '#bf365b',
                        'loc': 'left',
                        'fontdict': {
                            'fontsize': 20,
                                'fontweight': 'bold',
                        }
                        },                                
                values=waffle_outcome_values, 
                   colors=colours, 
                   labels= label,
                   facecolor='#DDDDDD',
                   legend={
                       'loc': 'lower left',
                           'bbox_to_anchor': (0, -0.25),
                           'framealpha': 0,
                           'ncol': 3,
                           'fontsize': 12,
                   } )       
    
    #bounding box  (.0, -.04)
    plt.rcParams.update({'axes.facecolor':'gray'}) #this get ignored; why
    st.pyplot(fig)   
    plt.clf() 
    plt.close() 
