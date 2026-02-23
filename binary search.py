nums = list(map(int, input("Enter sorted numbers: ").split()))
target = int(input("Enter the  target: "))

left = 0
right = len(nums) - 1

while left <= right:
    mid = (left + right) // 2

    if nums[mid] == target:
        print("Index:", mid)
        break
    elif nums[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
else:
    print(-1)