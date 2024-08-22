UTF-8 Encoding Rules:
A single-byte character (ASCII) uses 1 byte, starting with 0.
A character with 2 bytes starts with 110 and the next byte starts with 10.
A character with 3 bytes starts with 1110 and the following bytes start with 10.
A character with 4 bytes starts with 11110 and the following bytes start with 10.
Plan:
Iterate over the list of integers.
Determine how many bytes are in the current UTF-8 character by examining the leading bits.
Check that the subsequent bytes start with 10.
Return True if all characters are valid, otherwise False.
