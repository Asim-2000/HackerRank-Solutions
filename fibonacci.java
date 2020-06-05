import java.util.Scanner;
public class fibonacci{
    int[] memo;

    public fibonacci(int N){
        memo=new int[N+1];
        for (int i=0;i<memo.length;i++){
            memo[i]=0;
        }
    }

    public int CalFib(int n){
        int result;
        if (memo[n]!=0){
            return  memo[n];
        }
        else if (n==1 || n==2){
            result=1;
            return result;
        }
        else{
            result=CalFib(n-1)+CalFib(n-2);
        }
        memo[n]=result;
        return result;
    }

    public static void main (String[] args){
        Scanner sc=new Scanner(System.in);
        int input=sc.nextInt();
        fibonacci fib=new fibonacci(input);
        System.out.println((fib.CalFib(input)));
        sc.close();
    }



}