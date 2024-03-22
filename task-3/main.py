from pathlib import Path
from parse_input import parse_input
from load_logs import load_logs
from count_logs import count_logs_by_level
from filter_logs import filter_logs_by_level


def main():
    user_input = input(f"Enter a file path and log level: ").strip().lower()

    try:
        # getting data from command line
        path, level = parse_input(user_input)

        file_path = Path(path)

        # reading file
        logs = load_logs(file_path)

        # count logs by level
        statistics = count_logs_by_level(logs)
 
        # printing logs count in table view
        row_format ="{:^15}|{:^15}"
        table_header = ['Logging level', 'Quantity'] 

        print(row_format.format(*table_header))
        print('-' * 30)

        for stats_level, stats in statistics.items():
            print(row_format.format(stats_level, stats))

        # printing logs details in case user entered level type
        if level:            
            filtered_logs = filter_logs_by_level(logs, level)
            print(f'Details of logs for level "{level.upper()}":')
            for log_item in filtered_logs:
                print(f'{log_item['date']} {log_item['time']} - {log_item['log_message']}')

    except ValueError:
        print(f"Oops! Looks like empty command field. Try again...")


if __name__ == "__main__":
    main()