import random


def monty_hall_simulation(num_trials, switch_door):
    wins = 0
    for _ in range(num_trials):
        doors = [0, 0, 1]
        random.shuffle(doors)
        contestant_choice = random.randint(0, 2)
        for door in range(3):
            if door != contestant_choice and doors[door] == 0:
                monty_opened = door
                break
        if switch_door:
            for door in range(3):
                if door != contestant_choice and door != monty_opened:
                    contestant_choice = door
                    break
        if doors[contestant_choice] == 1:
            wins += 1
    return wins / num_trials


if __name__ == "__main__":
    num_trials = 10000
    switch_door = True
    win_percentage = monty_hall_simulation(num_trials, switch_door)
    print(f"Win percentage with switching doors: {win_percentage:.2%}")
