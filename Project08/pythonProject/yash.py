class Piano:
    def __init__(self,brand="Steinway",model="D"):
        self.brand = brand
        if num_keys < 0:
            self.num_keys = 88
        else:
            self.num_keys = num_keys
            self.num_keys = 88
        self.is_playing = is_playing

    def play(self):
        if self.is_playing = True
            return "Playing"
        else:
            return "Not Playing"
    def __str__(self):
        return f"{self.brand} {self.model} with {self.num_keys} keys"