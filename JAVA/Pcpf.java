import java.util.Scanner;
import java.lang.Math.*;
class Shapes
{
	double a;
	int b;
	int c,d;
	
	Shapes(double r)
	{
		System.out.println("Radius of Circle="+r);
	}
	
	Shapes(int a)
	{
		System.out.println("Side of Square is="+a);
	}
	
	Shapes(int l, int b)
	{
		System.out.println("Length of Rectangle="+l+" and Breath="+b);
	}
	
	float area(int l, int b)
	{
		return l*b;
	}
	
	double area(double rad)
	{
		return Math.PI*rad*rad;
	}
	
	float area(int a)
	{
		return a*a;
	}
}
public class Pcpf
{
	public static void main(String args[])
	{
		Scanner sc=new Scanner(System.in);
		System.out.print("Enter radius:");
		double a=sc.nextDouble();
		Shapes circle= new Shapes(a);
		System.out.println("The area of circle:"+circle.area(a));
		
		System.out.println("");
		System.out.print("Enter side of square:");
		int b= sc.nextInt();
		Shapes square= new Shapes(b);
		System.out.println("Area of square: "+square.area(b));
		
		System.out.println("");
		System.out.print("Enter length and breadth:");
		int c=sc.nextInt();
		int d=sc.nextInt();
		Shapes rect= new Shapes(c,d);
		System.out.println("Area of rectangle: "+rect.area(c,d));
	}
}