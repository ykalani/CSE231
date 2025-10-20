#######################################################################################################################
#
# Computer Project 07
#
#
# This program is a simulation of the card game UNO.
# The program will create a deck of UNO cards and shuffle them.
# The program will start by displaying a banner
# The user will be prompted to enter the number of players (2-5) and the game will begin.
# Each player will be dealt 5 cards from the deck.
# the game consists of special cards such as Skip, Reverse, +2, Wild, and Wild Draw Four that can change the play
# the user will either play a card from their hand or draw a card from the deck.
# The game will continue until a player has no cards left in their hand.
# The user will be prompted to play another round or exit the game.
#
#
#######################################################################################################################

from uno import Card, Deck, Player


def banner():
    """
    Used to display the banner at the start of the game.
    Takes no arguments.
    prints the banner when called. returns nothing.
    """
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
    """
    Used to display the current game state which includes the number of cards in each player's hand.
    Args:
        my_players: list of the players and card they have in their hand.
    returns nothing
    prints the game state when called.
    """
    print("\nGame state:")
    for i in my_players:
        print(f"{i.name} - {len(i.hand)} cards")


def is_card_valid(color, card_value, playable_cards):
    '''
    Used to check if the card the user wants to play is a valid card.
    Args:
        color: types of colors in the game (Red, Green, Blue, Yellow, Wild)
        card_value: different values of cards in the game (0-9, Skip, Reverse, +2, Color Change, +4)
        playable_cards: card that can be played by the user

    Returns: True if the card is valid, False if the card is not valid.

    '''

    if (color in ['Red', 'Green', 'Blue', 'Yellow', 'Wild']
            and card_value in [str(i) for i in range(10)]
            + ['Skip', 'Reverse', '+2', "Color Change", '+4']):

        for card in playable_cards:
            if color == card.color and card_value == card.value:
                return True
        return False
    else:
        return False


def next(turn, reverse, num_players):
    '''
    Used to determine the next player's turn.
    Args:
        turn: used to determine the current player's turn
        reverse: to tell whether the game is going forward or backward
        num_players: to tell the number of players in the game

    Returns:
        updated turn order for the next player
    '''
    return next_turn(turn, reverse, num_players)


def next_turn(turn, reverse, num_players):
    """
    Used to determine the next player's turn.
    Args:
        turn: used to determine the current player's turn
        reverse: to tell whether the game is going forward or backward
        num_players: to tell the number of players in the game

    Returns:
        turn: updated turn order for the next player

    """
    if reverse == -1:
        if turn == 0:
            turn = num_players - 1
        else:
            turn = turn - 1
    else:
        if turn == num_players - 1:
            turn = 0
        else:
            turn = turn + 1
    return turn


def has_won(my_players, turn):
    """
    print the winner of the game
    Args:
        my_players: list of players and cards
        turn which players move it is

    Returns:
    prints when and which player won the game
    """
    print(f"\n-----{my_players[turn].name} has won the round-----")


def first_prompt():
    '''
    Used to prompt the user to play a game of UNO.
    Returns:
        True if Uno, false if not
    '''
    prompt = input("\n:~Do you want to play a game of UNO? (yes/no) ~:")
    if prompt.lower() == "yes":
        return True
    else:
        return False


def ending():
    '''
    Used to print a message when the user decides to end the game.
    Returns:
        prints a message when the user decides to end the game.
    '''
    print("Thanks for playing!\nGo Green!! Go White!!")


def another_round(prompt):
    '''
    Used to prompt the user to play another round of UNO.
    Returns:
        True if want to play uno false elsewise
    '''
    if prompt.lower() == "yes":
        return True
    else:
        return False


def num_players_int(num_players):
    '''
    Used to prompt the user to enter the number of players in the game.
    Args:
        num_players: the number of players in the game
    Returns:
        num_players: the number of players in the game
    '''
    num_players = int(num_players)
    return num_players


def main():
    banner()
    prompt = first_prompt()

    while prompt:

        num_players = str(input("\n:~Enter number of players (2-5) ~:"))  # why did I have to make this a string :(
        while num_players not in ['2', '3', '4', '5']:
            print("Please enter a number between 2 and 5.")
            num_players = str(input("\n:~Enter number of players (2-5) ~:"))

        num_players = num_players_int(num_players)

        my_players = []
        my_deck = Deck()
        for i in range(num_players):
            my_players.append(Player(i + 1))
            for n in range(5):
                my_players[i].draw_card(my_deck)
        pile = []
        pile.append(my_deck.deal_card())

        turn = 0
        players = len(my_players)
        reverse = 1  # 1 for forward, -1 for reverse
        color = ""
        card_value = ""
        while True:

            if len(my_players[turn].hand) == 0:
                has_won(my_players, turn)
                break
            playable_cards = []
            print(f"\n{my_players[turn].name}'s turn. Current card: {pile[-1]}")
            print(f"\tYour hand: {my_players[turn].hand}")
            for card in my_players[turn].hand:
                if (card.color == pile[-1].color or card.value == pile[-1].value
                        or card.color == "Wild" or color == card.color):
                    playable_cards.append(card)

            if len(my_players[turn].hand) == 0:
                has_won(my_players, turn)
                break

            if len(playable_cards) == 0:
                if my_deck.is_empty():
                    my_deck.reset_deck(pile)
                    pile = []
                    pile.append(my_deck.deal_card())

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

                    if my_deck.is_empty():
                        my_deck.reset_deck(pile)
                        pile = []
                        pile.append(my_deck.deal_card())

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

                        if my_deck.is_empty():
                            my_deck.reset_deck(pile)
                            pile = []
                            pile.append(my_deck.deal_card())

                        for i in range(4):
                            my_players[turn].draw_card(my_deck)
                        turn = next(turn, reverse, num_players)
                        pile.append(card)
                        game_state(my_players)
                        continue

                pile.append(card)

                if len(my_players[turn].hand) == 0:
                    has_won(my_players, turn)
                    break

                turn = next(turn, reverse, num_players)
            game_state(my_players)

        prompt = input("\n:~Do you want to play another round? (yes/no) ~:")
        prompt = another_round(prompt)
    ending()


# DO NOT MODIFY THE FOLLOWING 2 LINES.
# DO NOT WRITE ANYTHING AFTER THE FOLLOWING 2 LINES OF CODES
# All your code should be either in the main function
# or in another function.
if __name__ == "__main__":
    main()


