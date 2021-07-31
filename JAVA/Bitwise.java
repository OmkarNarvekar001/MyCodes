import java.util.Scanner;
public class Bitwise
{
public static void main(String[] args)
   {
    	int a,b;
		Scanner sc=new Scanner(System.in);
		System.out.println("Enter first number:");
        a =sc.nextInt();
        System.out.println("Enter second number:");
        b = sc.nextInt();
		sc.close();
		System.out.println("Bitwise AND: a&b="+(a & b));
		System.out.println("Bitwise OR: a|b="+(a | b));
		System.out.println("Bitwise Complement: ~a= "+(~a));
		System.out.println("Bitwise XOR: a^b="+(a^b));
		System.out.println("Bitwise right shift: a>>1="+(a>>1));
		System.out.println("Bitwise left shift: b<<2="+(b<<2));
   }
}

/* OUTPUT:

D:\java>javac Bitwise.java
D:\java>java Bitwise
Enter first number:                                                                                                             
10                                                                                                                              
Enter second number:                                                                                                            
5                                                                                                                               
Bitwise AND: a&b=0                                                                                                              
Bitwise OR: a|b=15                                                                                                              
Bitwise Complement: ~a= -11                                                                                                     
Bitwise XOR: a^b=15                                                                                                             
Bitwise right shift: a>>1=5                                                                                                     
Bitwise left shift: b<<2=20  
 */







