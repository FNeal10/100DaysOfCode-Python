print("WELCOME TO TREASURE ISLAND.\nYOUR MISSION IS TO FIND THE TREASURE")
left_right = input("\nLEFT or RIGHT? ")
if left_right.lower() == "left".lower():
    swim_wait = input("\nSWIM or WAIT? ")
    if swim_wait.lower() == "wait".lower():
        choose_door = input("\nWhich DOOR? ")
        if choose_door.lower() == "yellow".lower():
            print("YOU WIN")
        elif choose_door.lower() == "red".lower():
            print("Burned by fire. Game Over")
        elif choose_door.lower() == "blue".lower():
            print("Eaten by beasts. Game Over")
        else:
            print("Game Over")
    else:
        print("Attacked by trout. Game Over")
else:
    print("Fell into a hole. Game Over")