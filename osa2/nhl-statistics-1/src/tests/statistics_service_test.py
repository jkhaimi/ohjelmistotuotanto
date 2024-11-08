import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri", "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(PlayerReaderStub())

    def test_pelaajat(self):
        player_names = [player.name for player in self.stats._players]
        expected_names = ["Semenko", "Lemieux", "Kurri", "Yzerman", "Gretzky"]
        self.assertEqual(player_names, expected_names)

    def test_pelaajienJoukkueet(self):
        player_teams = [player.team for player in self.stats._players]
        expected_teams = ["EDM", "PIT", "EDM", "DET", "EDM"]
        self.assertEqual(player_teams, expected_teams)

    def test_topPelaajat(self):
        top_players = self.stats.top(2)
        expected_top_names = ["Gretzky", "Lemieux", "Yzerman"]
        top_names = [player.name for player in top_players]
        self.assertEqual(top_names, expected_top_names)

if __name__ == "__main__":
    unittest.main()
