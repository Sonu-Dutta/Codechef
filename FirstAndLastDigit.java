
import java.util.Scanner;

class FirstAndLastDigit
{
    public static void main (String[] args) 
    {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter number of test cases: ");
        int T=sc.nextInt();
        while(T-->0){
            System.out.println("Enter number: ");
            int n=sc.nextInt();
            int [] a=new int[100];
            int i=0;
            while(n!=0){
                a[i]=n%10;
                n=n/10;
                i++;
            }
            int sum=a[0]+a[i-1];
            System.out.println(sum);
        }
    }
}