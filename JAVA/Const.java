
import java.util.Scanner;
class Fun
{
Fun()
{
	System.out.println("Default constructor called");
}

Fun(String na)
{
	System.out.println("Overloaded constructor called");
	System.out.println("Entered name :"+na);
}
}
public class Const
{
	public static void main (String []args)
	{
		Scanner sc=new Scanner(System.in);
		Fun f1=new Fun();
		System.out.println("Enter your name");
		String na=sc.nextLine();
		Fun f2=new Fun(na);
	}

}







