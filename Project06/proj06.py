#######################################################################################################################
#
# Computer Project 06
#
# Description:
# Creates a program to manage zoos with a menu and several details
# prompts user to ask expenses and the number of the zoos
# enter the zoos name
# reads the files
# gives the users 4 options
# one to display which zoo is the healthiest
# one to display which zoo is the most expensive
# one to show each zoos individual information
# one to allow the program to be quit
#
#######################################################################################################################
import csv
from operator import itemgetter

# Lists of valid personalities and games

"""
# Use these in your input statement
"\n:~Enter the Expenses file ~:"
"\n:~Enter the number of Zoo files available (at least two) ~:"
"\n:~Enter a Zoo name ~:"
"\n:~Input a choice ~:"

":~Enter a zoo ~:"
":~Enter an animal species ~:"
":~Enter the animal’s name ~:"

# Use these in your print statement
"Error. File does not exist"
"There must be a minimum of two files."
".csv"  # needs to be added to the zoo name
"Error. File {} does not exist"

"Invalid zoo or does not exist."
"Invalid species or does not exist."
"Invalid name or does not exist."

"{}% of {} Zoo animals are sick. The sickest being {}."
" and "
"{} Zoos take better care of their animals!!!"
"{} Zoo takes better care of its animals!!!"
"{} Zoo spends ${} a month."
"{} zoos are the most expensive zoos!!!"
"{} Zoo is the most expensive zoo!!!"
"There are no twins in the zoo."
"Invalid choice. Choice must be a number or X."
"Thank you for your time at the Zoo!!!"
"\n{} and {} are twins separated at birth!!!\n"
"{}\n***************"
"Species ID: {}"
"Species: {}"
"Sex: {}\n"
"\nThey both:"
"\t\tAre {} years old."
"\t\tAre {}."
"\t\tTheir favorite game is {}."
"\t\tTheir favorite food is {}."
"\n{}\n***************"
"Species ID: {}"
"Species: {}"
"Age: {} years old"
"Sex: {}"
"Health: {}"
"Years at Zoo: {}"
"Favorite game: {}"
"Favorite food: {}"
"Personality: {}"
"Money spent per month: ${:,.2f}"
"""


# Write all your function definitions before the main
def banner():
    """
    displays banner when needed at the start of the program
    """
    banner = '''
        Zoos of the World!!
    ******************************************************************************************************************
    *                 ,-._                       **         (\-"""-/)           **      /\                 /\        *
    *              _.-'  '--.                    **          |     |            **     / \'._    (\_/)   _.'/ \       *
    *            .'      _  -`\_                 **          \ ^ ^ /  .-.       **    /_.''._'--('.')--'_.''._\      *
    *           / .----.`_.'----'                **           \_o_/  / /        **    | \_ / `;=/ " \=;` \ _/ |      *
    *           ;/     `                         **          /`   `\/  |        **     \/ `\__|`\___/`|__/`  \/      *
    *          /_;                               **         /       \  |        **      `      \(/|\)/       `       *
    *                                            **         \ (   ) /  |        **              " ` "                *
    *       ._      ._      ._      ._           **        / \_) (_/ \ /        **************************************
    *    _.-._)`\_.-._)`\_.-._)`\_.-._)`\_.-._   **       |   (\-/)   |         *
    *                                            **       \  --^o^--  /         *
    *    o                                       **        \ '.___.' /          *
    *   o      ______/~/~/~/__           /((     **       .'  \-=-/  '.         *
    *     o  // __            ====__    /_((     **      /   /`   `\   \        *
    *    o  //  @))       ))))      ===/__((     **     (//./       \.\\)        *
    *       ))           )))))))        __((     **      `"`         `"`        *
    *       \\     \)     ))))    __===\ _((      ********************************
    *        \\_______________====      \_((      *
    *                                    \((     *
    **********************************************
    '''
    print(banner)


def menu():
    """
    displays the menu when prompted
    """
    choices = ''' 
        Menu: 
            1: The healthiest zoo
            2: The most expensive zoo
            3: Individual information
            4: Twins separated at birth
            X: Quit the program\n'''
    print(choices)


def zoo(zoo_files):
    """
    Prompts for zoo name for all zoos
    asks for all zoos data and opens and reads them, this appends it to files_data
    Adds and stores them in files_data
    """
    files_data = []
    for i in range(int(zoo_files)):
        while True:
            zoo_name = input("\n:~Enter a Zoo name ~:")
            try:
                zoos = open(f"{zoo_name}.csv", "r")
                data = zoos.read()
                files_data.append((zoo_name, data))  # Store zoo name with data
                zoos.close()
                break  # Break out of the while loop if file is found and read successfully
            except FileNotFoundError:
                print(f"Error. File {zoo_name}.csv does not exist")
    return files_data


def sick_calc(sick_animals, total_animals):
    """
    Uses formula to calculate the percentage of sick animals
    returns percent sick
    needs the sick and total for calculations
    """
    if total_animals > 0:
        percentage_sick = int((sick_animals / total_animals) * 100)
    else:
        percentage_sick = 0
    return percentage_sick


