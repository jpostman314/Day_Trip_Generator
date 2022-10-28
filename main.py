
import random







destinations_list = ["Buffalo", "Syracuse", "Albany", "Manhatten", "Boston", "Baltimore", "Myrtle Beach", "Miami", "Houston"]
restaurants_list = ["Anchor Bar", "Pies Guys", "Carrabba's", "Minetta Tavern", "The Smith", "Carmine's", "Ms. Cheezious", "KOMODO", "Coyo Taco", "The Pit Room", "Pinkerton's Barbecue"]
mode_of_transportation_list = ["Car", "Private Jet", "Walk", "Motorcycle", "Bicycle", "Limo", "Train", "Boat"]
entertainment_list = ["Comedy Show", "Mall", "Parkour", "Museum", "Live Music", "Beach", "Rent Jet Skis", "Go-Karts", "Mini-Golf", "Park"]

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

winner = select_destinations(destinations_list)
print(f"{winner} it is!")

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

winner = select_restaurant(restaurants_list)
print(f"{winner} it is!")

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

winner = select_mode_of_transportation(mode_of_transportation_list)
print(f"{winner} it is!")

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

winner = select_entertainment(entertainment_list)
print(f"{winner} it is!")