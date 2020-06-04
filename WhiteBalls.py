n,k=input().split(" ")
n=int(n)
k=int(k)
ball=input()

w=ball.count("W")
cache={}

def  solve_game(depth,balls):
    if balls in cache:
        return cache[bls]
    if depth==k:
        return w-balls.count("W")