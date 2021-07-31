import java.util.*;
import java.lang.Math.*;

class shape
{
	void shape(double r)
	{
		System.out.println("Entered radius is "+r);
		System.out.println("Area of Circle is= "+Math.PI*r*r);
		System.out.println();
	}
	
	void shape(float l,float m)
	{
		System.out.println("Entered length= "+l+" & breadth= "+m);
		System.out.println("Area of Rectangle= "+(l*m));
		System.out.println();
	}
	
	void shape(float sq)
	{
		System.out.println("Entered side of the square= "+sq);
		System.out.println("Area of Square= "+(sq*sq));
		System.out.println();
	}
}




public class Coverload
{
public static void main(String []args)
{
	Scanner sc=new Scanner(System.in);
		System.out.println("Enter the radius of the circle: ");
		double r=sc.nextDouble();
		System.out.println();
		System.out.println("Enter the length and breadth of rectangle: ");
		float l=sc.nextFloat();
		float m=sc.nextFloat();
		System.out.println();
		System.out.println("Enter the side of the square:");
		float sq=sc.nextFloat();
		System.out.println();
		shape s=new shape();
		s.shape(r);
		s.shape(l,m);
		s.shape(sq);
	
}
}

/* OUTPUT

D:\JAVA>javac Coverload.java

D:\JAVA>java Coverload
Enter the radius of the circle:
23

Enter the length and breadth of rectangle:
6.7 5.8

Enter the side of the square:
8

Entered radius is 23.0
Area of Circle is= 1661.9025137490005

Entered length= 6.7 & breadth= 5.8
Area of Rectangle= 38.86

Entered side of the square= 8.0
Area of Square= 64.0 */