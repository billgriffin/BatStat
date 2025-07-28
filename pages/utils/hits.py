import streamlit as st
import pandas as pd
import plotly.express as px

#Define the function for pie plot
def plot_pie(hits, year_pick):
    labels_pie = list(hits.keys())
    sizes_pie = list(hits.values())

    all_hits_pie = px.pie(values = sizes_pie, 
                        names = labels_pie, 
                        title = 'Location of hits'  + " in " + str(year_pick),   
                        color_discrete_sequence = px.colors.qualitative.G10,
                        hole = .25)
    all_hits_pie.update_traces(textposition='inside', textinfo='percent+label')
    all_hits_pie.update_layout(
                               title_font_color="#55B2FF",
                               legend=dict(title='Hit Locations')
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
    all_hits_bar.update_layout(
        title_font_color="#55B2FF",
        legend=dict(title='Hit Locations')
    )
    return all_hits_bar


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
                  title_font_color="#55B2FF"
                 )
    all_hits_bubbles.update_traces(textposition='top center')
    all_hits_bubbles.update_xaxes(showgrid=False, zeroline=False, visible=False)
    all_hits_bubbles.update_yaxes(showgrid=False, zeroline=False, visible=False)
    return all_hits_bubbles
