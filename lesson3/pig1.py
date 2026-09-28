import random

score = 0
turn_count = 0
while score < 100:
    turn_score = 0
    while True: 
        roll = random.randint(1,6)
        print(f"You rolled: {roll}")
        if roll == 1:
            turn_score = 0
            print("You greedy pig! 0 points this turn!")
            break
        else:
            turn_score = turn_score + roll
            print(f"Your score so far this turn is: {turn_score}")

        choice = input("Do you want to roll again (y/n)?")
        if choice == "n":
            break
    
    turn_count = turn_count + 1
    print(f"you have completed {turn_count} turns")
    score = score + turn_score
    print(f"Total score so far is: {score}")