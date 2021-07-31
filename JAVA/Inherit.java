import java.util.Scanner;

class Inp
{
	Scanner sc=new Scanner(System.in);
	public float l;
	public float m;
	void accept()
	{
		System.out.println("Enter two numbers: ");
		l=sc.nextFloat();
		m=sc.nextFloat();
	}
	void disp()
	{
		System.out.println("First number= "+l);
		System.out.println("Second number= "+m);
	}
}

class Calc extends Inp
{
	 void add()
	 {
		 System.out.println("Sum of two numbers= "+(l+m));
	 }
	 
	 void sub()
	 {
		 System.out.println("Difference of two numbers= "+(l-m));
	 }
	 
	 void pro()
	 {
		 System.out.println("Product of two numbers= "+(l*m));
	 }
	 
	 void div()
	 {
		 System.out.println("Division of two numbers= "+(l/m));
	 }
}

class Modulo extends Calc
{
	void modulus()
	{
		System.out.println("Remainder of two numbers= "+(l%m));
	}
}

public class Inherit 
{
	public static void main(String [] args)
	{
		Modulo m=new Modulo();
		m.accept();
		m.disp();
		m.modulus();
		m.add();
		m.sub();
		m.pro();
		m.div();
	}
}