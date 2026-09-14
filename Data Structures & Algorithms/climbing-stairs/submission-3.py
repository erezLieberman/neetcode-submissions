class Solution:
    def climbStairs(self, n: int) -> int:
        arr = []
        arr.insert(0, 1)
        arr.insert(1, 1)
        arr.insert(2, 2)
        
        if n > 2:
            for i in range(3,n+1):
                arr.insert(i,arr[i-1] + arr[i-2])
        print(arr)
        return arr[n]
             

        
