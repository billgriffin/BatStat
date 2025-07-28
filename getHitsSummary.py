""" Cleaned and optimized """    

import pandas as pd
import plotly.express as px
import numpy as np
    

def get_field_values(tournament, location, ball):
    """Get field values based on location and ball type"""
    hits = tournament.query(f'hit == "1" & location == "{location}" & ball == "{ball}"').hit.count()
    outs = tournament.query(f'hit == "0" & location == "{location}" & ball == "{ball}"').hit.count()    
    return [hits, hits + outs]
#######################
def get_infield_values(tournament, location, ball):
    """Get field values based on location and ball type"""
    hits = tournament.query(f'hit == "1" & location == "{location}" & ball != "{ball}"').hit.count()
    outs = tournament.query(f'hit == "0" & location == "{location}" & ball != "{ball}"').hit.count()    
    return [hits, hits + outs]
###########################

def leftfield(tournament):
    """Get the values for left field"""
    left_values = get_field_values(tournament, "Left", "Fly") #calls the field function
    leftin_values = get_infield_values(tournament, "Left", "Fly") # calls the in_field function
    return left_values, leftin_values

def left_centerfield(tournament):
    """Get the values for left-center field"""
    left_center_values = get_field_values(tournament, "Left-center", "Fly")
    left_center_in_values = get_infield_values(tournament, "Left-center", "Fly")
    return left_center_values, left_center_in_values

def centerfield(tournament):
    """Get the values for center field"""
    center_values = get_field_values(tournament, "Center", "Fly")
    center_in_values = get_infield_values(tournament, "Center", "Fly")
    return center_values, center_in_values

def right_centerfield(tournament):
    """Get the values for right-center field"""
    right_center_values = get_field_values(tournament, "Right-center", "Fly")
    right_center_in_values = get_infield_values(tournament, "Right-center", "Fly")
    return right_center_values, right_center_in_values

def rightfield(tournament):
    """Get the values for right field"""
    right_values = get_field_values(tournament, "Right", "Fly")
    right_in_values = get_infield_values(tournament, "Right", "Fly")
    return right_values, right_in_values

def walk(tournament):
    """Get the number of walks"""
    walks = tournament.query('hit == "2" ').hit.count()
    return walks

def sacrifice(tournament):
    """Get the number of sacrifices"""
    sacrifices = tournament.query('hit == "3" ').hit.count()
    return sacrifices

def fielder_choice(tournament):
    """Get the number of fielder's choices"""
    choices = tournament.query('ball == "Fielder\'s Choice" ').hit.count()
    return choices

def single(tournament):
    """Get the number of singles"""
    singles = tournament.query('outcome == "Single" ').hit.count()
    return singles

def double(tournament):
    """Get the number of doubles"""
    doubles = tournament.query('outcome == "Double" ').hit.count()
    return doubles

def triple(tournament):
    """Get the number of triples"""
    triples = tournament.query('outcome == "Triple" ').hit.count()
    return triples

def homer(tournament):
    """ Get the number of home runs """
    homer = tournament.query('outcome == "Home Run" ').hit.count()   
    return homer

#############################################
#def prepare_data():
    #with open("./data/bat.csv", "r") as file:
        #result = pd.read_csv(file)#, engine="pyarrow")

    #HIT_VALUES = ['1', '1', '1', '1', '0','2', '3']

    #CONDITIONS = [
            #(result['outcome'] == 'Single'),
            #(result['outcome'] == 'Double'),
            #(result['outcome'] == 'Triple'),
            #(result['outcome'] == 'Home Run'),
            #(result['outcome'] == 'Out'), 
            #(result['outcome'] == 'Walk'), 
            #(result['outcome'] == 'Sacrifice')
            #]

    #result['hit'] = np.select(CONDITIONS, HIT_VALUES)

    #return result     

#tournament = prepare_data()
##print(single(values))
##print()
#print(leftfield(tournament))
#print(left_centerfield(tournament))
#print(centerfield(tournament))
#print(right_centerfield(tournament))
#print(rightfield(tournament))