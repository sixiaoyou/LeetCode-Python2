'''
【Python3代码不变,故此Python2代码可做参考】
LeetCode648. Replace Words
In English, we have a concept called root, which can be followed by some other words to form another longer word - let's call this word successor. For example, the root an, followed by other, which can form another word another.

Now, given a dictionary consisting of many roots and a sentence. You need to replace all the successor in the sentence with the root forming it. If a successor has many roots can form it, replace it with the root with the shortest length.

You need to output the sentence after the replacement.

Example 1:
Input: dict = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"
Note:
The input will only have lower-case letters.
1 <= dict words number <= 1000
1 <= sentence words number <= 1000
1 <= root length <= 100
1 <= sentence words length <= 1000
'''
class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        dict2 = {}
        array = sentence.split()
        start1 = 0
        dict.sort()
        count = 0
        for j in dict:
            if j[0] not in dict2:
                dict2[j[0]] = 0
            else:
                dict.remove(j)
        while start1 < len(array):
            start2 = 0
            while start2 < len(dict):
                length = len(dict[start2])
                if array[start1][0] == dict[start2][0]:
                    if len(array[start1]) >= length and array[start1][0:length] == \
                            dict[start2]:
                        array[start1] = dict[start2]
                start2 += 1
            start1 += 1
        return " ".join(array)

