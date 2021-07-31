import java.util.Scanner;
public class areaofshape
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
		
		int op=sc.nextInt();
		switch(op)
		{
			case 1: 
			    System.out.println("Enter side of Square:");
                float x=sc.nextFloat();
				float as=x*x;
				System.out.print("");
				System.out.println("Area of Square="+as);
				 break;
				 
			 case 2:
			    System.out.println("Enter length and breath of Recatngle:");
			    System.out.print("Enter Length:");
		        float l=sc.nextFloat();
				System.out.print("Enter Breath:");
				float b=sc.nextFloat();
				float y=l*b;
				System.out.print(" ");
				System.out.println("Area of Rectangle="+y);
				 break;
				 
			case 3:
			    System.out.println("Enter Radius of Circle:");
		        double r=sc.nextDouble();
				double z=3.14*r*r;
				System.out.print(" ");
				System.out.println("Area of Circle:"+z);
			    break;
				
			case 4:
			    System.out.println("Enter Base and Height of Triangle:");
			    System.out.print("Enter Base:");
		        double bas=sc.nextDouble();
				System.out.print("Enter Height:");
				double h=sc.nextDouble();
				double xx=0.5*bas*h;
				System.out.println(" ");
				System.out.println("Area of Triangle="+xx);
				break;
				
			case 5:
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
				
				default:
		System.out.println("You have entered wrong option");
		return;
		}
		
	}
}

//OUTPUT:
// D:\java>javac areaofshape.java

// D:\java>java areaofshape
// Menu:
// 1.Square
// 2.Reactagle
// 3.Circle
// 4.Triangle
// 5.Trapezoidal

// Select shape of which area is to be found:3
// Enter Radius of Circle:
// 5.5
 // Area of Circle:94.985

// D:\java>
             			
		
