""" Batting Average and On Base Percentage """

def hittingpercentages(tournament):
    outs =  tournament.query('hit == "0"').hit.count()   # number of outs
    hits =   tournament.query('hit == "1"').hit.count()    # number of hits    
    sac =    tournament.query('hit == "3"').hit.count()    # sac fly
    walks = tournament.query('hit == "2"').hit.count()  # number of walks
    ba = round(hits/(hits + outs),3)
    obp = round((walks + hits)/ (walks + hits + outs),3)
    #print(f'The batting average was: {ba:.3f} and the OBP was: {obp:.3f}')
    return ba, obp