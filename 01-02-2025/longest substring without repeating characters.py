'''Given a string s, find the length of the longest 
substring
 without repeating characters.
Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        p,m,n= 0,0,0
        u = {}
        o = len(s)
        while(n< o):
            c = s[n]               
            u[c] = 1 if not c in u else u[c] + 1                      
            if u[c] > 1:
                while(u[c] > 1):
                    u[s[m]] =u[s[m]]- 1
                    m=m+1                    
            p = max(p,n-m+1)
            n=n+1
        return p
