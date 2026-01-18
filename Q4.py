def remove_even(numbers):
    result = []
    for n in numbers:
        if n % 2 != 0:   # if number is NOT even, keep it
            result.append(n)
    return result


nums = [1,2,3,4,5,6,7,8,9,10]
print(remove_even(nums))
