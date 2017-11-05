class SolutionV1(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        list1 = []
        if numbers.count(target / 2) == 2 and target % 2 == 0:
            list1.append(numbers.index(target / 2) + 1)
            list1.append(numbers.index(target / 2) + 2)
            print list1
        else:
            numbers1 = list(set(numbers))
            for i in xrange(len(numbers1)):
                if numbers.count(numbers1[i]) == 1 and numbers.count(target - numbers1[i]) == 1:
                    if (numbers1[i] < (target - numbers1[i])):
                        list1.append(numbers.index(numbers1[i]) + 1)
                        list1.append(numbers.index(target - numbers1[i]) + 1)
                        print list1
                    else:
                        list1.append(numbers.index(target - numbers1[i]) + 1)
                        list1.append(numbers.index(numbers1[i]) + 1)
                        print list1

class SolutionV2(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i,j=0,len(numbers)-1
        while i<=j:
            if numbers[i]+numbers[j]==target:
                return [i+1,j+1]
            elif numbers[i]+numbers[j]<target:
                i+=1;
            else:
                j-=1

