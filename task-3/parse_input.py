def parse_input(user_input: str):
    path, *args = user_input.split()

    level = args[0].strip().lower() if len(args) >= 1 else ''

    return path, level

