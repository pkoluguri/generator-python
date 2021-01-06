def square_numbers(nums):
    for num in nums:
        yield(num*num)
nums = square_numbers([1,5,9,3])