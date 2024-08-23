import pandas as pd

def player_performance(data):
    """Calculate player performance like average runs, wickets, etc."""
    return data.groupby('player_name').agg({
        'runs': 'mean',
        'wickets': 'sum'
    })

def team_performance(data):
    """Analyze team performance based on scores and wickets."""
    return data.groupby('team').agg({
        'runs': 'sum',
        'wickets': 'sum'
    })
