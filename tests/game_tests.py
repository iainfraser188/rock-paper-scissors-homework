import unittest
from models.game import *
from models.player import *



class TestGame(unittest.TestCase):

    def setUp(self): 
        self.player_1 = Player("Player_1","rock")
        self.player_2 = Player("player_2","scissors")
        self.player_3 = Player("player_2","paper")
        self.game_1 = Game(self.player_1,self.player_2)
        self.game_2 = Game(self.player_1,self.player_3)

    def test_player_1_winner(self):
        self.assertEqual("player 1 wins",self.game_1.determin_winner(self.player_1,self.player_2))
 

    def test_player_2_wins(self):
        self.assertEqual("player 2 wins",self.game_2.determin_winner(self.player_1,self.player_3))

    def testDraw(self):
        self.assertEqual("it's a draw",self.game_1.determin_winner(self.player_1,self.player_1))
