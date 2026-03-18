'''Name: Jacob Miranda & Daniel Puerto
Date: 03/16/26
Group: 13
Description:
'''

import check_input
import random
import vehicle
import car
import motorcycle
import truck 



def place_obstacle(track):

    for lane in track:
        placed = 0
        while placed < 2:
            pos = random.randint(1, len(lane) -2)
            if lane[pos] == "-":
                lane[pos] =="#"
                placed += 1


def find_next_obstacle(lane, start_pos):

    try:
        return lane.index("#", start_pos + 1)
    except ValueError:
        return 9999


def print_track(track):
    for lane in track:
        print("".join(lane))




def main():

    track = [
        ["C"] + ["-"] * 99,
        ["M"] + ["-"] * 99,
        ["T"] + ["-"] * 99
    ]

    place_obstacle(track)

    print_track(track)


    print("Would you like to be car, motorcycle, or truck?")
    choice = check_input.get_int_range("Enter 1 for car, 2 for motorcycle, or 3 for truck: ", 1, 3)
    if choice == 1:
        player = car.Car("Car", "P",  10)
        player_lane = 0
    elif choice == 2:
        player = motorcycle.Motorcycle("Motorcycle", "P",  15)
        player_lane = 1
    else:
        player = truck.Truck("Truck", "P", 5)
        player_lane = 2

    #Marked as the player
    track[player_lane][0] = player.initial()

    #Creates opponents
    vehicles = [None, None, None]
    vehicles[player_lane] = player

    if player_lane != 0:
        vehicles[0] = car.Car("Car", "C", 10)
    if player_lane != 1:
        vehicles[1] = motorcycle.Motorcycle("Motorcycle", "M", 15)
    if player_lane != 2:
        vehicles[2] = truck.Truck("Truck", "T", 5)

    #Opponent initlas
    initials = [vehicle.initial() for vehicle in vehicles]

    #Finish Order
    finish_order = []

    #Race Loop 

    while len(finish_order) < 3:

        print("\nCurrent Track:")
        print_track(track)

        if player not in finish_order:
            print("\nChoose move:")
            print("1. Fast")
            print("2. Slow")
            print("3. Special Move")
            move_choice = check_input.get_int_range("Enter choice (1-3): ", 1, 3)

            lane = track[player_lane]
            obs = find_next_obstacle(lane,player.position())

            if move_choice == 1:
                print(player.fast(obs))
            elif move_choice == 2:
                print(player.slow(obs))
            else:
                print(player.special_move(obs))

        #Opponent moves
        for lane_index, racer in enumerate(vehicles):
            if racer is None or racer in finish_order:
                continue
            if racer is player:
                continue

            lane = track[lane_index]
            obs = find_next_obstacle(lane, racer.position())

            roll = random.random()
            if racer.energy() <= 0:
                result = racer.slow(obs)
            elif roll < 0.4:
                result = racer.slow(obs)
            elif roll < 0.7:
                result = racer.fast(obs)
            else:
                result = racer.special_move(obs)

            print(f"{racer.name}: {result}")

        #Update Track 
        for lane_index, racer in enumerate(vehicles):
            if racer is None:
                continue
            
            lane = track[lane_index]

            #Clear the old initials
            for i in range(len(lane)):
                if lane[i] == initials[lane_index]:
                    lane[i] = "*"

            #Out of bounds 
            if racer.position() >= len(lane):
                racer._position = len(lane) - 1

            #Replace old initial
            lane[racer.position()] = initials[lane_index]

            #Checks finish 
            if racer.position() == len(lane) - 1 and racer not in  finish_order:
                finish_order.append(racer)

    #Resuslts
    print("\nFinal Results: ")
    for i, racer in enumerate(finish_order, start=1):
        print(f"{i}. {racer.name}")
        

    

if __name__ == "__main__":
    main()
