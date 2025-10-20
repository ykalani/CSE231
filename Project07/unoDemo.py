from uno import Card, Deck, Player

''' The basic process is this:
    1) You create a Deck instance, which is filled (automatically) with 60 Card instances
    2) You create a player with a player number as their name.
    2) You can deal those cards out of the deck into player hand, its hand is a list of cards
    3) You can manipulate cards as you add/remove/modify them from a hand
    4) You can compare cards
'''
#--------------------------------------------------------------------------------------
print("############Card Class demo:")
a_card = Card("Red", "1")
print("a_card:",a_card) # call the __str__

b_card = Card("Purple", "1")
print("b_card:",b_card) # call the __str__

c_card = Card("Wild", "+4")
print("Original c_card:",c_card) # call the __str__
print()
c_card.change_color("Red")
print("updated c_card:",c_card)
print("c_card new color:",c_card.color)
print()
# check if equal (will call __eq__ method)
if a_card == c_card:
    print(a_card,'is equal to',c_card)
else:
    print(a_card,'is not equal to',c_card)

# check if Card is valid. (will call __bool__ method)
if a_card:
    print("a_card is evaluated to True")
else:
    print("a_card is evaluated to False")

if b_card:
    print("b_card is evaluated to True")
else:
    print("b_card is evaluated to False")

print()

#--------------------------------------------------------------------------------------
print("############Deck Class demo:")
my_deck = Deck()
print()
print("======messy print a deck=====")
print(my_deck) # call the __str__

print("======pretty print a deck=====")
my_deck.display()

print('How many cards in the deck:',len(my_deck)) # call __len__ method

a_card = my_deck.deal_card()
print("Dealt card is:",a_card)
print('How many cards left in the deck:',len(my_deck))

print("Is the deck empty?",my_deck.is_empty())

# reset the same deck with a pile of cards
pile=[]
for i in range(5): # deal 5 cards to the pile
    pile.append(my_deck.deal_card())
my_deck.reset_deck(pile)
print("The new deck:",my_deck)
print()
#--------------------------------------------------------------------------------------
print("############Player Class demo:")
my_player = Player(1)
print("my_player:",my_player)

# deal some cards to the player
for i in range(3): # deal 3 cards to player hand
    my_player.draw_card(my_deck)
print("my_player after dealing 2 cards hands:",my_player)
print("my_player name:", my_player.name)
print("my_player hand:", my_player.hand)
print()


a_card = Card("Red","1")
b_card = Card("Wild","+4")
print("Does my_player hand has (Red 1):", a_card in my_player) # call __contains__
print("Does my_player hand has (Wild +4):", b_card in my_player) # call __contains__
print()

# play a specific card from player hand
c_card = my_player.play_card(b_card)
print("c_card:",c_card)
print("Does my_player hand has (Wild +4) now:", c_card in my_player) # call __contains__
print()
print("Did the player win?",my_player.has_won())




