import webbrowser
import time
import os
import os.path
import ast
import sys

online_features = False

# First number is for main version features, Second is for overall list release wave, third is for total number of games, last is for fun :)
Version = "3.2.11.7"

categories = {
    "Driving": [
        ["Slow Roads", "https://slowroads.io/"],
    ],

    "Shooter": [
        ["Deadshot FPS", "https://deadshot.io/"],
        ["Knockoff Fortnite", "https://1v1.lol/"],
        ["3D Aim Trainer", "https://app.3daimtrainer.com/quick-play"],
        ["Superhot Prototype", "https://superhotgame.com/superhot-prototype"],
    ],

    "Horror": [
        ["Slide in The Woods", "https://horrorgames.io/slide-in-the-woods"],
    ],

    "Exploration": [
        ["Geogussr Free", "https://openguessr.com/"],
        ["Minecraft V1.8.8", "https://eaglercraft.com/mc/1.8.8/"],
        ["Trippy AI Generated Minecraft", "https://oasis.decart.ai/welcome"],
    ],

    "Puzzle": [
        ["what beats rock?", "https://www.whatbeatsrock.com/"],
    ],

    "Easy-to-run": [
        ["Best Paper.io", "https://paper-io.com/conflict/"],
    ],

    "Custom": [],
}

def list_categories():
    print("Available categories:")
    for i, category in enumerate(categories.keys(), 1):
        print(f"{i}. {category}")

def list_items(category):
    if category in categories:
        print(f"Items in {category} category:")
        for i, item in enumerate(categories[category], 1):
            print(f"{i}. {item[0]}")
    else:
        print("Invalid category")

def open_item(category, item_index):
    if category in categories and 0 <= item_index < len(categories[category]):
        url = categories[category][item_index][1]
        webbrowser.open(url)
    else:
        print("Invalid item")

def load_custom_category():
    if os.path.isfile("custom.txt"):
        with open("custom.txt", "r") as file:
            custom_items = ast.literal_eval(file.read())
            categories["Custom"] = custom_items

def add_custom_url():
    name = input("Enter the name of the custom URL: ")
    print("""

""")
    url = input("Enter the custom URL: ")
    print("""

""")
    categories["Custom"].append([name, url])
    with open("custom.txt", "w") as file:
        file.write(str(categories["Custom"]))

def main():
    load_custom_category()
    
    while True:
        print("""

""")
        print("\n1. List categories")
        print("2. Add custom URL")
        print("3. Exit")
        print("""


""")
        choice = input("Enter Selection: ")
        print("\n")
        print("\n")
        print("\n")

        if choice == "1":
            list_categories()
            selected_category_index = int(input("Select category number: ")) - 1
            print("""

""")
            selected_category = list(categories.keys())[selected_category_index]
            
            list_items(selected_category)
            selected_item_index = int(input("Select an item number: ")) - 1
            
            open_item(selected_category, selected_item_index)
        elif choice == "2":
            add_custom_url()
        elif choice == "3":
            break
        else:
            print("Invalid entry. Please try again.")

if __name__ == "__main__":
    main()