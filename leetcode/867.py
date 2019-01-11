class Solution:
    def transpose(self, A):
        """
        此方法的本质就是ans[c][r] = A[r][c]
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        # R——A的长度，C——数组的长度
        R,C =len(A),len(A[0])
        ans = [[None]*R for _ in range(C)]
        # ans  [[None, None, None], [None, None, None], [None, None, None]]
        for r,row in enumerate(A):
            for c,val in enumerate(row):
                ans[c][r]= val
        return ans

def main():
    s  =Solution()
    b = s.transpose([[1,2,3],[4,5,6],[7,8,9]])
    print(b)
    #[[1, 4, 7], [2, 5, 8], [3, 6, 9]]

if __name__ == "__main__":
    main()
