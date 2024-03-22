def sum_profit(text, func):
    total_income = 0

    # using function for profit calculation
    for number in func(text):
        total_income += number
        
    return total_income
