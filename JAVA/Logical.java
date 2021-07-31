import java.util.Scanner;
public class Logical
{
public static void main(String[] args)
   {
    	
        boolean result;
		float num1,num2,num3;
		Scanner sc=new Scanner(System.in);
		System.out.print("Enter first number:");
         num1 =sc.nextFloat();
        System.out.print("Enter second number:");
         num2 = sc.nextFloat();
		System.out.print("Enter third number:");
         num3 = sc.nextInt();
		sc.close();
        result = (num1 > num2) || (num3 > num1);        
        System.out.println("(num1 > num2) || (num3 > num1)="+result);        	
        result = (num1 > num2) && (num3 < num1);        
        System.out.println("(num1 > num2) && (num3 < num1)="+result);
		result = (num1 > num3) && (num2 > num1);        
        System.out.println("(num1 > num3) && (num2 > num1)="+result);
		 result = (num1 > num3) || (num3 < num1);        
        System.out.println("(num1 > num3) || (num3 < num1)="+result); 
    }
}


/* OUTPUT:

D:\java>javac Logical.java
D:\java>java Logical
Enter first number:20                                                                                                           
Enter second number:10                                                                                                          
Enter third number:15                                                                                                           
(num1 > num2) || (num3 > num1)=true                                                                                             
(num1 > num2) && (num3 < num1)=true                                                                                             
(num1 > num3) && (num2 > num1)=false                                                                                            
(num1 > num3) || (num3 < num1)=true          
 */












