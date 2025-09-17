#######################################################################################################################
#
# Computer Project 07
#
#######################################################################################################################



# Use these in your input statement
"\n:~Enter number of players (2-5) ~:"
"\t:~Choose a card color (Red, Green, Blue, Yellow, or Wild) ~:"
"\t:~Choose a card value (0-9, Skip, Reverse, +2, Color Change, +4) ~:"
"\t:~Choose a new color (Red, Green, Blue, Yellow) ~:"
"\t:~Choose a valid color (Red, Green, Blue, Yellow) ~:"
"\n:~Do you want to play a game of UNO? (yes/no) ~:"
"\n:~Do you want to play another round? (yes/no) ~:"

# Use these in your print statement
"Please enter a number between 2 and 5."
"\n{}'s turn. Current card: {}"
"\tYour hand: {}"
"\tPlayable cards: {}"
"\tInvalid card choice. Please choose a valid card from your hand."
"\tNo playable cards. Drawing a card."
"\nGame state:"
"\t{} is skipped!"
"\tDirection reversed!"
"\t{} draws two cards!"
"\tColor Changed to {}!"
"\t{} draws four cards!"
"\n-----{player.name} has won the round-----"
"Thanks for playing!\nGo Green!! Go White!!"


from uno import Card, Deck, Player

def banner():
    banner = """🌟🌟🌟 Welcome to the *Ultimate UNO Showdown*! 🌟🌟🌟

    💥 Prepare yourself for a thrilling, card-flipping adventure
    where alliances waver, strategies unfold, and only the
    sharpest tactician will claim the ultimate victory! 💥

    💥 Will you reverse the tide, skip ahead of your rivals,
    or drop that Wild Draw Four at the perfect moment to leave
    them in disarray? Let the games begin! 💥
    """
    print(banner)

def game_state(my_players):
    print("\nGame state:")
    for i in my_players:
        print(f"{i.name} - {len(i.hand)} cards")

def is_card_valid(color, card_value, playable_cards):
    if color in ['Red', 'Green', 'Blue', 'Yellow', 'Wild'] and card_value in [str(i) for i in range(10)] + ['Skip','Reverse','+2',"Color Change",'+4']:
        for card in playable_cards:
            if color == card.color and card_value == card.value:
                return True
        return False
    else:
        return False

def next(turn, reverse, num_players):
    return nextTurn(turn, reverse, num_players)

def nextTurn(turn, reverse, num_players):
    if reverse == -1:
        if turn == 0:
            turn = num_players - 1
        else :
            turn = turn - 1
    else :
        if turn == num_players - 1:
            turn = 0
        else :
            turn = turn + 1
    return turn


def skip(turn, reverse, num_players):
    turn = next(turn, reverse, num_players)
    turn = next(turn, reverse, num_players)
    return turn

def main():
    banner()
    prompt = input("\n:~Do you want to play a game of UNO? (yes/no) ~:")
    if prompt.lower() == "yes":
       prompt = True
    else:
        prompt = False

    while prompt:

        num_players = str(input("\n:~Enter number of players (2-5) ~:"))  # why did I have to make this a string :(
        while num_players not in ['2', '3', '4', '5']:
            print("Please enter a number between 2 and 5.")
            num_players = str(input("\n:~Enter number of players (2-5) ~:"))

        num_players = int(num_players)


        my_players = []
        my_deck = Deck()
        for i in range(num_players):
            my_players.append(Player(i+1))
            for n in range(5):
                my_players[i].draw_card(my_deck)
        pile = []
        pile.append(my_deck.deal_card())

        turn = 0
        players = len(my_players)
        reverse = 1 # 1 for forward, -1 for reverse
        color = ""
        card_value = ""
        while True:
            playable_cards = []
            print(f"\n{my_players[turn].name}'s turn. Current card: {pile[-1]}")
            print(f"\tYour hand: {my_players[turn].hand}")
            for card in my_players[turn].hand:
                if card.color == pile[-1].color or card.value == pile[-1].value or card.color == "Wild" or color == card.color:
                    playable_cards.append(card)
            if len(playable_cards) == 0:
                my_players[turn].draw_card(my_deck)
                print("\tNo playable cards. Drawing a card.")
                game_state(my_players)
                turn = next(turn, reverse, num_players)
                continue

            print(f"\tPlayable cards: {playable_cards}")

            not_valid = True
            while not_valid:
                color = input("\t:~Choose a card color (Red, Green, Blue, Yellow, or Wild) ~:")
                card_value = input("\t:~Choose a card value (0-9, Skip, Reverse, +2, Color Change, +4) ~:")
                if is_card_valid(color, card_value, playable_cards):
                    not_valid = False
                else:
                    print("\tInvalid card choice. Please choose a valid card from your hand.")
                    print(f"\tPlayable cards: {playable_cards}")
                    continue

            card = Card(color, card_value)
            if card in my_players[turn].hand:
                my_players[turn].hand.remove(card)
                if card.value == "Reverse":
                    print("\tDirection reversed!")
                    reverse = reverse * -1
                    turn = next(turn, reverse, num_players)
                    pile.append(card)
                    game_state(my_players)
                    continue

                if card.value == "+2":
                    turn = next(turn, reverse, num_players)
                    print(f"\t{my_players[turn].name} draws two cards!")
                    for i in range(2):
                        my_players[turn].draw_card(my_deck)
                    turn = next(turn, reverse, num_players)
                    pile.append(card)
                    game_state(my_players)
                    continue

                if card.value == "Skip":
                    turn = next(turn, reverse, num_players)
                    print(f"\t{my_players[turn].name} is skipped!")
                    turn = next(turn, reverse, num_players)
                    pile.append(card)
                    game_state(my_players)
                    continue

                if card.color == "Wild":
                    color = input("\t:~Choose a new color (Red, Green, Blue, Yellow) ~:")
                    while color not in ['Red', 'Green', 'Blue', 'Yellow', 'Wild']:
                        color = input("\t:~Choose a valid color (Red, Green, Blue, Yellow) ~:")
                    card.change_color(color)
                    print(f"\tColor Changed to {color}!")
                    if card.value == "+4":
                        turn = next(turn, reverse, num_players)
                        print(f"\t{my_players[turn].name} draws four cards!")
                        for i in range(4):
                            my_players[turn].draw_card(my_deck)
                        turn = next(turn, reverse, num_players)
                        pile.append(card)
                        game_state(my_players)
                        continue

                pile.append(card)

                if len(my_players[turn].hand) == 0:
                    print(f"\n-----{my_players[turn].name} has won the round-----")
                    break

                turn = next(turn, reverse, num_players)
            game_state(my_players)


        prompt = input("\n:~Do you want to play another round? (yes/no) ~:")
        if prompt.lower() == "yes":
            prompt = True
        else:
            prompt = False
    print("Thanks for playing!\nGo Green!! Go White!!")



# DO NOT MODIFY THE FOLLOWING 2 LINES.
# DO NOT WRITE ANYTHING AFTER THE FOLLOWING 2 LINES OF CODES
# All your code should be either in the main function
# or in another function.
if __name__ == "__main__":
    main()


