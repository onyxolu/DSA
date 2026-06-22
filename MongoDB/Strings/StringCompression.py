from typing import List

# Clarify: case sensitive (uppercase ≠ lowercase)? same char can reappear non-consecutively?
# compressing consecutive runs, not total frequency
#
# Volunteer before being asked:
#   - Naive: build a separate result string/array → O(n) extra space
#   - Optimal: two pointers (read + write) → O(1) extra space, modify chars in place
#   - Multi-digit counts (10+) → convert to string, write each digit separately
#   - Real world: run-length encoding — used in image compression (BMP, fax machines), genomics

class Solution:
    def compress(self, chars: List[str]) -> int:
        write_index = 0
        read_index = 0
        n = len(chars)

        while read_index < n:
            current_char = chars[read_index]

            chars[write_index] = current_char      # write the character itself
            write_index += 1

            group_end = read_index + 1
            while group_end < n and chars[group_end] == current_char:
                group_end += 1                      # find end of this consecutive run

            group_size = group_end - read_index

            if group_size > 1:
                for digit in str(group_size):        # handles multi-digit counts (10+)
                    chars[write_index] = digit
                    write_index += 1

            read_index = group_end                   # move to start of next group

        return write_index

# Edge cases:
#   single character → returns 1, no count appended
#   all same character → single group, count appended
#   no repeats at all → every group size 1, no counts appended, length unchanged
#   group size >= 10 → count split into separate digit characters

# Complexity:
#   time  → O(n) — single pass through chars
#   space → O(1) — in-place modification, write pointer never exceeds read pointer

# Follow-ups:
#   What if input is a string, not a list? → strings are immutable in Python, would need to
#                                              return a new string instead of modifying in place
#   Decompress this format → read char + following digits until next letter, expand accordingly
#   Unicode/multi-byte characters → same logic works, Python handles unicode chars natively