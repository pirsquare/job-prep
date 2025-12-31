from collections import Counter


# Find all anagrams in a string (FREQUENCY MAP window)

# anagrams means check is substring but irregardless of order (use sorted when compare)
# Anagrams are words or phrases formed by rearranging the letters of another word or phrase, using all the original letters exactly once.
# anagrams have same length

# Question
# Given strings s and p, find all start indices of p's anagrams in s.

# Solution
# anagrams have same length
# use sorted string to compare and traverse

# Input
s = "cbaebabacd"
p = "abc"


def find_anagrams(s, p):
    left = 0
    indices = []
    p_sorted = "".join(sorted(p))

    for right in range(len(s)):
        window_len = right-left
        if len(p) > window_len:
            continue

        window_s = sorted(s[left:right])
        window_text = "".join(window_s)

        # print(f"left: {left}")
        # print(f"right: {right}")
        # print(f"window_text: {window_text}")

        if p_sorted == window_text:
            indices.append(left)

        if window_len >= len(p):
            left += 1

    return (indices)



print(find_anagrams(s, p))
# [0, 6]


# recommended solution
def find_anagrams(string, ss):
    ss_len = len(ss)
    string_len = len(string)

    if ss_len > string_len:
        return []

    need = Counter(ss)
    window = Counter(string[:ss_len])

    print(f"need: {need}")
    print(f"window: {window}")

    res = []
    if window == need:
        res.append(0)

    for i in range(ss_len, string_len):
        window[string[i]] += 1
        left_char = string[i - ss_len]
        window[left_char] -= 1

        if window[left_char] == 0:
            del window[left_char]

        if window == need:
            res.append(i - ss_len + 1)
    return res

print(find_anagrams(s, p))
