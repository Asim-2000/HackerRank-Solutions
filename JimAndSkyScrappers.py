def solve(arr):
    single_route = 0
    st = []
    
    for i in range(len(arr)):
        while st and st[-1][0] < arr[i]:
            st.pop()
        if st and arr[i] == st[-1][0]:
            single_route += st[-1][1]
            st[-1][1] += 1
        else:
            st.append([arr[i], 1])
    
    return 2*single_route