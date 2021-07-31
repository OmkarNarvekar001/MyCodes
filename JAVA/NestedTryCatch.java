import java.util.Scanner;
public class NestedTryCatch
 {
	public static void main(String[] args) 
	{
		Scanner sc=new Scanner(System.in);
		try
		{
		try 
		   {
			System.out.println("Enter two numbers: ");
			int a=sc.nextInt();
			int b=sc.nextInt();
			System.out.println("Product="+(a*b));
			}	
			catch(Exception e) 
		    {
				System.out.println(e+"; Enter an Integer value!!!");
		    }
		try 
		   {
			    System.out.println("Enter the size of array:");
                int s=sc.nextInt();				
				int arr[]=new int[s];
		        System.out.println("Enter the elements:");
				arr[s]=sc.nextInt();
			}
	        catch(ArrayIndexOutOfBoundsException e) 
		    {
				System.out.println(e);
		    }
		}
		catch(Exception e)
		{
			System.out.println(e);
		}
		
	
	}

}