#!/usr/bin/python3
import sys
import re
from signal import signal, SIGINT

# Regular expression to match the log format
log_pattern = re.compile(
    r'^(?P<ip>\S+) - \[(?P<date>.+)\] "GET /projects/260 HTTP/1.1" '
    r'(?P<status_code>\d{3}) (?P<file_size>\d+)$'
)

# Initialize global variables
total_size = 0
status_counts = {
    200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0
}
line_count = 0


def handle_interrupt(signal, frame):
    """Handles keyboard interrupt signal (CTRL + C)."""
    print_stats()
    sys.exit(0)


def print_stats():
    """Prints the current statistics."""
    global total_size, status_counts
    print(f"File size: {total_size}")
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")


# Register signal handler for keyboard interrupt
signal(SIGINT, handle_interrupt)

for line in sys.stdin:
    match = log_pattern.match(line.strip())
    if match:
        status_code = int(match.group('status_code'))
        file_size = int(match.group('file_size'))

        total_size += file_size
        if status_code in status_counts:
            status_counts[status_code] += 1

        line_count += 1

        # Print statistics every 10 lines
        if line_count % 10 == 0:
            print_stats()

print_stats()
