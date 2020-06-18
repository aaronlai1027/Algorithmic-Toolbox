# Uses python3
import sys

# apply when majority number exist for sure
# def moorvoting(nums):
#     res = -1
#     cnt = 0;
#     for num in nums:
#         if cnt == 0:
#             res = num
#             cnt += 1
#         elif num == res:
#             cnt += 1
#         else:
#             cnt -= 1
#     return res

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]

    mid = (left+right)//2
    majLeft = get_majority_element(a,left,mid)
    majRight = get_majority_element(a,mid,right)

    if majLeft == majRight :
        return majLeft

    cntMajLeft = get_count(a, left, right,majLeft)
    cntMajRight = get_count(a, left, right,majRight)
    
    if cntMajLeft > cntMajRight and cntMajLeft > (right-left)//2:
        return majLeft 
    elif cntMajRight > cntMajLeft and cntMajRight > (right-left)//2:
        return majRight

    return -1
    
def get_count(a, left, right,x):
    count = 0
    for i in range(left,right):
        if(a[i]==x):
            count+=1
    return count    

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
