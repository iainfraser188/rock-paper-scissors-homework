import unittest
from models.game import *
from models.player import *



class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player_1 = Player("iain","rock")
        self.player_2 = Player("steve","scissors")


    def test_player_has_name(self):
        self.assertEqual("iain",self.player_1.name) 
        self.assertEqual("steve",self.player_2.name)  

    def test_player_made_choice(self):
        self.assertEqual("rock",self.player_1.choice)
        self.assertEqual("scissors",self.player_2.choice)


  



        #  def setUp(self):
        
        # self.drink = Drink("beer", 2.00, 5)
        # self.food = Food("Burger", 4.99, 3)
        # self.customer = Customer("Frodo", 10.00, 28, 0)
        # self.customer_2 = Customer("Same", 10.00, 27, 5)