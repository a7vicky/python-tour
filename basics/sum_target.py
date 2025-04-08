# Two sum (find two numbers that add up to target)
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        if target - num in seen:
            return [seen[target - num], i]
        seen[num] = i

if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    result = two_sum(nums, target)
    if result:
        print(f"Indices of the two numbers that add up to {target} are: {result}")
    else:
        print("No two numbers add up to the target.")