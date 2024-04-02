def product_except_self(nums):
    prefix = [nums[0]]
    postfix = [nums[-1]]
    pwr = nums[0]
    for i in range(1, len(nums)):
        pwr *= nums[i]
        prefix.append(pwr)
    pwr = nums[-1]
    for i in range(len(nums) - 2, -1, -1):
        pwr *= nums[i]
        postfix.append(pwr)

    postfix.reverse()

    result = []
    for i in range(len(nums)):
        if i == 0:
            result.append(postfix[i + 1])
        elif i == len(nums) - 1:
            result.append(prefix[i - 1])
        else:
            result.append(prefix[i - 1] * postfix[i + 1])
    return result


print(product_except_self([1, 2, 3, 4]))  # [24,12,8,6]
