import java.util.Scanner;
class Main
{
	 void a(int l)
	{
		System.out.println("Method a called");
		System.out.println("Value of L="+l);
		
	}
	void b()
	{
		System.out.println(" Method b called");
		this.a(20);
	}
}


public class This2
{
	public static void main(String args[])
	{

		Main y=new Main();
		y.b();
		
	}
}