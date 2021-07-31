import java.util.Scanner;
public class area
{
 public static void main(String args[])
 {
  Scanner sc=new Scanner(System.in);
  System.out.println("Menu");
  System.out.println("1.Square");
  System.out.println("2.Recatngle");
  System.out.println("3.Circle");
  System.out.println("4.Triangle");
  System.out.println("5.Trapezoidal");
  System.out.println("6.Exit");
  System.out.println("Print your option:");
     
	 int op=sc.nextInt();
	   
	 switch(op)
     {
        case 1:  System.out.println("Enter side of Square:");
                float x=sc.nextFloat();
				float as=x*x;
				 System.out.println("Area of Square="+as);
				 break;
	 
	 
		 case 2:  System.out.println("Enter length and breath of Recatngle:");
		        float l=sc.nextFloat();
				float b=sc.nextFloat();
				float y=l*b;
				 System.out.println("Area of Rectangle="+y);
				 break;
	 
	 
		 case 3:  System.out.println("Enter Radius of Circle:");
		         double r=sc.nextDouble();
				 double z=3.14*r*r;
				  System.out.println("Area of Circle:"+z);
				  break;
	 
	 
		 case 4:  System.out.println("Enter Height and Base of Triangle:");
		        double bas=sc.nextDouble();
				double h=sc.nextDouble();
				double xx=0.5*bas*h;
				System.out.println("Area of Triangle="+xx);
				break;
				 
	 
	 
	     case 5:  System.out.println("Enter Height and Bassesof Trapezoidal:");
		        float he=sc.nextFloat();
				float b1=sc.nextFloat();
				float b2=sc.nextFloat();
				double aa=0.5*(b1+b2)*he;
				System.out.println("Area of Trapezoidal="+aa);
				break;
	 
	 
	  default:
	 }
 }
}
			
				
	   
  
