import java.util.Scanner;
class Rectangle{
	float length,breath,area;
	void input()
	{
		Scanner sc=new Scanner(System.in);
		System.out.println("Enter the length and breath of Rectangle:");
		length=sc.nextFloat();
		breath=sc.nextFloat();
	}
	void calc()
	{
		area=length*breath;
		System.out.println("Area of rectangle="+area);
	}
}

class Circle{
	double radius,area;
	void input()
	{
		Scanner sc=new Scanner(System.in);
		System.out.println("Enter the radius of Circle:");
		radius=sc.nextDouble();
		
	}
	void calc()
	{
		area=3.14*radius*radius;
		System.out.println("Area of Circle="+area);
	}
}

class Square{
	double side,area;
	void input()
	{
		Scanner sc=new Scanner(System.in);
		System.out.println("Enter the Side of square:");
		side=sc.nextDouble();
		
	}
	void calc()
	{
		area=side*side;
		System.out.println("Area of Square="+area);
	}
}

class Triangle{
	double length,height,area;
	void input()
	{
		Scanner sc=new Scanner(System.in);
		System.out.println("Enter the length and Height of Triangle:");
		length=sc.nextDouble();
		height=sc.nextDouble();
		
	}
	void calc()
	{
		area=0.5*length*height;
		System.out.println("Area of Triangle="+area);
	}
}

class Trapezoidal{
	double base1,base2,height,area;
	void input()
	{
		Scanner sc=new Scanner(System.in);
		System.out.println("Enter the bases and height of Trapezoidal:");
		base1=sc.nextDouble();
		base2=sc.nextDouble();
		height=sc.nextDouble();
	}
	void calc()
	{
		area=0.5*(base1+base2)*height;
		System.out.println("Area of Trapezoidal="+area);
	}
}

public  class Shape2
{
	public static void main(String args[])
	{
		Rectangle r = new Rectangle();
		r.input();
		r.calc();
		
		Circle c = new Circle();
		c.input();
		c.calc();
		
		Square s=new Square();
		s.input();
		s.calc();
		
		Triangle t=new Triangle();
		t.input();
		t.calc();
		
		Trapezoidal tr =new Trapezoidal();
		tr.input();
		tr.calc();
		
		
	}
}
	
	
	
// D:\java>java Shape2
// Enter the length and breath of Rectangle:
// 12 6
// Area of rectangle=72.0
// Enter the radius of Circle:
// 5
// Area of Circle=78.5
// Enter the Side of square:
// 4
// Area of Square=16.0
// Enter the length and breath of Triangle:
// 10 4
// Area of Square=20.0
// Enter the bases and height of Trapezoidal:
// 10 5 15
// Area of rectangle=112.5
// D:\java>
	