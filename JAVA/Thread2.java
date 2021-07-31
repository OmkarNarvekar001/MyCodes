import java.util.Scanner;

class parent extends Thread
{
	public void run()
	{
		System.out.println();
		System.out.println("Class parent");
	}
	void even(int n)
	{
		try
		{
		int i;
		for(i=0;i<=n;i++)
	      {
		     if(i%2==0)
	           {
                System.out.println(i);
		        parent.sleep(1000);
		       }
		  }
		}
		catch(Exception e)
		{
			System.out.println(e);
		}
		
		
	}
}

class child extends Thread
{
	public void run()
	{
		System.out.println();
		System.out.println("Class child");
	}
	
	void odd(int m)
	{
		try
		{
		  int i;
          for(i=0;i<=m;i++)
		  {
			  if(i%2!=0)
			  {
				  System.out.println(i);
				  child.sleep(1000);
			  }
		  }			  
		}
		catch(Exception e)
		{
			System.out.println(e);
		}
	}
}





public class Thread2
{
	public static void main(String args [])
	{
		try
		{
		 Scanner sc=new Scanner(System.in);
		parent p=new parent();
		System.out.println("Enter the range upto which even number should be printed:");
		int n=sc.nextInt();
		child c=new child();
		System.out.println("Enter the range upto which even number should be printed:");
		int m=sc.nextInt();
		p.start();
		p.sleep(2000);
		p.even(n);
		c.start();
        c.sleep(2000);
        c.odd(m);	
		}
		catch(Exception e)
		{
			System.out.println(e);
		}
		
	}
}