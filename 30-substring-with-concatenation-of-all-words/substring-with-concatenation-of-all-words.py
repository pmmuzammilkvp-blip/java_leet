class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        num_words = len(words)
        word_len = len(words[0])
        total_len = num_words * word_len
        n = len(s)

        if n < total_len:
            return []

        # Build frequency map of words
        word_count = {}
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1

        result = []

        # For each possible offset (0 to word_len - 1), slide a window
        for offset in range(word_len):
            # Use a frequency map for the current window
            curr_count = {}
            count = 0  # number of words in current window that match (with correct frequency)
            left = offset

            # right moves in steps of word_len
            for right in range(offset, n, word_len):
                word = s[right:right + word_len]

                if word in word_count:
                    curr_count[word] = curr_count.get(word, 0) + 1
                    count += 1

                    # If freq exceeds target, move left forward
                    while curr_count[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        curr_count[left_word] -= 1
                        count -= 1
                        left += word_len
                else:
                    # Reset because this chunk is not a valid word
                    curr_count = {}
                    count = 0
                    left = right + word_len

                # Check if we have a valid window
                if count == num_words and right - left + word_len == total_len:
                    result.append(left)

        return result