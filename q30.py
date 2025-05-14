# Name- ANURADHA KUMARI
# Reg no.- 23117107002
# Biomedical and Robotics Engineering

import random

def monty_hall_simulation(num_trials=10000):
    stay_wins = 0
    switch_wins = 0

    for _ in range(num_trials):
        doors = [0, 0, 0]
        car_position = random.randint(0, 2)
        doors[car_position] = 1  

        
        player_choice = random.randint(0, 2)

        
        possible_doors = [i for i in range(3) if i != player_choice and doors[i] == 0]
        host_opens = random.choice(possible_doors)

        
        remaining_doors = [i for i in range(3) if i != player_choice and i != host_opens]
        switch_choice = remaining_doors[0]

        
        if doors[player_choice] == 1:
            stay_wins += 1

        
        if doors[switch_choice] == 1:
            switch_wins += 1

    
    print(f"After {num_trials} simulations:")
    print(f"Staying won the car: {stay_wins} times ({(stay_wins/num_trials)*100:.2f}%)")
    print(f"Switching won the car: {switch_wins} times ({(switch_wins/num_trials)*100:.2f}%)")


monty_hall_simulation()