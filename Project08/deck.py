
from flashcard import Flashcard

# YOUR FIRST CUSTOM CLASS

class Deck:
    """
    Deck object, stores a collection of flashcards
    Purpose: To store a collection of flashcards
    3 custom functions
    """
    def __init__(self, name):
        """
        Construct a deck with a name
        :param name: Name of the deck
        """
        self.name = name
        self.cards = []

    def __str__(self):
        '''
        returns a string representation of the deck
        :return: String representation of the deck
        '''
        return f"{self.name} -- {len(self.cards)} cards, {len(self.get_due_cards())} cards due"

    def add_card(self, front, back):
        '''
        Add a card to the deck
        :param front: Front of the card
        :param back: Back of the card
        adds back and front of a flashcard
        '''
        card = Flashcard(front, back)
        self.cards.append(card)
        self.cards.sort()  # Ensure sorted order

    def load_from_file(self, filename):
        """
        Load cards from a file
        :param filename: Name of the file
        """
        try:
            file = open(filename, 'r')
            for line in file:
                front, back, days, timer = line.strip().split(',')
                card = Flashcard(front, back, int(days), int(timer))
                self.cards.append(card)
            self.cards.sort()
            file.close()
        except FileNotFoundError:
            print(f"Error: {filename} not found.")

    def get_due_cards(self):
        """
        Get all cards that are due for review
        :return: List of cards that are due for review
        """
        return [card for card in self.cards if card.days_until_review == 0]


# YOUR SECOND CUSTOM CLASS

class CollectionOfDecks:
    """
    Collection of decks, stores a collection of decks
    Purpose: To store a collection of decks
    3 custom functions
    """
    def __init__(self):
        """
        Construct a deck with a name
        :param name: Name of the deck as a dictionary
        """
        self.decks = {}

    def __str__(self):
        """
        returns a string representation of the collection
        :return: String representation of the collection
        """
        return '\n'.join(str(deck) for deck in self.decks.values())

    def add_deck(self, name):
        """
        Add a deck to the collection
        :param name: Name of the deck
        """
        if name in self.decks:
            print(f"Error: Deck '{name}' already exists.")
        else:
            self.decks[name] = Deck(name)

    def load_from_file(self, filename):
        """
        Load decks from a file
        :param filename: Name of the file
        """
        try:
            file = open(filename, 'r')
            for line in file:
                deck_name = line.strip()
                if deck_name:
                    deck = Deck(deck_name)
                    deck.load_from_file(f"{deck_name}.dk")
                    self.decks[deck_name] = deck
            file.close()
        except FileNotFoundError:
            print(f"Error: {filename} not found.")

    def advance_day(self):
        """
        Advance all cards in all decks by one day
        used for keeping use of spaced repitition
        """
        for deck in self.decks.values():
            for card in deck.cards:
                if card.days_until_review > 0:
                    card.days_until_review -= 1
