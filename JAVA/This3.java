import java.util.Scanner;
class Func
{
	Func()
	{
		System.out.println("Default constructor.");
	}
	 Func(int a,int b)
	{
	this();
	System.out.println("Paremeterized constructor called");
	System.out.println("Product of the two numbers is: "+(a*b));
		
	}
}


public class This3{
	public static void main(String args[])
	{
		Scanner sc=new Scanner(System.in);
		System.out.print("Enter first number: ");
	    int x=sc.nextInt();
	    System.out.print("Enter Second number: ");
	    int y=sc.nextInt();
		Func ma=new Func(x,y);
	}
}