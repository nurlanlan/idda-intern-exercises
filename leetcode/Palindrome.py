class Solution:
    def isPalindrome(self, s: str) -> bool:
        converted = "".join(ch.lower() for ch in s if ch.isalnum())
        print(converted)
        if converted[::-1] == converted:
            return True
        return False

obj = Solution()
print(obj.isPalindrome("race a car"))
