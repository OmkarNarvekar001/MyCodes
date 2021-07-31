class leap extends Thread
{
	public void run()
	{
		for( int i=2000;i<=2050;i++)
		{
			if(i%4==0)
            System.out.println(""+i+" is Leap Year");
        else
            System.out.println(""+i+" Not a Leap Year");
			
		}
	}
}
class zero extends Thread
{
	public void run()
	{
		for(int i=2000;i<=2050;i++)
		{
			int k = 0;
			int b = i;
			while(b!=0)
			{
				if(b % 10 == 0)
					k++;
				b=b/10;
			}
			if(k>1)
				System.out.println("\n"+i+" has "+k+" zeros.");
			else
				System.out.println("\n"+i+" has 1 zero");
		}
	}
}
public class LeapYear
{
	public static void main(String args[])
	{
		leap ob1 = new leap();
		zero ob2 = new zero();
		ob1.start();
		ob2.start();
	}
}