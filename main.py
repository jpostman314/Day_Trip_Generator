
import random
from select import select







destinations = ["Buffalo", "Syracuse", "Albany", "Manhatten", "Boston", "Baltimore", "Myrtle Beach", "Miami", "Houston"]
restaurants = ["Anchor Bar", "Pies Guys", "Carrabba's", "Minetta Tavern", "The Smith", "Carmine's", "Ms. Cheezious", "KOMODO", "Coyo Taco", "The Pit Room", "Pinkerton's Barbecue"]
mode_of_transportation = ["Car", "Private Jet", "Walking", "Motorcycle", "Bicycle", "Limo", "Train", "Boat"]
entertainment = ["Comedy Show", "Mall", "Parkour", "Museum", "Live Music", "Beach", "Rent Jet Skis", "Go-Karts", "Mini-Golf", "Park"]

day_trip_generator = [destinations, restaurants, mode_of_transportation, entertainment]

def greeting():
    print("""
                                                            Day Trip Generator
            """)
    print("This program will randomly select a destination, restaurant, mode of transportation and form of entertainment to create a random day trip for you to enjoy! Once each selection has been chosen at random, you will be able to accept or deny that choice. I hope you enjoy the adventure the Day Trip Generator creates for you!!")
    print("")

greeting()


def select_destinations(destination_list):
    confirm_bool = True
    while confirm_bool:
        selected_destination = random.choice(destination_list)
        user_input = input(f"{selected_destination} has been chosen as your destination! Do you accept this destination? (Type Yes or No) : ")
        if user_input == "Yes":
            confirm_bool = False
        elif user_input == "No":
            print("")
            print("Okay, lets try again. ")
            print("")
            destination_list.remove(selected_destination)
        else:
            print("")
            print("Invalid selection. Please try again. ")
            print("")
            
    return selected_destination
chosen_destination = select_destinations(destinations)   
print("")
print(f"{chosen_destination} is the destination you'll be going to!")
print("")




def select_restaurant(restaurants_list):
    confirm_bool = True
    while confirm_bool:
        selected_restaurant = random.choice(restaurants_list)
        user_input = input(f"{selected_restaurant} has been chosen as your restaurant! Do you accept this restaurant? (Type Yes or No) : ")
        if user_input == "Yes":
            confirm_bool = False
        elif user_input == "No":
            print("")
            print("Okay, lets try again.")
            print("")
            restaurants_list.remove(selected_restaurant)
        else:
            print("")
            print("Invalid selection. Please try again." )
            print("")
    return selected_restaurant
chosen_restaurant = select_restaurant(restaurants)
print("")
print(f"{chosen_restaurant} is where you'll be eating!")
print("")


def select_mode_of_transportation(mode_of_transportation_list):
    confirm_bool = True
    while confirm_bool:
        selected_mode_of_transportation = random.choice(mode_of_transportation_list)
        user_input = input(f"{selected_mode_of_transportation} has been chosen as your mode of transportation! Do you accept this mode of transportation? (Type Yes or No) : ")
        if user_input == "Yes":
            confirm_bool = False
        elif user_input == "No":
            print("")
            print("Okay, lets try again.")
            print("")
            mode_of_transportation_list.remove(selected_mode_of_transportation)
        else:
            print("")
            print("Invalid selection. Please try again." )
            print("")
    return selected_mode_of_transportation
chosen_mode_of_transportation = select_mode_of_transportation(mode_of_transportation)
print("")
print(f"{chosen_mode_of_transportation} will be your mode of transportation!")
print("")



def select_entertainment(entertainment_list):
    confirm_bool = True
    while confirm_bool:
        selected_entertainment = random.choice(entertainment_list)
        user_input = input(f"{selected_entertainment} has been chosen as your entertainment! Do you accept this form of entertainment? (Type Yes or No) : ")
        if user_input == "Yes":
            confirm_bool = False
        elif user_input == "No":
            print("")
            print("Okay, lets try again.")
            print("")
            entertainment_list.remove(selected_entertainment)
        else:
            print("")
            print("Invalid selection. Please try again." )
            print("")
    return selected_entertainment
chosen_entertainment = select_entertainment(entertainment)
print("")
print(f"{chosen_entertainment} will be your entertainment!")
print("")


choices_list = [chosen_destination, chosen_restaurant, chosen_mode_of_transportation, chosen_entertainment]

def displaying_choices(choices_list):
    for choices in choices_list:
        print(choices)
    print("")

displaying_choices(choices_list)


def confirm_choices():
    conf_bool = True
    while conf_bool:
        user_input = input("Are you satisfied with these choices? (Type Yes or No) : ")
        if user_input  == "Yes":
            print("")
            print(f"You have chosen {chosen_destination} for your destination, {chosen_restaurant} for your restaurant, {chosen_mode_of_transportation} as your mode of transportation and {chosen_entertainment} as your entertainment. Enjoy your adventure!" )
            print("")
            exit()
        elif user_input == "No":
            print("")
            print("Sorry these choices don't work for you. Lets start over.")
            print("")
            break
        else:
            print("")
            print("Invalid selection. Please try again." )
            print("")

