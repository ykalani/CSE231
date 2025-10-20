from flashcard import Flashcard
#################creating cards and review timer####################
# 2 lines from Biology.dk
line1 = "Homeostasis,Maintenance of a balance internal state,0,2"
line2 = "Biology,Study of life,2,8"

#---------------creating cards----------------
front,back,days,timer = line1.strip().split(",")
card1 = Flashcard(front, back, int(days))
print("card1:", card1)

front,back,days,time = line2.strip().split(",")
card2 = Flashcard(front, back, int(days))
print("card2:", card2)
input()
#---------------review cards and grade----------------
print("\n-----------------------------------------------------")
print("Card 1 front:",card1.front)
print("Card 1 back:",card1.back)
grade = '1' #correct
card1.update_review_time(grade)
print("\ncard1 after review with 1:", card1)

input()
grade = '2' #Incorrect
card1.update_review_time(grade)
print("\ncard1 after review with 2:", card1)
input()

grade = '3' #Hard
card1.update_review_time(grade)
print("\ncard1 after review with 3:", card1)

input()
grade = '4' #Easy
card1.update_review_time(grade)
print("\ncard1 after review with 4:", card1)
input()
#################creating one deck of cards####################
print("\n-----------------------------------------------------")
# here I'm using a list but the requirement should be a Custom Class that represents a
# collection of cards ------> what did we use in the Deck class for Project 7.
my_deck = [card1, card2]
print("Original deck:")
for card in my_deck:
    print(card)

my_deck.sort()
print("\nSorted deck:")
for card in my_deck:
    print(card)
input()

#################Creating a collection of decks####################
print("\n-----------------------------------------------------")
# 1 line from Vocab.dk
line3 = "Insular,Narrowly restricted in outlook or scope,2,2"
front,back,days,tim = line3.strip().split(",")
card3 = Flashcard(front, back, int(days))
print("card3:", card3)
input()

my_other_deck = [card3]

# here I'm using a list but the requirement should be a Custom Class that represents a
# collection of decks
my_collection = [my_deck, my_other_deck]


#################Final Thoughts####################
"""
- Option “D” might be a good starting point because it will help when testing. 
- Option “R” should be implemented next. Although it is the hardest to implement, 
it is also the most crucial to the program’s functionality. 
- Option “N” can be tackled right after because it is also related to reviewing. 
- The last few commands should be relatively simple.
"""


