import java.util.Scanner;

class input
{
	int l,m;
	void input()
	{  
	try
     	{
		Scanner sc=new Scanner(System.in);
		System.out.println("Enter two numbers of which tables are to be displayed:");
		l=sc.nextInt();
		m=sc.nextInt();
		}
		catch(Exception e)
		{
			System.out.println(e);
		}
	}
}

class Mult extends input
{
	public void run()
	{
		int i;
		for(i=0;i<11;i++)
		{
			System.out.print(l+"X"+i+" = "+(l*i)+"\t");
            System.out.print(" ");
			try
			{
			Thread.sleep(1000);
			System.out.print(m+"X"+i+" = "+(m*i)+" \t");
			Thread.sleep(1000);
			System.out.println();
		   }
		
		catch(Exception e)
		{
			System.out.println(e);
		}
		}
	}
}

public class Thread3
{
	public static void main(String [] args)
	{
		Mult t=new Mult();
		t.input();
		t.run();
	}
}