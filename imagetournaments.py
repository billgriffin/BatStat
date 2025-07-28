""" Diamond image for all tournaments """

import matplotlib.pyplot as plt
from hittingAvgs import hittingpercentages
import streamlit as st


#-------------------------------------------------------------------------
""" create graphic for each  tournament """

def imagetournaments (tournament) :        
    title = tournament['tournament'].loc[tournament.index[0]]        
    
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
        "axes.facecolor":"gray",
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
    
    """ import variable values """
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
   
    #---------------------------------------------
    ## setup lines on image
    #leftline = plt.Line2D((335,210),(442,65),lw=2.5, color = 'k')
    #rightline = plt.Line2D((335,455),(442,65),lw=2.5, color = 'k')
    #ax = plt.gca()
    
    #plt.gca().add_line(leftline)
    #plt.gca().add_line(rightline)
    #-------------------------------------------
    ### import data here ###
    left = leftfield(tournament) #left field, left infield
    #print(f"this is the left values [from tournament] for imagetournaments: {left}")
    leftcenter = left_centerfield(tournament)
    center = centerfield(tournament)
    rightcenter = right_centerfield(tournament)
    right = rightfield(tournament)
    
    ## outcomes list
    walk = walk(tournament)
    sacrifice = sacrifice(tournament)
    fielder_choice = fielder_choice(tournament)
    single = single(tournament)
    double = double(tournament)
    triple = triple(tournament)
    homer = homer(tournament)   
    ba = hittingpercentages(tournament)
    obp = hittingpercentages(tournament)        
    #----------------------------------------------------tournament
    
    # data
    # xxx[hits][total]
    left_values = [left[0][0],left[0][1]] #left field, left infield
    print(f"this is the left_values for imagetournaments: {left_values}")
    leftcenter_values = [leftcenter[0][0],leftcenter[0][1]] 
    center_values = [center[0][0],center[0][1]] 
    rightcenter_values = [rightcenter[0][0],rightcenter[0][1]] 
    right_values = [right[0][0],right[0][1]]     
    leftin_values = [left[1][0],left[1][1]] 
    leftcenter_in_values = [leftcenter[1][0],leftcenter[1][1]]  
    centerin_values = [center[1][0],center[1][1]] 
    rightcenter_in_values = [rightcenter[1][0],rightcenter[1][1]]       
    rightin_values = [right[1][0],right[1][1]]           
    
    # labels
    leftfield = 'Left'
    leftcenterfield = 'Left\nCenter'
    centerfield = 'Center'
    rightcenterfield = 'Right\nCenter'
    rightfield = 'Right'
    
    leftfielddata = str(left_values[0])+'-'+str(left_values[1])  #hits - total
    leftcenterfielddata = str(leftcenter_values[0])+'-'+str(leftcenter_values[1]) 
    centerfielddata = str(center_values[0])+'-'+str(center_values[1]) 
    rightcenterfielddata = str(rightcenter_values[0])+'-'+str(rightcenter_values[1]) 
    rightfielddata = str(right_values[0])+'-'+str(right_values[1])  
    
    leftinfield =  str(leftin_values[0])+'-'+str(leftin_values[1])
    leftcenterinfield = str(leftcenter_in_values[0])+'-'+str(leftcenter_in_values[1])
    centerinfield =  str(centerin_values[0])+'-'+str(centerin_values[1])
    rightcenterinfield = str(rightcenter_in_values[0])+'-'+str(rightcenter_in_values[1])
    rightinfield = str(rightin_values[0])+'-'+str(rightin_values[1])    
    
    walkslabel = 'Walk = ' + str(walk)
    saclabel = 'Sacrifice =  ' + str(sacrifice)
    fielderlabel =  'Fielder\'s Choice  =  ' + str(fielder_choice)
    single = 'Single = ' + str(single)
    double = 'Double = ' + str(double)
    triple = 'Triple = ' + str(triple)
    homer = 'Home Run = '+ str(homer)
    ba = 'Batting Average: '+ str(ba[0])
    obp = 'On Base Percentage: '+ str(obp[1])      
       
    # placement390
    plt.text(50, 64, leftfield, fontsize=16, color='k', fontweight='bold')
    plt.text(150, 25, leftcenterfield, fontsize=16, color='k', fontweight='bold')
    plt.text(300, 8, centerfield, fontsize=16, color='k', fontweight='bold')
    plt.text(440, 25, rightcenterfield, fontsize=16, color='k', fontweight='bold')
    plt.text(570, 64, rightfield, fontsize=16, color='k', fontweight='bold')
    single
    plt.text(135, 175, leftfielddata, fontsize=16, color='k', fontweight='bold')
    plt.text(192, 60, leftcenterfielddata, fontsize=16, color='k', fontweight='bold')
    plt.text(305, 115, centerfielddata, fontsize=16, color='k', fontweight='bold')
    plt.text(445, 60, rightcenterfielddata, fontsize=16, color='k', fontweight='bold')
    plt.text(500, 175, rightfielddata, fontsize=16, color='k', fontweight='bold')
    
    plt.text(250, 333, leftinfield, fontsize=15, color='k', fontweight='bold')
    plt.text(270, 263, leftcenterinfield, fontsize=15, color='k', fontweight='bold')
    plt.text(323, 325, centerinfield, fontsize=15, color='k', fontweight='bold')
    plt.text(365, 263, rightcenterinfield, fontsize=15, color='k', fontweight='bold')
    plt.text(387, 333, rightinfield, fontsize=15, color='k', fontweight='bold')   
    
    plt.text(44, 330, walkslabel, fontsize=15, color='k', fontweight='bold')
    plt.text(44, 350, saclabel, fontsize=15, color='k', fontweight='bold')
    plt.text(44, 370, fielderlabel, fontsize=15, color='k', fontweight='bold')
    plt.text(44, 390, single, fontsize=15, color='k', fontweight='bold')
    plt.text(44, 410, double, fontsize=15, color='k', fontweight='bold')
    plt.text(44, 430, triple, fontsize=15, color='k', fontweight='bold')
    plt.text(44, 450, homer, fontsize=15, color='k', fontweight='bold')
    
    plt.text(495, 380,title, fontsize=20, color='#FF8C02', fontweight='bold', style='italic')
    plt.text(485, 410, ba, fontsize=15, color='#55B2FF', fontweight='bold')  
    plt.text(485, 430, obp, fontsize=15, color='#55B2FF', fontweight='bold')                
    #---------------------------------------------------
       
    
    fig = ax.get_figure()
    st.pyplot(fig)   
    plt.clf() 
    plt.close() 
