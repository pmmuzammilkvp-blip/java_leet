class Solution:
    def fullJustify(self, words, maxWidth):
        res = []
        i = 0
        n = len(words)

        while i < n:
            # Determine which words fit on this line
            line_len = len(words[i])
            j = i + 1
            while j < n and line_len + 1 + len(words[j]) <= maxWidth:
                line_len += 1 + len(words[j])
                j += 1

            line_words = words[i:j]
            num_words = j - i
            total_chars = sum(len(w) for w in line_words)
            spaces_needed = maxWidth - total_chars

            # Last line or single word line -> left justify
            if j == n or num_words == 1:
                line = ' '.join(line_words)
                line += ' ' * (maxWidth - len(line))
            else:
                # fully justify
                spaces_between_words = spaces_needed // (num_words - 1)
                extra_spaces = spaces_needed % (num_words - 1)

                line = ''
                for k in range(num_words - 1):
                    line += line_words[k]
                    line += ' ' * (spaces_between_words + (1 if k < extra_spaces else 0))
                line += line_words[-1]  # last word

            res.append(line)
            i = j

        return res
