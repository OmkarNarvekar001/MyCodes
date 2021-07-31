import java.util.Scanner;
public class TryCatch
{
	public static void main (String[] args)
	{
        Scanner sc = new Scanner(System.in);
	    int num ;
        System.out.print("Enter an integer: ");
	    try
	       {
	         num = sc.nextInt();
	         System.out.println("The square of " + num + " is " + num*num );
	       }
	    catch(Exception e)
	       {
	          System.out.println(e+"!!!Enter an Integer value.");
	          System.out.println("Run the program again." );
	       }
	System.out.println("Good-by" );

	}
}