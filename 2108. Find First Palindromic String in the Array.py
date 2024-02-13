# Intuition
The problem asks for finding the first palindrome in a list of words. A palindrome is a word that reads the same forwards and backwards. 

# Approach
The approach used in the provided code is straightforward. It iterates through the list of words and checks if each word is equal to its reverse. If a palindrome is found, it is stored in the `res` variable and the loop breaks.

# Complexity
- Time complexity: 
  - In the worst-case scenario, where there are no palindromes in the list or the last word is a palindrome, the time complexity would be O(n*m), where n is the number of words and m is the average length of the words. This is because, in the worst case, each word has to be checked for being a palindrome.
- Space complexity: 
  - The space complexity is O(1) since the additional space used does not grow with the input size. Only a constant amount of extra space is used for storing the result.

Example 1:

Input: words = ["abc","car","ada","racecar","cool"]
Output: "ada"
Explanation: The first string that is palindromic is "ada".
Note that "racecar" is also palindromic, but it is not the first.
  
# Code
```python
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        n = len(words)
        res = ''
        for i in range(n):
            if words[i] == words[i][::-1]:
                res = words[i]
                break     
        return res
```
