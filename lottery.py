"""
There are two approaches to create this simulator:
    1. Using combinatorics to calculate the odds of winning -> faster
    2. Actually creating the lottery game. (that's what I did!) -> slower
I choose the slower method as this stimulates real lottery, and i'm printing the progression so we're capping in speed because of the prints anyways.
"""

import random, time
import config as cfg

def two_decimals(num: float) -> float:
    return "{:.2f}".format(num)

def initialize_lottery(country: str, rounds: int, sleep: float = 0, console_print: bool = True) -> None:
    """_summary_

    Args:
        country (str): country initials in caps - e.g. 'IL' -> pulling specific country's lottery information
        rounds (int): iteration count
        sleep (float): sleep between iterations, if dealing with high round count, leave at 0 for best performance. Defaults to 0.
        console_print (bool, optional): enable console prints. Defaults to True.
    """
    # initialize variables
    prize_sum, price_sum = 0, 0
    prize_3_hits, prize_4_hits, prize_5_hits, prize_6_hits, prize_jack_hits = 0, 0, 0, 0, 0 # initialize  hits counter

    if console_print: print("Starting Lottery...")
    start_timer = time.time() # start timer

    for i in range(1, rounds + 1):
        winning_draw = random.sample(range(1, cfg.method[country]['max_number'] + 1), 6) # Permutation, out of a pool of 37 
        winning_draw.append(random.randrange(1, cfg.method[country]['extra_number'] + 1)) # adding the special number (out of a pool of 7)
        player_draw = random.sample(range(1, cfg.method[country]['max_number'] + 1), 6)
        player_draw.append(random.randrange(1, cfg.method[country]['extra_number'] + 1))
        price_sum += cfg.method[country]['ticket_price']
        count_hits = 0
        special_hit = False
        # calculate hits
        for x in range(len(player_draw) - 2): # -2, without the special number
            if player_draw[x] in winning_draw:
                count_hits += 1
        if player_draw[len(player_draw) - 1] == winning_draw[len(winning_draw) - 1]: # special number hit
            special_hit = True
        # if 3 hits, only last 3 (without special number)
        if count_hits == 3: 
            count_hits = 0
            for x in range(len(player_draw) - 5, len(player_draw) - 2):
                if player_draw[x] in winning_draw:
                    count_hits += 1
        # if 4 hits, only last 4 (without special number)
        if count_hits == 4:
            count_hits = 0
            for x in range(len(player_draw) - 6, len(player_draw) - 2):
                if player_draw[x] in winning_draw:
                    count_hits += 1
        # if 5 hits, only last 5 (without special number)
        if count_hits == 5:
            count_hits = 0
            for x in range(len(player_draw) - 7, len(player_draw) - 2):
                if player_draw[x] in winning_draw:
                    count_hits += 1

        # add prizes to sum
        if count_hits == 3 and special_hit:
            prize_sum += cfg.method[country]['3_prize_special']
            prize_3_hits += 1
        if count_hits == 3 and not special_hit:
            prize_sum += cfg.method[country]['3_prize']
            prize_3_hits += 1
        if count_hits == 4 and special_hit:
            prize_sum += cfg.method[country]['4_prize_special']
            prize_4_hits += 1
        if count_hits == 4 and not special_hit:
            prize_sum += cfg.method[country]['4_prize']
            prize_4_hits += 1
        if count_hits == 5 and special_hit:
            prize_sum += cfg.method[country]['5_prize_special']
            prize_5_hits += 1
        if count_hits == 5 and not special_hit:
            prize_sum += cfg.method[country]['5_prize']
            prize_5_hits += 1
        if count_hits == 6:
            # prize_sum += cfg.method[country]['6_prize'][random.randrange(len(cfg.method[country]['6_prize']) - 1)] # random prize if 6 hits
            prize_sum += cfg.method[country]['6_prize']
            prize_6_hits += 1
        if count_hits == 7:
            prize_sum += cfg.method[country]['jackpot_prize']
            prize_jack_hits += 1
        
        end_timer = time.time() # stops timer

        # printing results:
        if console_print:
            to_print = f'Rounds played: {i} Prize won: {two_decimals(prize_sum)}₪ Total Price Paid: {two_decimals(price_sum)}₪ Balance: {two_decimals(prize_sum-price_sum)}₪ || {str(player_draw)} vs {str(winning_draw)}'
            print(to_print, end='\r', flush=True)
        
        time.sleep(sleep) # system sleep for given time. sleep = 0 for best performance.

    if console_print:
        print("\n--------------------Summary--------------------") 
        print(f'Out of {rounds} rounds played, you won: {two_decimals(prize_sum)}₪, paid: {two_decimals(price_sum)}₪, total balance: {two_decimals(prize_sum-price_sum)}₪')
        print(f'3 hits: {prize_3_hits}, 4 hits: {prize_4_hits}, 5 hits: {prize_5_hits}, 6 hits {prize_6_hits}, jackpot: {prize_jack_hits}')
        print(f'The stimulation took: {two_decimals(end_timer - start_timer)}s')
        print("--------------------Lottery done successfully... better luck next time!--------------------")
    else:
        pass # return summary

initialize_lottery('IL', 1000000, 0)
