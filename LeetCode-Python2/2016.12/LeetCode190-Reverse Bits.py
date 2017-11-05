'''
LeetCode 190. Reverse Bits
Reverse bits of a given 32 bits unsigned integer.

For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), return 964176192 (represented in binary as 00111001011110000010100101000000).

Follow up:
If this function is called many times, how would you optimize it?

Related problem: Reverse Integer
'''
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        binI=bin(n)
        strI=str(binI).replace('0b','')
        for i in xrange(32-len(strI)):
            strI='0'+strI
        listBinI=list(strI)
        listBinI.reverse()
        strBinI=''.join(listBinI)
        finalBinI='0b'+strBinI
        return eval(finalBinI)



