from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        prefix = ""
        first = strs[0]

        for i in range(len(first)):
            char = first[i]

            for word in strs:
                if i >= len(word) or word[i] != char:
                    return prefix

            prefix += char

        return prefix
