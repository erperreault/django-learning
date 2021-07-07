test_chart_path = 'viz/static/viz/test.png'

# these are separated because the BGG database has them formatted differently
stat_fields = [
    ('usersrated', 'Number of Ratings'),
    ('average', 'Average Rating'),
    ('bayesaverage', 'Bayesian Average Rating'),
    ('owned', 'BGG Owners'),
    ('averageweight', 'Average Complexity'),
]

data_fields = [
    ('yearpublished', 'Year Published'),
    ('minplayers', 'Min Players'),
    ('maxplayers', 'Max Players'),
    ('playingtime', 'Playing Time'),
    ('minplaytime', 'Min Play Time'),
    ('maxplaytime', 'Max Play Time'),
    ('age', 'Age'),
    ('boardgamepublisher', 'Publisher'),
]

# for displaying nicely formatted axis labels instead of the internal ones
nice_dict = {
    field[0]:field[1] for field in stat_fields+data_fields
    }