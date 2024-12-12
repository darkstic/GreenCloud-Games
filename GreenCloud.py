import webbrowser
import time

online_features=False

# First number is for main version features, Second is for overall list release wave, third is for total number of games.
Version="1.1.10"

games_list=[
    ["Placeholder"],# 0
    ["Slow Roads","https://slowroads.io/"],#                              1
    ["Deadshot FPS","https://deadshot.io/"],#                             2
    ["Knockoff Fortnite","https://1v1.lol/"],#                            3
    ["Best Paper.io","https://paper-io.com/conflict/"],#                  4
    ["Geogussr Free","https://openguessr.com/"],#                         5
    ["Minecraft V1.8.8","https://eaglercraft.com/mc/1.8.8/"],#            6
    ["Trippy AI Generated Minecraft","https://oasis.decart.ai/welcome"],# 7
    ["What beats rock?","https://www.whatbeatsrock.com/"],#               8
    ["3D Aim Trainer","https://app.3daimtrainer.com/quick-play"],#        9
    ["Superhot Prototype","https://superhotgame.com/superhot-prototype"],#10
]

listsize=len(games_list)

def game_menu():
    for x, sublist in enumerate(games_list[1:listsize],start=1):
        print(f"{x}: {games_list[x][0]}")

    print("""



""")# Large Spacer

    game_selection=input("Enter the number for the game you would like to play:  ")
    if game_selection=="v":
        print(Version)
        time.sleep(3)
        print("""
        
        """)
        game_menu()
    elif game_selection=="q":
        exit()
    elif game_selection=="s":
        print("""

""")
        suggestion=input("Enter your suggestion for the dev here:  ")
        if online_features==True:
            pointless_variable="Placeholder"
            # Enter future messaging function here
        else:
            print("Feedback Features are not yet available")
            time.sleep(2)
        game_menu()
    else:
        game_selection=int(game_selection)

        webbrowser.open(games_list[game_selection][1])

        time.sleep(1)
    game_menu()

game_menu()
