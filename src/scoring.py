class CricketScoring:
    def __init__(self):
        self.runs = 0
        self.wickets = 0
        self.overs = 0

    def update_score(self, runs, wickets, overs):
        """Update match score based on ball-by-ball updates."""
        self.runs += runs
        self.wickets += wickets
        self.overs += overs

    def get_score(self):
        """Return the current score of the match."""
        return f"Score: {self.runs}/{self.wickets} in {self.overs} overs"
