'''
LeetCode 500:Keyboard Row
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.


American keyboard


Example 1:
Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
Note:
You may use one character in the keyboard more than once.
You may assume the input string will only contain letters of alphabet.
'''

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        removeWords=[]
        words1='QWERTYUIOP'
        words2='ASDFGHJKL'
        words3='ZXCVBNM'
        for i in words:
            strI=''.join(set(i.upper()))
            for j in xrange(len(strI)-1):
                if strI[j] in words1 and strI[j+1] not in words1:
                    removeWords.append(i)
                elif strI[j] in words2 and strI[j + 1] not in words2:
                    removeWords.append(i)
                elif strI[j] in words3 and strI[j + 1] not in words3:
                    removeWords.append(i)
        setRemoveWords=list(set(removeWords))
        for j in setRemoveWords:
            words.remove(j)
        return words


