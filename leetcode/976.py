class Solution:
    def largestPerimeter(self, A):
        """
        先按降序排序，
        遍历列表，如果最大a[i-2]小于其他两个，则返回
        :type A: List[int]
        :rtype: int
        """
        a = sorted(A,reverse=True)
        for i in range(2,len(A)):
            if a[i-2]<a[i-1]+a[i]:
                return sum(a[i-2:i+1])
        return 0


