//overloading by changing data type of arguments.
import java.util.Scanner;
class Calculate
{
  int Calculate (int a, int b)
  {
    System.out.println("Sum of "+a+" + "+b+"= "+(a+b)) ;
	return a+b;
  }
  float Calculate (float a, float b)
  {
    System.out.println("Sum of "+a+" + "+b+"= "+(a+b));
	return a+b;
  }
  
}	

public class Overload
{
	public static void main (String[] args)
  {
	Scanner sc=new Scanner(System.in);
	System.out.print("Enter first number: ");
	float x=sc.nextFloat();
	System.out.print("Enter Second number: ");
	float y=sc.nextFloat();
    Calculate  ca = new Calculate();
    ca.Calculate((int)x,(int)y);      
    ca.Calculate(x,y); 
  }
} 












  