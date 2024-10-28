#!/usr/bin/python3
import sys
import re
from signal import signal, SIGINT

# Initialize counters and data structures
total_file_size = 0
status_code_count = {str(code): 0 for code in [200, 301, 400, 401, 403, 404, 405, 500]}
line_count = 0

# Regular expression to match log entry format
log_pattern = re.compile(
    r'^\S+ - \[\S+ \S+\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$'
)

def print_stats():
    """Function to print accumulated statistics."""
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_count.keys()):
        if status_code_count[code] > 0:
            print(f"{code}: {status_code_count[code]}")

def handle_interrupt(signal_received, frame):
    """Handle CTRL + C signal to print stats before exiting."""
    print_stats()
    sys.exit(0)

# Register signal handler for CTRL + C
signal(SIGINT, handle_interrupt)

# Process input lines from stdin
for line in sys.stdin:
    match = log_pattern.match(line.strip())
    if match:
        status_code, file_size = match.groups()
        # Update file size and status code count
        total_file_size += int(file_size)
        if status_code in status_code_count:
            status_code_count[status_code] += 1
    line_count += 1

    # Print statistics every 10 lines
    if line_count % 10 == 0:
        print_stats()

# Print final statistics if EOF is reached
print_stats()