def calculate_sick_percentage(files_data):
    """
    Checks if each animal in each zoo is sick
    Calculates the total sick percentage in a zoo
    Prints out the statements
    """
    zoo_stats = {}
    for zoo_name, data in files_data:
        total_animals = 0
        sick_animals = 0
        species_sick_counts = {}

        lines = data.split('\n')
        headers = lines[0].split(',')

        for line in lines[1:]:
            if line.strip():  # Skip empty lines
                animal_data = line.split(',')
                animal_dict = dict(zip(headers, animal_data))
                total_animals += 1
                if animal_dict['Health'].lower() == 'sick':
                    sick_animals += 1
                    species = animal_dict['Species ID']
                    if species in species_sick_counts:
                        species_sick_counts[species] += 1
                    else:
                        species_sick_counts[species] = 1

        percentage_sick = sick_calc(sick_animals, total_animals)


def species_files():
    """
    asks for species file
    prompts and reprompts for species id
    returns the species file
    """
    while True:
        species_file = input("\n:~Enter the Species ID file ~:")
        try:
            species = open(f"{species_file}", "r")
            break
        except FileNotFoundError:
            print("Error. File does not exist")
    return species


def expenses():
    """
    asks for expenses file
    prompts and reprompts for expenses
    returns the expenses file
    """
    while True:
        expenses_file = input("\n:~Enter the Expenses file ~:")
        try:
            expenses = open(f"{expenses_file}", "r")
            break
        except FileNotFoundError:
            print("Error. File does not exist")
    return expenses


def zoo_file():
    """
    asks for all zoo files needed
    Prompts for zoo name for all zoos
    reprompts
    returns all zoo files in zoo_files
    """
    zoo_files = input("\n:~Enter the number of Zoo files available (at least two) ~:")
    while True:
        if int(zoo_files) < 2:
            print("There must be a minimum of two files.")
            zoo_files = input("\n:~Enter the number of Zoo files available (at least two) ~:")
        else:
            break
    return zoo_files


def personality():
    """
    stores and sorts through the possible traits
    it shows the personal games that can be done
    eventually returns games
    """
    personality = ["shy", "courageous", "aggressive", "calm", "needy", "curious", "independent"]
    return personality


def dict_create(pers, games):
    traits = dict(zip(pers, games))
    expenses_data = expenses()
    return traits


def games():
    """
    stores and sorts through the personality so that is can loop through the possible traits
    it shows the personal games that can be done
    eventually returns games
    """
    games = ["swim", "platforms", "handfeeding", "puzzles", "fake hunting", "swings", "hiding"]
    return games


def calculate_monthly_expenses(files_data, expenses_data):
    """
    used to calc expenses monthly
    files data and expenses pass
    goes through and divides by 12 to get monthly expenses
    """
    zoo_expenses = {}

    for zoo_name, data in files_data:
        total_expense = 0

        lines = data.split('\n')
        headers = lines[0].split(',')

        for line in lines[1:]:
            if line.strip():  # Skip empty lines
                animal_data = line.split(',')
                animal_dict = dict(zip(headers, animal_data))

                species = animal_dict['Species ID']
                food = animal_dict['Favorite Food']
                years_at_zoo = int(animal_dict['Years at Zoo'])

                # Calculate the expense for this animal
                animal_expense = expenses_data['species'][species] / 12
                food_expense = expenses_data['food'][food] / 12
                worker_pay = expenses_data['workers']['pay_per_year'] / 12

                total_expense += animal_expense + food_expense + worker_pay

        zoo_expenses[zoo_name.title()] = round(total_expense, 2)

    # Sort zoo_expenses alphabetically by zoo name
    sorted_zoo_expenses = dict(sorted(zoo_expenses.items()))

    # Determine the most expensive zoo
    max_expense = max(sorted_zoo_expenses.values())
    most_expensive_zoos = [zoo for zoo, expense in sorted_zoo_expenses.items() if expense == max_expense]
    most_expensive_zoos.sort()

    # Print each zoo's expenses
    for zoo, expense in sorted_zoo_expenses.items():
        print(f"{zoo} Zoo spends ${expense:,.2f} a month.")

    # Print the most expensive zoo
    most_expensive_zoos_str = ' and '.join(most_expensive_zoos)
    print(f"{most_expensive_zoos_str} Zoo is the most expensive zoo!!!")
    print()


def x():
    """
    prints exit message
    this prompt is displayed when needed for time at the zoo
    returns via a print statement so no acutal return
    """
    print("Thank you for your time at the Zoo!!!")


def get_animal_details(files_data, expenses_data):
    '''
    uses files data to see the titile of the zoo and go through the zoo animal listings
    chcks if the zoo exists and if the data is valid
    return via print if it doesnt exist
    '''
    while True:
        zoo_name = input("\n:~Enter a zoo ~: ").title()
        zoo_data = None
        for name, data in files_data:
            if name.title() == zoo_name:
                zoo_data = data
                break

        if zoo_data is None:
            print("Invalid zoo or does not exist.")


def main():
    banner()
    pers = personality()
    game = games()
    traits = dict_create(pers, game)
    expenses_data = expenses()
    zoo_files = zoo_file()
    files_data = zoo(zoo_files)

    while True:
        menu()
        choice = input("\n:~Input a choice ~:")
        if choice.lower() == "x":
            x()
            break
        elif choice.lower() == "1":
            calculate_sick_percentage(files_data)
        elif choice.lower() == "2":
            calculate_monthly_expenses(files_data, expenses_data)
        elif choice.lower() == "3":
            get_animal_details(files_data, expenses_data)


# DO NOT MODIFY THE FOLLOWING 2 LINES.
# DO NOT WRITE ANYTHING AFTER THE FOLLOWING 2 LINES OF CODES
# All your code should be either in the main function
# or in a function.
if __name__ == "__main__":
    main()


