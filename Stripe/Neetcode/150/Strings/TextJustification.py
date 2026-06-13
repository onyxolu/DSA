class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        line, length = [], 0
        i = 0

        while i < len(words):
            if length + len(words[i]) + len(line) <= maxWidth:
                line.append(words[i])
                length += len(words[i])
                i += 1
            else:
                # Line complete
                extra_space = maxWidth - length
                remainder = extra_space % max(1, (len(line) - 1))
                space = extra_space // max(1, (len(line) - 1))
                for j in range(max(1, len(line) - 1)):
                    line[j] += " " * space
                    if remainder:
                        line[j] += " "
                        remainder -= 1
                res.append("".join(line))
                line, length = [], 0

        # Handling last line
        last_line = " ".join(line)
        trail_space = maxWidth - len(last_line)
        res.append(last_line + " " * trail_space)
        return res