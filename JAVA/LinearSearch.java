import java.util.Scanner;
public class LinearSearch
{
	public static void main(String []args)
	{
	  int i;
	  Scanner sc=new Scanner(System.in);
	  System.out.println("Enter the size of the array: ");
	  int n=sc.nextInt();
	  int a[]=new int[n];
	  System.out.println("Enter "+n+" elements in the array: ");
	  for(i=0;i<n;i++)
	  {
		  a[i]=sc.nextInt();
	  }
	  System.out.println("Enter the element to be searched: ");
	  int s=sc.nextInt();
	  
	  for(i=0;i<n;i++)
	  {
		  if(a[i]==s)
		  {
			  System.out.println("Element "+s+" found at index: "+i);
			  break;
		  }
		  
	  }
	  
	  if(i==n)
	  {
		   System.out.println("Element "+s+" not found!!");
	  }
	  
	  
	  
	}
	
}