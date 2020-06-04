def solve(arr):
    single_route = 0
    stack = []
    
    for i in range(len(arr)):
        while stack and stack[-1][0] < arr[i]:
            stack.pop()
        if stack and arr[i] == stack[-1][0]:
            single_route += stack[-1][1]
            stack[-1][1] += 1
        else:
            stack.append([arr[i], 1])
    
    return 2*single_route