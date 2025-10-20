class Flashcard(object):
    """
    Flashcard object, stores front, back sides and time until review
    """
    def __init__(self, front, back, days=0, timer=1):
        """
        Construct a flashcard, front and back sides are required
        Always starts with 0 days until review
        :param front: Text on front of card (prompt)
        :param back: Text on back of card (answer)
        :param days: Days until review
        :param timer: Most recent review timer
        """
        self.front = front
        self.back = back
        self.wait_time = timer
        self.days_until_review = days

    def __str__(self):
        """
        :return: String representation of card
        """
        return f"{self.front:<20} | {self.back:<65.64} | {self.days_until_review} days until review"


    def __repr__(self):
        """
        :return: String representation of card when used in the shell
        """
        return str(self)


    def __lt__(self, other):
        """
        :param other: Another Flashcard object
        :return: True if self is lexicographically less than other
        """
        return (self.front, self.back) < (other.front, other.back)

    def update_review_time(self, response):
        """
        Based on the user response, updates the time until next review
        :param response: Can be either 1,2,3,4 for correct, incorrect, hard, easy
        """
        if response == '1':
            self.wait_time *= 2
        elif response == '2':
            self.wait_time = 1
        elif response == '3':
            self.wait_time *= 1
        elif response == '4':
            self.wait_time *= 4
        self.days_until_review = self.wait_time

