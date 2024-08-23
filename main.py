from src.data_loader import load_data
from src.analysis import player_performance, team_performance
from src.scoring import CricketScoring

if __name__ == "__main__":
    data = load_data('data/match_data.csv')
    
    # Analyze player and team performance
    print(player_performance(data))
    print(team_performance(data))

    # Live Scoring
    live_score = CricketScoring()
    live_score.update_score(100, 2, 15)
    print(live_score.get_score())
