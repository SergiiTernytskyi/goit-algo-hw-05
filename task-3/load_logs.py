from parse_log import parse_log_line

def load_logs(file_path: str) -> list:
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            lines = [parse_log_line(el) for el in file.readlines()]
            return lines
    except FileNotFoundError:
        print(f"Oops! File, You trying to reach seems does not exist. Try again...")
    except OSError:
        print(f"Oops! Error occurred trying to open {file_path}")

