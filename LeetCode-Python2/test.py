import copy
class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        list1,list2,list3,mark,mark2,temp,temp1=[],[],[],-1,True,0,0
        ls=list(str(num))
        list1=map(int,str(num))
        list3=copy.deepcopy(list1)
        list3.sort().reverse
        for j in range(len(list1)):
            if mark2 and list3[j]>list1[j]:
                ls[j]=str(list3[j])
                temp=list3[j]
                temp1=str(list1[j])
                mark2=False
            if list1[j] == temp:
                mark = j
        if mark>0:
            ls[mark]=temp1
        list2=map(str,ls)
        return int("".join(list2))