confirm_choices()

def new_select_destinations(destination_list):
    confirm_bool = True
    while confirm_bool:
        selected_destination = random.choice(destination_list)
        user_input = input(f"{selected_destination} has been chosen as your new destination! Do you accept this destination? (Type Yes or No) : ")
        if user_input == "Yes":
            confirm_bool = False
        elif user_input == "No":
            print("")
            print("Okay, lets try again. ")
            print("")
            destination_list.remove(selected_destination)
        else:
            print("")
            print("Invalid selection. Please try again. ")
            print("")
            
    return selected_destination
new_chosen_destination = new_select_destinations(destinations)   
print("")
print(f"{new_chosen_destination} is the new destination you'll be going to!")
print("")




def new_select_restaurant(restaurants_list):
    confirm_bool = True
    while confirm_bool:
        selected_restaurant = random.choice(restaurants_list)
        user_input = input(f"{selected_restaurant} has been chosen as your new restaurant! Do you accept this restaurant? (Type Yes or No) : ")
        if user_input == "Yes":
            confirm_bool = False
        elif user_input == "No":
            print("")
            print("Okay, lets try again.")
            print("")
            restaurants_list.remove(selected_restaurant)
        else:
            print("")
            print("Invalid selection. Please try again." )
            print("")
    return selected_restaurant
new_chosen_restaurant = new_select_restaurant(restaurants)
print("")
print(f"{new_chosen_restaurant} is where you'll be eating!")
print("")


def new_select_mode_of_transportation(mode_of_transportation_list):
    confirm_bool = True
    while confirm_bool:
        selected_mode_of_transportation = random.choice(mode_of_transportation_list)
        user_input = input(f"{selected_mode_of_transportation} has been chosen as your new mode of transportation! Do you accept this mode of transportation? (Type Yes or No) : ")
        if user_input == "Yes":
            confirm_bool = False
        elif user_input == "No":
            print("")
            print("Okay, lets try again.")
            print("")
            mode_of_transportation_list.remove(selected_mode_of_transportation)
        else:
            print("")
            print("Invalid selection. Please try again." )
            print("")
    return selected_mode_of_transportation
new_chosen_mode_of_transportation = new_select_mode_of_transportation(mode_of_transportation)
print("")
print(f"{new_chosen_mode_of_transportation} will be your new mode of transportation!")
print("")



def new_select_entertainment(entertainment_list):
    confirm_bool = True
    while confirm_bool:
        selected_entertainment = random.choice(entertainment_list)
        user_input = input(f"{selected_entertainment} has been chosen as your new entertainment! Do you accept this form of entertainment? (Type Yes or No) : ")
        if user_input == "Yes":
            confirm_bool = False
        elif user_input == "No":
            print("")
            print("Okay, lets try again.")
            print("")
            entertainment_list.remove(selected_entertainment)
        else:
            print("")
            print("Invalid selection. Please try again." )
            print("")
    return selected_entertainment
new_chosen_entertainment = new_select_entertainment(entertainment)
print("")
print(f"{new_chosen_entertainment} will be your new entertainment!")
print("")


new_choices_list = [new_chosen_destination, new_chosen_restaurant, new_chosen_mode_of_transportation, new_chosen_entertainment]

def day_trip_questions():
    new_chosen_destination = new_select_destinations(destinations)
    print("")
    print(f"{new_chosen_destination} is the new destination you'll be going to!")
    print("")
    new_chosen_restaurant = new_select_restaurant(restaurants)
    print("")
    print(f"{new_chosen_restaurant} is where you'll be eating!")
    print("")
    new_chosen_mode_of_transportation = new_select_mode_of_transportation(mode_of_transportation)
    print("")
    print(f"{chosen_mode_of_transportation} will be your new mode of transportation!")
    print("")
    new_chosen_entertainment = new_select_entertainment(entertainment)
    print("")
    print(f"{new_chosen_entertainment} will be your new entertainment!")
    print("")




def displaying_new_choices(new_choices_list):
    for choices in new_choices_list:
        print(choices)
    print("")

displaying_new_choices(new_choices_list)

def confirm_new_choices():
    conf_bool = True
    while conf_bool:
        user_input = input("Are you satisfied with these new choices? (Type Yes or No) : ")
        if user_input  == "Yes":
            print("")
            print(f"You have chosen {new_chosen_destination} for your destination, {new_chosen_restaurant} for your restaurant, {new_chosen_mode_of_transportation} as your mode of transportation and {new_chosen_entertainment} as your entertainment. Enjoy your adventure!" )
            print("")
            conf_bool = False
        elif user_input == "No":
            print("")
            print("Sorry these choices don't work for you. Lets start over.")
            print("")
            day_trip_questions()
        else:
            print("")
            print("Invalid selection. Please try again." )
            print("")

confirm_new_choices()
