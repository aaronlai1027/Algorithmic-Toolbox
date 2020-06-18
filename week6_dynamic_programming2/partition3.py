# Uses python3
import sys

def partition3(A):
    return 1 if helper(A,3) else 0

def helper(nums,k):

    n = len(nums)
    if k == 0 or k > n: return False

    total = sum(nums)
    if total%k: return False
    
    target = total/k
    visited = [False] * n
    nums.sort(reverse=True)
    if nums[0] > target: return False

    def dfs(k,startIdx,curSum):
        if k == 1: return True
        if curSum == target:
            return dfs(k-1,0,0)
        for i in range(startIdx,n):
            if not visited[i] and curSum+nums[i]<=target: 
                visited[i] = True
                if dfs(k,i+1,curSum+nums[i]): return True
                visited[i] = False
        return False
    
    return dfs(k,0,0)



if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A))

