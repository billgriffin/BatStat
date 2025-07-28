import matplotlib.pyplot as plt
from hittingAvgs import hittingpercentages
import streamlit as st
import numpy as np

#helper function for importing data
def get_data(func, tournament):
    #print(f"This is the summaryimage tournament values: {tournament}")
    return func(tournament)

def imageSummary(tournament):
    from getHitsSummary import (
        leftfield, 
        left_centerfield, 
        centerfield, 
        right_centerfield, 
        rightfield, 
        walk, 
        sacrifice, 
        fielder_choice, 
        homer, 
        single, 
        double, 
        triple
    )
        
    # fields
    fields = [leftfield, left_centerfield, centerfield, right_centerfield, rightfield]
    fields_names = ['Left', 'Left Center', 'Center', 'Right Center', 'Right']
    field_values = np.array([get_data(field, tournament) for field in fields])
    #print(f"this is the field_values for summaryimage: {field_values}")    
    
    # outcomes
    outcomes = [walk, sacrifice, fielder_choice, single, double, triple, homer]
    #outcomes_names = ['Walk', 'Sacrifice', 'Fielder Choice', 'Single', 'Double', 'Triple', 'Homer']
    outcomes_values = np.array([get_data(outcome, tournament) for outcome in outcomes])
    
    # hitting averages
    ba = hittingpercentages(tournament)
    obp = hittingpercentages(tournament)        
    
    # image
    img = plt.imread('image/fieldimage.png')    
    
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
        "xtick.labelsize": 12,
        "ytick.labelsize": 12,
        "legend.fontsize": 12,
        "figure.titlesize": 16,
        "figure.titleweight": "bold",
        "figure.figsize": [10, 7.5],
        "figure.autolayout": True,
        "figure.facecolor": "#55B2FF",
        "figure.edgecolor": "#55B2FF"
    })
    
    fig, ax = plt.subplots(1)
    ax.imshow(img)
    ax.axis('off')
    
    # code to plot image and data goes here...
    #-------------------------------------------
    # import data here 
    
    left_values =                   field_values[0][0][0], field_values[0][0][1]  #using array
    #print(f"this is the left_values for summaryimage: {left_values}")
    leftin_values =                field_values[0][1][0], field_values[0][1][1]  #using array 
    leftcenter_values =         field_values[1][0][0], field_values[1][0][1]  
    leftcenter_in_values =    field_values[1][1][0], field_values[1][1][1]     
    center_values =              field_values[2][0][0], field_values[2][0][1] 
    centerin_values =           field_values[2][1][0], field_values[2][1][1]         
    rightcenter_values =      field_values[3][0][0], field_values[3][0][1]  
    rightcenter_in_values =  field_values[3][1][0], field_values[3][1][1]        
    right_values =                 field_values[4][0][0], field_values[4][0][1]            
    rightin_values =              field_values[4][1][0], field_values[4][1][1]           
                    
    # labels
    leftfield = fields_names[0] #'Left'
    leftcenterfield = fields_names[1] #'Left\nCenter'
    centerfield = fields_names[2] #'Center'
    rightcenterfield = fields_names[3] #'Right\nCenter'imshow
    rightfield = fields_names[4] #'Right'    
    
    leftfielddata = str(left_values[0])+'-'+str(left_values[1])
    leftcenterfielddata = str(leftcenter_values[0])+'-'+str(leftcenter_values[1]) 
    centerfielddata = str(center_values[0])+'-'+str(center_values[1]) 
    rightcenterfielddata = str(rightcenter_values[0])+'-'+str(rightcenter_values[1]) 
    rightfielddata = str(right_values[0])+'-'+str(right_values[1])
    
    leftinfield =  str(leftin_values[0])+'-'+str(leftin_values[1])
    leftcenterinfield = str(leftcenter_in_values[0])+'-'+str(leftcenter_in_values[1])
    centerinfield =  str(centerin_values[0])+'-'+str(centerin_values[1])
    rightcenterinfield = str(rightcenter_in_values[0])+'-'+str(rightcenter_in_values[1])
    rightinfield = str(rightin_values[0])+'-'+str(rightin_values[1])       
    
    # labels with values
    walkslabel = 'Walk = ' + str(outcomes_values[0])
    saclabel = 'Sacrifice =  ' + str(outcomes_values[1])
    fielderlabel =  'Fielder\'s Choice =  '+ str(outcomes_values[2])
    single = 'Single = ' + str(outcomes_values[3])
    double = 'Double = ' + str(outcomes_values[4])
    triple = 'Triple = ' + str(outcomes_values[5])
    homer = 'Home Run = '+ str(outcomes_values[6])    
    
    ba = 'Batting Average: '+ str(ba[0])  
    obp = 'On Base Percentage: '+ str(obp[1])       
    
    # title placement
    plt.text(50, 64, leftfield, fontsize=16, color='k', fontweight='bold')
    plt.text(150, 25, leftcenterfield, fontsize=16, color='k', fontweight='bold')
    plt.text(310, 8, centerfield, fontsize=16, color='k', fontweight='bold')
    plt.text(440, 25, rightcenterfield, fontsize=16, color='k', fontweight='bold')
    plt.text(570, 64, rightfield, fontsize=16, color='k', fontweight='bold')
    # data
    plt.text(135, 175, leftfielddata, fontsize=16, color='k', fontweight='bold')
    plt.text(187, 60, leftcenterfielddata, fontsize=16, color='k', fontweight='bold')
    plt.text(315, 115, centerfielddata, fontsize=16, color='k', fontweight='bold')
    plt.text(445, 60, rightcenterfielddata, fontsize=16, color='k', fontweight='bold')
    plt.text(500, 175, rightfielddata, fontsize=16, color='k', fontweight='bold')
    
    plt.text(250, 333, leftinfield, fontsize=15, color='k', fontweight='bold')
    plt.text(270, 263, leftcenterinfield, fontsize=15, color='k', fontweight='bold')
    plt.text(323, 325, centerinfield, fontsize=15, color='k', fontweight='bold')
    plt.text(365, 263, rightcenterinfield, fontsize=15, color='k', fontweight='bold')
    plt.text(387, 333, rightinfield, fontsize=15, color='k', fontweight='bold')       
   
    # text summary
    plt.text(44, 330, walkslabel, fontsize=15, color='k', fontweight='bold')
    plt.text(44, 350, saclabel, fontsize=15, color='k', fontweight='bold')
    plt.text(44, 370, fielderlabel, fontsize=15, color='k', fontweight='bold')
    plt.text(44, 390, single, fontsize=15, color='k', fontweight='bold')
    plt.text(44, 410, double, fontsize=15, color='k', fontweight='bold')
    plt.text(44, 430, triple, fontsize=15, color='k', fontweight='bold')
    plt.text(44, 450, homer, fontsize=15, color='k', fontweight='bold')
    
    plt.text(495, 380, 'Summary', fontsize=20, color='#FF8C02', fontweight='bold', style='italic')
    plt.text(485, 410, ba, fontsize=18, color="#55B2FF", fontweight='bold')  
    plt.text(485, 430, obp, fontsize=18, color="#55B2FF", fontweight='bold')     
    
    #---------------------------------------------------    
        
    fig = ax.get_figure()
    st.pyplot(fig)
    
    