def solution(numbers):
    answer = 0
    
    nums = ["zero","one", "two", "three", "four", "five", "six", "seven", "eight", "nine"] 
    
    for i in nums:
        if i in numbers:
            numbers = numbers.replace(i,str(nums.index(i)))
    
    answer = int(numbers)
    
    return answer