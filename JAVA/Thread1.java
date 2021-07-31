import java.util.Scanner;
public class Thread1
{
    public static void main(String args[]) 
    {
		try
		{
		Scanner sc=new Scanner(System.in);
		int m;
		System.out.println("Ente the range upto which numbers should be printed:");
		m=sc.nextInt();
		Thread t=Thread.currentThread();
        System.out.println("Thread: "+t);
        t.setName("Thread2");
        System.out.println(t);
        for(int i=1;i<=m;i++)
        {
            System.out.println(i);
            t.sleep(1000);
        }
		}
		catch(Exception e)
		{
			System.out.println(e);
		}
       
    }
}