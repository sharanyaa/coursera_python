# Mini-project #6 - Blackjack - Sharanya
# LINK TO GAME: http://www.codeskulptor.org/#user40_jFsGWs7Gn0idO9D.py
import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = "Begin: Hit or Stand?"
newdeal = ""
score = 0
player_hand = []
dealer_hand = []
game_deck = []
# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}
# define card class
class Card:
    def __init__(self, suit, rank):
        
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            #print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.hand = []	# create Hand object

    def __str__(self):
        if len(self.hand)==0 :
            return "Hand is empty"
        else:
            res = "Hand contains "
            for i in range(len(self.hand)):
                res = res + str(self.hand[i]) + " "
            return res
    def add_card(self, card):
        self.hand.append(card)	# add a card object to a hand

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        hand_value = 0
        num_aces = 0
        for card in self.hand:
            v = VALUES[card.get_rank()]
            if(v == 1):
                num_aces += 1
            hand_value += v	# compute the value of the hand, see Blackjack video
        if(num_aces==0):
            return hand_value
        else:
            if(hand_value + 10 <=21):
                return hand_value + 10
            else:
                return hand_value        
            
    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        n = len(self.hand)if (len(self.hand)<=5) else 5
        i = 0
        while i < n:
            card = self.hand[i]
            card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(card.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(card.suit))
            canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
            pos[0] += 75
            i += 1
# define deck class 
class Deck:
    def __init__(self):
        self.deck = []	# create a Deck object
        for s in SUITS:
            for r in RANKS:
                c = Card(s, r)
                self.deck.append(c)
        
    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.deck)    # use random.shuffle()

    def deal_card(self):
        return self.deck.pop()	# deal a card object from the deck
    
    def __str__(self):
        s = "Deck contains "
        for card in self.deck:	# return a string representing the deck
            s= s + str(card) + " "
        return s

#define event handlers for buttons
def deal():
    global outcome, in_play, game_deck, player_hand, dealer_hand, newdeal, score
    game_deck = Deck()
    player_hand = Hand()
    dealer_hand = Hand()
    newdeal = ""
    # your code goes here
    game_deck.shuffle()
    if (in_play):
        outcome = "You left a game and lost! New Deal?"
        score -= 1
    else:
        outcome = "Begin: Hit or Stand?"
    i = 0
    while i<2:
        player_hand.add_card(game_deck.deal_card())
        dealer_hand.add_card(game_deck.deal_card())
        i += 1
    #print "Player's " + str(player_hand)
    #print "Dealer's Hand contains " + str(dealer_hand.hand[1])
    in_play = True

def hit():
    global game_deck, player_hand, dealer_hand, outcome, newdeal, in_play, score
    # replace with your code below
    if(in_play):
        if(player_hand.get_value() <= 21):
            player_hand.add_card(game_deck.deal_card())
            #print "Hit!"
            outcome = "Hit!"
        # if the hand is in play, hit the player
        # if busted, assign a message to outcome, update in_play and score
        if(player_hand.get_value() > 21):
            in_play = False
            score -= 1
            #print "You have busted, DEALER WINS!\n"  
            outcome = "You have busted, DEALER WINS!"
            newdeal = "New Deal?"
        
def stand():
    global game_deck, player_hand, dealer_hand, outcome, newdeal, in_play, score
    if(in_play):
        newdeal = ""
        outcome = "Stand"
        # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
        # assign a message to outcome, update in_play and score
        if(player_hand.get_value() > 21):
            in_play = False
            score -= 1
            #print "You have busted, DEALER WINS!\n"
            outcome = "You have busted, DEALER WINS!"
            newdeal = "New Deal?"
        else:
            while(dealer_hand.get_value() <= 17):
                dealer_hand.add_card(game_deck.deal_card())
            if(dealer_hand.get_value() > 21):
                in_play = False
                score += 1
                #print "Dealer has busted, YOU WIN!\n"
                outcome = "Dealer has busted, YOU WIN!"
                newdeal = "New Deal?"
            else:
                if(player_hand.get_value() <= dealer_hand.get_value()):
                    in_play = False
                    score -= 1
                    #print "You have lost, DEALER WINS!\n"
                    outcome = "You have lost, DEALER WINS!"
                    newdeal = "New Deal?"
                else:
                    in_play = False
                    score += 1
                    #print "Dealer has lost, YOU WIN!\n"
                    outcome = "Dealer has lost, YOU WIN!"
                    newdeal = "New Deal?"

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    global game_deck, player_hand, dealer_hand, score
#    card = Card("S", "A")
#    card.draw(canvas, [300, 300])
    canvas.draw_text('Blackjack', (180, 60), 50, 'Black')
    canvas.draw_text('Dealer:', (20, 105), 30, 'White')
    canvas.draw_text(outcome , (20, 330), 30, 'Orange')
    canvas.draw_text(newdeal , (20, 360), 25, 'Orange')
    canvas.draw_text('Player:', (20, 415), 30, 'White')
    canvas.draw_text('Score: ' + str(score), (20, 580), 30, 'White')
    dealer_hand.draw(canvas, [20, 130])
    player_hand.draw(canvas, [20, 440])
    if(in_play):
        # image, image_center_loc, image_size, position_on_canvas, size_on_canvas
        canvas.draw_image(card_back, [108, 48], CARD_BACK_SIZE, [55, 178], CARD_BACK_SIZE)

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 700)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
rules = "Values: Aces = 1 or 11 (player's choice). Kings, Queens, Jacks = 10. Other cards = card number. "
rules += "Goal: During a round/hand of Blackjack, the player plays against a dealer with the goal of building a hand"
rules += "(a collection of cards) whose cards have a total value that is higher than the value of the dealer's hand, but not over 21. "
rules += "The player and the dealer are each dealt two cards initially. The player may then ask for the dealer to repeatedly hit his hand by dealing him another"
rules += " card. If, at any point, the value of the player's hand exceeds 21, the player is busted and loses immediately."
rules += "At any point prior to busting, the player may stand and the dealer will then hit his hand until the value of "
rules += "his hand is 17 or more. If the "
rules += "dealer busts, the player wins. Otherwise, the player and dealer then compare the values of their hands and the"
rules += " hand with the higher value wins. The dealer wins ties."
label1 = frame.add_label(rules, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric
