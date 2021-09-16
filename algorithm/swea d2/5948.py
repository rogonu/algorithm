TC = int(input())
for tc in range(1, TC +1):
    nums = list(map(int, input().split()))
    nums.sort(reverse=True)
    res = nums[0] + nums[1]+ nums[6]
    print(f'#{tc} {res}')