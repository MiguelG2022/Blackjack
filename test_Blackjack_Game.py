import unittest
import BlackjackGame


class TestBlackjackGame(unittest.TestCase):

    def setUp(self):
        self.deckOne = BlackjackGame.Deck() 
        self.deckTwo = BlackjackGame.Deck()
        self.deckThree = BlackjackGame.Deck()
        self.playerOne = BlackjackGame.Hand()
        self.playerTwo = BlackjackGame.Hand()
        self.playerThree = BlackjackGame.Hand()

    def tearDown(self):
        pass
    
    def test_deck_size(self):
        self.assertEqual(len(self.deckOne.deck), 52)
        card = self.deckOne.deal()
        self.assertEqual(len(self.deckOne.deck), 51)
    
    def test_shuffle(self):
        self.deckThree.shuffle()
        self.assertNotEqual(self.deckTwo, self.deckThree)

    def test_Score(self):
        self.playerOne.add_card(BlackjackGame.Card("Hearts","Ace"))
        self.playerOne.add_card(BlackjackGame.Card("Diamonds","Ace"))
        self.playerOne.adjust_for_ace()
        self.assertEqual(self.playerOne.value, 12)
        self.playerTwo.add_card(BlackjackGame.Card("Spades","King"))
        self.playerTwo.add_card(BlackjackGame.Card("Clubs","Six"))
        self.assertEqual(self.playerTwo.value, 16)

    def test_hit(self):

        BlackjackGame.hit(self.deckThree, self.playerThree)
        self.assertEqual(len(self.deckThree.deck), 51)
        self.assertEqual(len(self.playerThree.cards), 1)

    

if __name__ == '__main__':
    unittest.main()