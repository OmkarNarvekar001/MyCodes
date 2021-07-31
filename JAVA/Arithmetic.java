import java.util.Scanner;
public class Arithmetic
{
	public static void main(String args[])
	{
		float num1,num2,result;
            Scanner sc = new Scanner(System.in); 
                System.out.print("Enter first number:");
                num1 =sc.nextFloat();
                System.out.print("Enter second number:");
                num2 = sc.nextFloat();
       
		result = num1 + num2;
        System.out.println("num1 + num2 = " + result);
		
		 result = num1 - num2;
        System.out.println("num1 - num2 = " + result);
    	
      
        result = num1 * num2;
        System.out.println("num1 * num2 = " + result);

        
        result = num1 / num2;
        System.out.println("num1 / num2 = " + result);
    	
      
        result = num1 % num2;
        System.out.println("num1 % num2 = " + result);
    }
}



/* OUTPUT:

D:\java>javac Arithmetic.java
D:\java>java Arithmetic
Enter first number:12.6
Enter second number:8.67
num1 + num2 = 21.27
num1 - num2 = 3.9300003
num1 * num2 = 109.242004
num1 / num2 = 1.4532872
num1 % num2 = 3.9300003
*/








		
		
		