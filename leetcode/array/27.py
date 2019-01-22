class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = 0
        for i in range(len(nums)):            
            if nums[i-count] ==val:
                nums.pop(i-count)
                count +=1

        return len(nums)

def main():
    a = Solution()
    nums = [0,1,2,2,3,2,2,3,0,4,2]
    val = 2
    print(a.removeElement(nums,val))

if __name__ == "__main__":
    main()