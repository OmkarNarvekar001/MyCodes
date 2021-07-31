import java.util.Scanner;
public class Operation
{
 public static void main(String args[])
  {
    float num1,num2;
    float sum,diff,mult,div;
    
	Scanner sc= new Scanner(System.in);
    System.out.println("Enter first number:");
     num1=sc.nextFloat();
    System.out.println("Enter Second number:");
     num2=sc.nextFloat();
     sc.close();
    
	sum=num1+num2;
     System.out.println("Sum of two numbers:"+sum);
     diff=num1-num2;
     System.out.println("Difference of two numbers:"+diff);
     mult=num1*num2;
     System.out.println("Multiplication of two numbers:"+mult);
     div=num1/num2;
     System.out.println("Division of two numbers:"+div);
  }
}
