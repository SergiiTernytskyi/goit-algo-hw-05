def caching_fibonacci():
    cache = {}

    def fibonacci(n):
        result = 1 

        try:
            if n <= 0: 
                result = 0
            elif n == 1:
                result = 1
            else:
                if n in cache:
                    result = cache[n]           
                else:
                    result = fibonacci(n - 1) + fibonacci(n - 2)
                    cache[n] = result
            return result
        except TypeError:
            return f'Oops! You entered not valid number. Try again...'       
    
    return fibonacci


fib = caching_fibonacci()
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610


