import java.util.Scanner;
import java.lang.Math.*;

class Shape
{
	void Shape(double r)
	{
		System.out.println("The entered radius: "+r);
		System.out.println("Area of Circle: "+Math.PI*r*r);
		System.out.println();
		
	}
	void Shape(float l,float m)
	{
		System.out.println("Entered length= "+l+" & breath= "+m);
		System.out.println("Area of rectangle: "+(l*m));
		System.out.println();
	}
	void Shape(float sq)
	{
		System.out.println("Entered side= "+sq);
		System.out.println("Area of Square: "+(sq*sq));
		System.out.println();
	}
	
}

public class ConsShape
{
	public static void main(String [] args)
	{
		Scanner sc=new Scanner(System.in);
		System.out.println("Enter the radius of the circle: ");
		double r=sc.nextDouble();
		System.out.println();
		System.out.println("Enter the length and breath of rectangle: ");
		float l=sc.nextFloat();
		float m=sc.nextFloat();
		System.out.println();
		System.out.println("Enter the side of the square:");
		float sq=sc.nextFloat();
		System.out.println();
		Shape s=new Shape();
		s.Shape(r);
		s.Shape(l,m);
		s.Shape(sq);
	}
}