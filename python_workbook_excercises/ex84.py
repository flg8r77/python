'''
What’s the minimum number of times you have to flip a coin before you can have
three consecutive flips that result in the same outcome (either all three are heads or
all three are tails)? What’s the maximum number of flips that might be needed? How
many flips are needed on average? In this exercise we will explore these questions
by creating a program that simulates several series of coin flips.

Create a program that uses Python’s random number generator to simulate flipping
a coin several times. The simulated coin should be fair, meaning that the probability
of heads is equal to the probability of tails. Your program should flip simulated
coins until either 3 consecutive heads of 3 consecutive tails occur. Display an H each
time the outcome is heads, and a T each time the outcome is tails, with all of the
outcomes for one simulation on the same line. Then display the number of flips that
were needed to reach 3 consecutive occurrences of the same outcome. When your
program is run it should perform the simulation 10 times and report the average
number of flips needed. Sample output is shown below:

'''

import random

def main():

    flips_total = 0
    for i in range(1, 11):
        flips = flip_coin()
        flips_total = flips_total + flips
    print(f'On average, {flips_total / 10} flips were needed')

def flip_coin():
    heads_streak = 0
    tails_streak = 0
    flips = 0   
    while True:
        i = random.randrange(0,2)
        flips += 1
        if i == 0:
            tails_streak = 0
            print(f'H ', end='')
            heads_streak += 1
            if heads_streak == 3:
                print(f'({flips} flips) ')
                return flips
        else:
            heads_streak = 0
            print(f'T ', end='')
            tails_streak += 1
            if tails_streak == 3:
                print(f'({flips} flips) ')
                return flips
        

if __name__ == "__main__":
    main()