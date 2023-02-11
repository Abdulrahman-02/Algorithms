# Test cases
test = {
    'input': { 
        'array': [13, 15, 10, 7, 4, 3, 1, 0], 
        'targetSum': 11
    },
    'output': [10,1]
}

tests=[]

tests.append(test)

tests.append({
    'input': {
        'array':[5,2],
        'targetSum' : 10
    },
    'output' : []
})

# function O(N^2) complexity
def twoNumberSum(array, targetSum):
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            if(array[i]+array[j] == targetSum):
                return [array[i],array[j]]
    return []
 
# function O(N) complexity
def twoNumberSum1(array, targetSum):
    nums = set()
    for num in array:
        if targetSum - num in nums:
            return [num, targetSum - num]
        else:
            nums.add(num)
    return []


results = []

# Testing
for test in tests:
    result = twoNumberSum(**test['input']) == test['output']
    results.append(result)

print(results)
