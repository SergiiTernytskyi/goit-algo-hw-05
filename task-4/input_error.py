from colorama import Fore


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return f"{Fore.RED}Oops! Try again, enter existing user name.{Fore.RESET}"
        except IndexError:
            return "Oops! Try again, enter the valid argument."
        except ValueError:
            return f"{Fore.RED}Oops! Try again, but enter name and phone number.{Fore.RESET}"
    return inner
