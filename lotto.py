"""
There are two approaches to create this simulator:
    1. Using combinatorics to calculate the odds of winning -> faster
    2. Actually creating the lottery game. (that's what I did!) -> slower
I choose the slower method as this stimulates real lottery, and i'm printing the progression so we're capping in speed because of the prints anyways.
"""

import random, time
import config as cfg

# initialize variables
prize_sum, price_sum = 0, 0
rounds = 100000 # number of rounds
prize_3_hits, prize_4_hits, prize_5_hits, prize_6_hits, prize_jack_hits = 0, 0, 0, 0, 0 # initialize  hits counter
sleep = 0 # sleep between iterations, if dealing with high round count, leave at 0.

print("Calculating...")
for i in range(1, rounds + 1):
    winning_draw = random.sample(range(1, cfg.method['IL']['max_number'] + 1), 6) # Permutation, out of a pool of 37 
    winning_draw.append(random.randrange(1, cfg.method['IL']['extra_number'] + 1)) # adding the special number (out of a pool of 7)
    player_draw = random.sample(range(1, cfg.method['IL']['max_number'] + 1), 6)
    player_draw.append(random.randrange(1, cfg.method['IL']['extra_number'] + 1))
    price_sum += cfg.method['IL']['ticket_price']
    count_hits = 0

    # calculate hits
    for x in range(len(player_draw) - 1): # -1 without the special number
        if player_draw[x] in winning_draw:
            count_hits += 1
    # if 3 hits, only last 3
    if count_hits == 3: 
        count_hits = 0
        for x in range(len(player_draw) - 4, len(player_draw) - 1):
            if player_draw[x] in winning_draw:
                count_hits += 1
    # if 4 hits, only last 4
    if count_hits == 4:
        count_hits = 0
        for x in range(len(player_draw) - 5, len(player_draw) - 1):
            if player_draw[x] in winning_draw:
                count_hits += 1
    # if 5 hits, only last 5
    if count_hits == 5:
        count_hits = 0
        for x in range(len(player_draw) - 6, len(player_draw) - 1):
            if player_draw[x] in winning_draw:
                count_hits += 1

    # add prizes to sum
    if count_hits == 3:
        prize_sum += cfg.method['IL']['3_prize']
        prize_3_hits += 1
    if count_hits == 4:
        prize_sum += cfg.method['IL']['4_prize']
        prize_4_hits += 1
    if count_hits == 5:
        prize_sum += cfg.method['IL']['5_prize']
        prize_5_hits += 1
    if count_hits == 6:
        prize_sum += cfg.method['IL']['6_prize'][random.randrange(len(cfg.method['IL']['6_prize']) - 1)] # random prize if 6 hits
        prize_6_hits += 1
    if count_hits == 7:
        prize_sum += cfg.method['IL']['jackpot_prize']
        prize_jack_hits += 1
    
    # printing results:
    to_print = f'Rounds played: {i} Prize won: {"{:.2f}".format(prize_sum)}₪ Total Price Paid: {"{:.2f}".format(price_sum)}₪ Balance: {"{:.2f}".format(prize_sum-price_sum)}₪ || {str(player_draw)} vs {str(winning_draw)}'
    print(to_print, end='\r', flush=True)
    time.sleep(sleep)


print("\nSummary:") 
print(f'Out of {rounds} rounds played, you won: {"{:.2f}".format(prize_sum)}₪, paid: {"{:.2f}".format(price_sum)}₪, total: {"{:.2f}".format(prize_sum-price_sum)}₪')
print(f'3 hits: {prize_3_hits}, 4 hits: {prize_4_hits}, 5 hits: {prize_5_hits}, 6 hits {prize_6_hits}, jackpot: {prize_jack_hits}')
print("Done")
    