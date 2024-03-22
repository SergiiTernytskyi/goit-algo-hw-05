def parse_log_line(line: str) -> dict:
    date, time, level, log_message = [line.strip() for line in line.split(' ', 3)]

    log_dict = {'date': date, 'time': time, 'level': level, 'log_message': ''.join(log_message)}

    return log_dict

