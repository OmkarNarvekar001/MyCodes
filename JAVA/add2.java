import java.util.Scanner;
public class add2
{
 public static void main(String args[])
  {
    float num1,num2,sum=0;
	Scanner sc= new Scanner(System.in);
    System.out.println("Enter first number:");
     num1=sc.nextFloat();
    System.out.println("Enter Second number:");
      num2=sc.nextFloat();
     sc.close();
    
	sum=num1+num2;
     System.out.println("Sum of two numbers:"+sum);

  }
}

// OUTPUT:
// D:\java>javac add2.java

// D:\java>java add2
// Enter first number:
// 10
// Enter Second number:
// 5
// Sum of two numbers:15.0

// D:\java>