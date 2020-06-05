class fib:
    self.memo=[]
    def __init__(self,memo):
        pass        

    def fibonacci(self,n):
        if (self.memo[n]!=0):
            return self.memo[n]
        elif (n==1 or n==2):
            result=1
            return result
        else:
            result=fibonacci(n-1)+fibonacci(n-2)
        
        memo[n]=result
        return result


class main:
    memo=[]
    num=int(input())
    fibo=fib(memo)
    fibo.fibonacci(num)


if __name__=='__main__':
    main()

