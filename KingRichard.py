def M_Formula_1(M,x):
    return (M[0]*x[0]+M[1]*x[1]+M[2], M[3]*x[0]+M[4]*x[1]+M[5])

def M_Formula_2(M,M2):
    return (M[0]*M2[0]+M[1]*M2[3], M[0]*M2[1]+M[1]*M2[4], M[0]*M2[2]+M[1]*M2[5]+M[2],
            M[3]*M2[0]+M[4]*M2[3], M[3]*M2[1]+M[4]*M2[4], M[3]*M2[2]+M[4]*M2[5]+M[5])

n = int(input())

squares = [(1,1,n-1)]

maps = [(1,0,0,0,1,0)]

s = int(input())

for i in range(s):
    a,b,d = map(int, input().split())
    squares.append((a,b,d))
    maps.append(M_Formula_2((0, 1, a-b, -1, 0, a+b+d), maps[-1]))

def main():
    for _ in range(int(input())): 
        w = int(input())
        y = x = (w//n+1, w%n+1) 
        min, max = 0, s+1
        while min+1<max:
            middle = (min+max)//2
            a,b,d = squares[middle]
            r,c = M_Formula_1(maps[middle], x)
            if (a<=r<=a+d and b<=c<=b+d):
                min=middle
                y=(r,c)
            else:
                max=middle
        print(y[0], y[1])

if __name__ == '__main__':
    main()