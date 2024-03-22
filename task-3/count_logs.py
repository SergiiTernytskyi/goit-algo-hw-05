from collections import Counter

def count_logs_by_level(logs: list) -> dict:
    log_statistics = Counter(log['level'] for log in logs)

    return log_statistics