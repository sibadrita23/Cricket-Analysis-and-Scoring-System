import unittest
from src.scoring import CricketScoring

class TestCricketScoring(unittest.TestCase):
    def test_update_score(self):
        score = CricketScoring()
        score.update_score(30, 2, 5)
        self.assertEqual(score.get_score(), "Score: 30/2 in 5 overs")

if __name__ == "__main__":
    unittest.main()
