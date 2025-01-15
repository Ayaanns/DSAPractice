#contains dublicates
def example_one(nums):
    return len(nums) != len(set(nums))

def example_two(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

def example_three(nums, k):
    window = {}
    for i, num in enumerate(nums):
        if num in window and i-window[num]<=k:
            return True
        window[num]=i
    return False


