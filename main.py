
import random
from select import select







destinations = ["Buffalo", "Syracuse", "Albany", "Manhatten", "Boston", "Baltimore", "Myrtle Beach", "Miami", "Houston"]
restaurants = ["Anchor Bar", "Pies Guys", "Carrabba's", "Minetta Tavern", "The Smith", "Carmine's", "Ms. Cheezious", "KOMODO", "Coyo Taco", "The Pit Room", "Pinkerton's Barbecue"]
mode_of_transportation = ["Car", "Private Jet", "Walk", "Motorcycle", "Bicycle", "Limo", "Train", "Boat"]
entertainment = ["Comedy Show", "Mall", "Parkour", "Museum", "Live Music", "Beach", "Rent Jet Skis", "Go-Karts", "Mini-Golf", "Park"]

day_trip_generator = [destinations, restaurants, mode_of_transportation, entertainment]

def greeting():
    print("""
                Day Trip Generator
            """)
greeting()


def select_destinations(destination_list):
    confirm_bool = True
    while confirm_bool:
        selected_destination = random.choice(destination_list)
        user_input = input(f"{selected_destination} has been chosen as your destination! Do you accept this destination? (Type Yes or No) : ")
        if user_input == "No":
            destination_list.remove(selected_destination)
        else:
            confirm_bool = False
    return selected_destination

chosen_destination = select_destinations(destinations)   
print(f"{chosen_destination} it is!")



def select_restaurant(restaurants_list):
    confirm_bool = True
    while confirm_bool:
        selected_restaurant = random.choice(restaurants_list)
        user_input = input(f"{selected_restaurant} has been chosen as your restaurant! Do you accept this restaurant? (Type Yes or No) : ")
        if user_input == "No":
            restaurants_list.remove(selected_restaurant)
        else:
            confirm_bool = False
    return selected_restaurant

chosen_restaurant = select_restaurant(restaurants)
print(f"{chosen_restaurant} it is!")

def select_mode_of_transportation(mode_of_transportation_list):
    confirm_bool = True
    while confirm_bool:
        selected_mode_of_transportation = random.choice(mode_of_transportation_list)
        user_input = input(f"{selected_mode_of_transportation} has been chosen as your mode of transportation! Do you accept this mode of transportation? (Type Yes or No) : ")
        if user_input == "No":
            mode_of_transportation_list.remove(selected_mode_of_transportation)
        else:
            confirm_bool = False
    return selected_mode_of_transportation

chosen_mode_of_transportation = select_mode_of_transportation(mode_of_transportation)
print(f"{chosen_mode_of_transportation} it is!")

def select_entertainment(entertainment_list):
    confirm_bool = True
    while confirm_bool:
        selected_entertainment = random.choice(entertainment_list)
        user_input = input(f"{selected_entertainment} has been chosen as your entertainment! Do you accept this form of entertainment? (Type Yes or No) : ")
        if user_input == "No":
            entertainment_list.remove(selected_entertainment)
        else:
            confirm_bool = False
    return selected_entertainment

chosen_entertainment = select_entertainment(entertainment)
print(f"{chosen_entertainment} it is!")


def day_trip_questions():
    chosen_destination = select_destinations(destinations)
    chosen_restaurant = select_restaurant(restaurants)
    chosen_mode_of_transportation = select_mode_of_transportation(mode_of_transportation)
    chosen_entertainment = select_entertainment(entertainment)


choices_list = [chosen_destination, chosen_restaurant, chosen_mode_of_transportation, chosen_entertainment]

def displaying_choices(choices_list):
    for choices in choices_list:
        print(choices)


def confirm_choices():
    conf_bool = True
    while conf_bool:
        user_input = input("Are you satisfied with these choices? (Type Yes or No) : ")
        if user_input  == "Yes":
            print(f"You have chosen {chosen_destination} for your destination, {chosen_restaurant} for your restaurant, {chosen_mode_of_transportation} as your mode of transportation and {chosen_entertainment} as your entertainment. Enjoy your adventure!" )
            break
        if user_input == "No":
            day_trip_questions()
            continue
        else:
            print("Invalid selection. Please try again." )



def run_confirmation_sequence(day_trip_generator):
    displaying_choices(choices_list)
    confirm_choices()
    



run_confirmation_sequence(day_trip_generator)



