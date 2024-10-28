Pattern Matching: We use a regular expression to match lines in the specified format. Only matched lines are processed; others are skipped.
Status Code Tracking: We increment counts only for the required status codes.
Statistics Output: After every 10 lines or upon CTRL + C, the print_stats function displays:
The total file size.
The count for each status code that has appeared, sorted in ascending order.
Signal Handling: signal(SIGINT, handle_interrupt) allows the script to handle CTRL + C and print statistics before exiting.
. Parsing Log Entries
Each log entry follows this format:

php
Copy code
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
The script should extract:

status code: an integer indicating the HTTP response code.
file size: an integer for the size of the response.
If a line doesn’t match this format, skip it.

2. Computing Metrics
Total File Size: Sum all file size values from the start.
Status Code Count: Count occurrences of each status code. Track only the specified codes: 200, 301, 400, 401, 403, 404, 405, and 500.
3. Output Format
After every 10 lines or upon interruption:

Print the total file size.
Print counts for each status code that appeared, sorted in ascending order.
4. Handling Interruptions
Use signal handling to manage CTRL + C interruptions and print the current statistics before the script exits.
