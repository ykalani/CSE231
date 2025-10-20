from animal import Animal

print   ("Animal Class")
class Dog(Animal):
    def __init__(self, name="Dogzilla", gender="Female", x=0, y=0, id=100):
        super().__init__(x, y, "Dog", id) # calls parent class constructor
        self.name = name
        self.gender = gender

    def about(self):

        return (f"Hi my name is {self.name}.\n"
                f"Animal Dog (ID: {self.id}) is at ({self.x}, {self.y}).\n"
                f"I'm your {self.gender.lower()} dog race watcher.")




class Panda(Animal):
    TALKS = {'newborn': "Hi master, my name is {}.",
             'feed': "Yummy !",
             'drink': "Tasty drink ~",
             'play': "Happy to have your company ~",
             'roll': "Weeeee! Watch me tumble toward destiny (or snacks)!",
             'default': "Hello, master! I'm feeling great!",
             'hunger': 'I am so hungry ~',
             'thirsty': 'Could you give me some drinks? Alcohol-free please ~',
             'loneliness': 'Could you stay with me for a little while ?',
             'tired': "I'm too hungry or thirsty to talk right now..."
             }

    def __init__(self, x=0, y=0, id=0, name="Fluffy", gender="Unknown", fur_color="Red", hunger=0, thirst=0,
                 loneliness=10):
        self.name = name
        self.gender = gender
        self.fur_color = fur_color
        self.hunger = hunger
        self.thirst = thirst
        self.loneliness = loneliness


# Define your Dog Class
"Hi my name is {}.\n{}.\nI'm your {} dog race watcher."

# Define your Panda Class

"Panda {} (ID: {}, Gender: {}, Fur Color: {})"
"Position: ({}, {})"
"Hunger: {}, Thirst: {}, Loneliness: {}"

"{}: {}"
