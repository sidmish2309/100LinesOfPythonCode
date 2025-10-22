class Solution:
    def nextLargerElement(self, arr, n):
        ans = [-1] * n
        stack = []
        
        for i in range(n - 1, -1, -1):
            while stack and arr[i] >= stack[-1]:
                stack.pop()
            if stack:
                ans[i] = stack[-1]
            stack.append(arr[i])
        
        return ans

# Driver Code
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        obj = Solution()
        res = obj.nextLargerElement(arr, n)
        print(' '.join(map(str, res)))
