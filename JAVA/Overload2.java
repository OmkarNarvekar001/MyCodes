//Overloading by changing number of arguments
import java.util.Scanner;
class multiply
{
  void multiply(float l, float b)
  {
    System.out.println("Product of "+l+" * "+b+" = "+(l*b)) ;
  }
  void multiply(float l, float b, float h)
  {
    System.out.println("Product of "+l+" * "+b+" * "+h+" = "+(l*b*h));
  }
  
}

public class Overload2
{
	public static void main(String[] args)
  {
	Scanner sc=new Scanner(System.in);
	System.out.print("Enter first number: ");
	float x=sc.nextFloat();
	System.out.print("Enter Second number: ");
	float y=sc.nextFloat();
	System.out.print("Enter Third number: ");
	float z=sc.nextFloat();
    multiply  ar = new multiply();
    ar.multiply(x,y);   
    ar.multiply(x,y,z);   
  } 
}