from generator_numbers import generator_numbers
from profit_calculation import sum_profit

def main():
    text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
    
    total_income = sum_profit(text, generator_numbers)
    print(f"Total income: {total_income}")


if __name__ == '__main__':
    main()







