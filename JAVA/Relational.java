
import java.util.Scanner;
public class Relational {
    public static void main(String[] args) 
	{
		float num1,num2;
    	Scanner sc=new Scanner(System.in);
		System.out.print("Enter first number:");
        num1 =sc.nextFloat();
        System.out.print("Enter second number:");
        num2 = sc.nextFloat();
		sc.close();      
        if (num1 > num2) 
		{
            System.out.println("number1 > number2.");
        }
        else if(num1 < num2)
		{
            System.out.println("number1 < number2.");
        }
		else if(num1 == num2)
		{
			System.out.println("number1 == number2.");
		}
		
    }
}



/* OUTPUT:

D:\java>javac Relational.java
D:\java>java Relational
Enter first number:10
Enter second number:5
number1 > number2.

Enter first number:10
Enter second number:50
number1 < number2.

Enter first number:15
Enter second number:15
number1 == number2. */