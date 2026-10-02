class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        s_len = len(s)

        if total_len > s_len:
            return []

        # Build the frequency map of words
        word_count = Counter(words)
        result = []

        # We need to check each possible offset (0 to word_len-1)
        # For each offset, we slide a window of total_len through s
        for i in range(word_len):
            if i + total_len > s_len:
                break

            left = i
            seen = Counter()  # frequency of words seen in current window
            count = 0  # number of valid words in current window

            # Slide one word at a time
            for j in range(i, s_len - word_len + 1, word_len):
                # Extract the current word
                word = s[j:j + word_len]

                if word in word_count:
                    seen[word] += 1
                    count += 1

                    # If this word appears more times than in the original set,
                    # move the left pointer until we fix the overcount
                    while seen[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        seen[left_word] -= 1
                        count -= 1
                        left += word_len
                else:
                    # If the word is not in the dictionary, reset the window
                    left = j + word_len
                    seen = Counter()
                    count = 0

                # Check if the current window contains exactly all the words
                if count == num_words:
                    result.append(left)
                    # Move the left pointer forward to continue sliding
                    left_word = s[left:left + word_len]
                    seen[left_word] -= 1
                    count -= 1
                    left += word_len

        return result