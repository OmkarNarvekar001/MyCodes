import java.util.Scanner;
public class shape
{
	public static void main(String args[])
	{
		Scanner sc=new Scanner(System.in);
		 System.out.println("Menu:");
		 System.out.println("1.Square");
	     System.out.println("2.Reactagle");
		 System.out.println("3.Circle");
		 System.out.println("4.Triangle");
	     System.out.println("5.Trapezoidal");
		 System.out.println("");
		 System.out.print("Select shape of which area is to be found:");
		 
		 int num=sc.nextInt();
		 
		 
		 while (num>0 && num<6)
		 {	 
		 if (num==1)
		 {
			 System.out.println("Enter side of Square:");
                float x=sc.nextFloat();
				float as=x*x;
				System.out.print("");
				 System.out.println("Area of Square="+as);
				 break;
		 }
		 
		 else if (num==2)
		 {
			  System.out.println("Enter length and breath of Recatngle:");
			  System.out.print("Enter Length:");
		        float l=sc.nextFloat();
				System.out.print("Enter Breath:");
				float b=sc.nextFloat();
				float y=l*b;
				System.out.print(" ");
				 System.out.println("Area of Rectangle="+y);
				 break;
		 }
		 
		 else if (num==3)
		 {
			 System.out.println("Enter Radius of Circle:");
		         double r=sc.nextDouble();
				 double z=3.14*r*r;
				 System.out.print(" ");
				  System.out.println("Area of Circle:"+z);
				  break;
		 }
		 
		 else if (num==4)
		 {
			 System.out.println("Enter Base and Height of Triangle:");
			 System.out.print("Enter Base:");
		        double bas=sc.nextDouble();
				System.out.print("Enter Height:");
				double h=sc.nextDouble();
				double xx=0.5*bas*h;
				System.out.println(" ");
				System.out.println("Area of Triangle="+xx);
				break;
		 }
		 
		 else 
		 {
			  System.out.println("Enter Height and Basses of Trapezoidal:");
		        System.out.print("Enter Height:");
				float he=sc.nextFloat();
				System.out.print("Enter Base 1:");
				float b1=sc.nextFloat();
				System.out.print("Enter Basse 2:");
				float b2=sc.nextFloat();
				double aa=0.5*(b1+b2)*he;
				System.out.println(" ");
				System.out.println("Area of Trapezoidal="+aa);
				break;
		 }
		 
		 }
		 if (num>6)
			 System.out.println("Enter a valid option!");
			 
	}
}
	
// OUTPUT:
// D:\java>javac shape.java
// D:\java>java shape
// Menu:
// 1.Square
// 2.Reactagle
// 3.Circle
// 4.Triangle
// 5.Trapezoidal

// Select shape of which area is to be found:4
// Enter Base and Height of Triangle:
// Enter Base:4
// Enter Height:5

// Area of Triangle=10.0
	
	
	
	

	
	
