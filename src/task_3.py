import sys
from typing import Dict, List


def parse_log_line(line: str) -> Dict[str, str]:
    """
    Parse a single log line into its components.

    :param line: A log line in the format "YYYY-MM-DD HH:MM:SS LEVEL Message".
    :return: A dictionary with keys 'date', 'time', 'level', and 'message'.
    """
    parts = line.strip().split(" ", 3)
    if len(parts) < 4:
        return {}
    return {
        "date": parts[0],
        "time": parts[1],
        "level": parts[2].upper(),
        "message": parts[3],
    }


def load_logs(file_path: str) -> List[Dict[str, str]]:
    """
    Load and parse log lines from the given file.

    :param file_path: The path to the log file.
    :return: A list of dictionaries representing parsed log lines.
    """
    logs = []
    try:
        with open(file_path, encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    parsed = parse_log_line(line)
                    if parsed:
                        logs.append(parsed)
    except FileNotFoundError:
        print(f"Error: File not found: {file_path}")
        sys.exit(1)
    return logs


def filter_logs_by_level(
    logs: List[Dict[str, str]], level: str
) -> List[Dict[str, str]]:
    """
    Filter logs by the given logging level.

    :param logs: A list of parsed log dictionaries.
    :param level: The log level to filter by (e.g., 'ERROR').
    :return: A list of logs matching the specified level.
    """
    level = level.upper()
    return list(filter(lambda log: log.get("level") == level, logs))


def count_logs_by_level(logs: List[Dict[str, str]]) -> Dict[str, int]:
    """
    Count the number of log entries for each logging level.

    :param logs: A list of parsed log dictionaries.
    :return: A dictionary with logging levels as keys and counts as values.
    """
    counts: Dict[str, int] = {}
    for log in logs:
        level = log.get("level", "UNKNOWN")
        counts[level] = counts.get(level, 0) + 1
    return counts


def display_log_counts(counts: Dict[str, int]) -> None:
    """
    Display the log counts in a formatted table.

    :param counts: A dictionary with logging levels and their corresponding counts.
    """
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<16} | {count}")
