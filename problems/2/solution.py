#a)
def f_u_w(nums,k) -> int:
    window = []
    nums_length = len(nums)
    for i,num in enumerate(nums):
        if i == 0 or window[-1] + 1 != num:
            window = [num]
        if i == nums_length:
            return -1
        if window[-1] + 1 == num :
            window.append(num)
            if len(window) == k:
                return i-k+1
print(f_u_w([1,2,3,3,2,100],3))

#b)
def f_u_w(nums, k) -> int:
    window = set()
    left = 0
    for right, num in enumerate(nums):
        while num in window: # if the number is in the window
            window.remove(nums[left]) #remove the left/first window
            left += 1
        window.add(num)
        if len(window) == k:
            return left
    return -1



