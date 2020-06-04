def add(a_b, c_d):
    (a,b) = a_b
    (c,d) = c_d
    return a+c, b+d

def sub(a_b, c_d):
    (a,b) = a_b
    (c,d) = c_d
    return a-c, b-d

def rot(i_j):
    (i,j) =i_j
    return j,-i

def rotk(k,x):
    for i in range(k):
        x = rot(x)
    return x

def trans(k_d,x):
    (k,d) = k_d
    return add(rotk(k,x),d)

def compose(k_d, K_D):
    (k,d) = k_d
    (K,D) = K_D
    return k + K & 3, trans((k,d),D)

def inv(k_d):
    (k,d) = k_d
    k = -k & 3
    return k, rotk(k^2,d)

def contains(co_c1,p):
    (c0,c1) = co_c1
    return c0[0] <= p[0] <= c1[0] and c0[1] <= p[1] <= c1[1]


n = int(input())
s = int(input())
transes = [None]*(s+1)
corners = [None]*(s+1)
transes[0] = 0, (0,0)
corners[0] = (0,0), (n-1,n-1)

for i in range(s):
    a,b,d = list(map(int, input().strip().split()))
    a -= 1
    b -= 1
    itr = inv(transes[i]); i += 1
    ncorns = [trans(itr,x) for x in [(a,b),(a,b+d),(a+d,b+d),(a+d,b)]]
    transes[i] = i & 3, sub((a,b), rotk(i & 3, ncorns[3]))
    corners[i] = min(ncorns), max(ncorns)

for qq in range(eval(input())):
    x = int(input())
    p = x//n, x%n
    L = 0
    R = s+1
    while R - L > 1:
        M = L + R >> 1
        if contains(corners[M],p):
            L = M
        else:
            R = M

    ans = trans((transes[L]),p)
    print("%s %s" % add(ans,(1,1)))