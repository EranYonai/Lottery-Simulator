def factorial(n, ite):
    factorial = 1
    for i in range(n-ite + 1, n + 1):
        factorial *= i
    return factorial

# According to IL Mifal Hapeis
method = {'IL': {
 'jackpot_prize': 80000000,
 'max_number': 37,
 'extra_number': 7,
 '6_prize': 3000000,
 '5_prize_special': 500000,
 '5_prize': 5000,
 '4_prize_special': 10000,
 '4_prize': 1000,
 '3_prize_special': 1000,
 '3_prize': 100,
 'ticket_price': 6.6
 }}

# chances of wining calaulation:
method['IL']['c_jackpot_prize'] = int(factorial(method['IL']['max_number'], 7) / 720)
method['IL']['c_6_prize'] = int(factorial(method['IL']['max_number'], 6) / 720)
method['IL']['c_5_prize'] = int(factorial(method['IL']['max_number'], 5) / 720)
method['IL']['c_4_prize'] = int(factorial(method['IL']['max_number'], 4) / 720)
method['IL']['c_3_prize'] = int(factorial(method['IL']['max_number'], 3) / 720) 
