puzzle = []

n,m = input().split(' ')

n=int(n)
m=int(m)

for i in range(n):
    puzzle.append(list(input().strip()[:m]))


print(puzzle)

def get_paths(i,j):
    paths=[]
    dots=0
    if (i>0):
        paths.append((i-1,j))
    if(j>0):
        paths.append((i,j-1))
    if (i<n):
        paths.append((i+1,j))
    if (j<n):
        paths.append((i,j+1))

    for i,j in paths:
        if (puzzle[i][j]=="."):
            dots+=1
    return paths,dots

print (get_paths(0,1))


def floodTunnel(cDot,i,j,count):
    if (cDot>0):
        k,dots=get_paths(i,j)
        if (dots<1):
            count+=1
            puzzle[i][j]='x'
            cDot-=1
        else:
            for i,j in k:
                if (puzzle[i][j]=="."):
                    puzzle[i][j]='x';
                    cDot-=1
                    count=floodTunnel(cDot,i,j,count)
    return count


cDot=1
for i in puzzle:
    cDot+=i.count(".")

print(floodTunnel(cDot,0,1,0))
