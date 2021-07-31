import java.util.Scanner;

public class MultipleCatch
 {

    public static void main(String[] args)
	{
        try{
            Scanner sc =new Scanner(System.in);
			System.out.println("Enter the size of array:");
            int s=sc.nextInt();				
     		int arr[]=new int[s];
		    System.out.println("Enter the elements:");
		    arr[s]=sc.nextInt();
			System.out.println("The elements of matrix:");
			for(int i=0;i<=5;i++)
			{
				System.out.println(" "+arr[i]);
			}
        }
		
        catch(ArrayIndexOutOfBoundsException e)
        {
            System.out.println(e);
        }
         catch(Exception e)
        {
            System.out.println(e);
        } 
    }
}