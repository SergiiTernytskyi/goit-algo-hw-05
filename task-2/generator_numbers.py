import re

def generator_numbers(text: str):
    try:
        # extracting floats from string
        float_numbers = [float(word) for word in re.findall(r'\d+\.\d+', text)]

        # creating generator
        for number in float_numbers:
            yield number
    except TypeError:
        print(f'Oops! You entered not valid string. Try again...')
