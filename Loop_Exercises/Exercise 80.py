import random
total_flips = 0
num_simulations = 10

for _ in range(num_simulations):
    flips = 0
    consecutive_outcomes = 0
    sum=0.0

    while consecutive_outcomes < 3:
        flip = random.choice(['H', 'T'])
        print(flip, end=' ')
        flips += 1

        if flip == 'H':
            consecutive_outcomes = consecutive_outcomes + 1 if consecutive_outcomes >= 0 else 1
        else:
            consecutive_outcomes = consecutive_outcomes - 1 if consecutive_outcomes <= 0 else -1

    total_flips += flips
    average_flips_needed = total_flips / num_simulations
    print("(",flips," flips)",sep="")
print("On average,",average_flips_needed, "flips were needed")