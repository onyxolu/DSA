from typing import List

# Clarify: words guaranteed non-empty, length ≤ maxWidth? favor left for extra spaces?
#          last line is left-justified only, single spaces, padding at end?
#
# Key insight: greedy packing — fit as many words as possible per line
# Spacing formula: total_spaces // gaps = even distribution, % gaps = leftover for left-most gaps
# Last line is fundamentally different — no distribution, just join + pad at end
#
# Volunteer before being asked:
#   - Edge case: single word on a line → gaps = max(1, len-1) avoids division by zero
#   - Edge case: words divide evenly into full lines → current_line_words could be empty
#     when reaching last-line logic → guard with `if current_line_words:`
#   - Real world: this is literally how word processors (Word, Google Docs) justify text

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        current_line_words = []
        current_line_word_length = 0
        word_index = 0

        while word_index < len(words):
            # +len(current_line_words) accounts for minimum 1 space between each word
            if (current_line_word_length + len(words[word_index]) + len(current_line_words)
                    <= maxWidth):
                current_line_words.append(words[word_index])
                current_line_word_length += len(words[word_index])
                word_index += 1
            else:
                total_spaces = maxWidth - current_line_word_length
                number_of_gaps = max(1, len(current_line_words) - 1)  # avoid div by zero
                spaces_per_gap = total_spaces // number_of_gaps
                extra_spaces = total_spaces % number_of_gaps          # leftover → left gaps first

                for gap_index in range(number_of_gaps):
                    current_line_words[gap_index] += " " * spaces_per_gap
                    if extra_spaces > 0:
                        current_line_words[gap_index] += " "          # extra space, left to right
                        extra_spaces -= 1

                result.append("".join(current_line_words))
                current_line_words = []
                current_line_word_length = 0

        # Last line: left-justified, single spaces, pad remainder at the end
        if current_line_words:                                       # guard: could be empty
            last_line = " ".join(current_line_words)
            remaining_spaces = maxWidth - len(last_line)
            result.append(last_line + " " * remaining_spaces)

        return result

# Edge cases:
#   single word longer than rest of line → its own line, padded right (if last) or alone (if not)
#   exactly one word fits per line → gaps = max(1, 0) = 1, no division by zero
#   words divide perfectly into full lines → current_line_words empty at end, guard skips append
#   single word total → goes straight to last-line logic, padded right

# Complexity:
#   time  → O(n × maxWidth) — n words, each line construction touches up to maxWidth chars
#   space → O(n × maxWidth) for the result

# Follow-ups:
#   What if maxWidth is smaller than the longest word? → problem guarantees this won't happen
#   Right-to-left languages → spacing logic would need to mirror (right gaps get extra instead)
#   Streaming words (don't know all words upfront) → can't fully justify a line until you know
#                                                      if more words exist, would need lookahead buffer