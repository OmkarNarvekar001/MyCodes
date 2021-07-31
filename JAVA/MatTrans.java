import java.util.Scanner;
public class MatTrans
{
	public static void main(String []args)
	{
		int i,j;
		Scanner sc=new Scanner(System.in);
		System.out.println("Enter the dimention of Matrix 1: ");
		int m1=sc.nextInt();
		int n1=sc.nextInt();
		
		int a[][]=new int[m1][n1];
		int t[][]=new int[m1][n1];
		
		System.out.println("Enter elements of Matrix A: ");
		for(i=0;i<m1;i++)
		{
			for(j=0;j<n1;j++)
			{
				a[i][j]=sc.nextInt();
			}
		}
		
		System.out.println("Elements of Matrix A: ");
		for(i=0;i<m1;i++)
		{
			for(j=0;j<n1;j++)
			{
				System.out.print(" "+a[i][j]);
			}
			System.out.println("");
		}
		         
			System.out.println("Transpose of Matrix A :"); 
            for(i=0;i<m1;i++)
			{
				for(j=0;j<n1;j++)
				{
			     t[i][j]=a[j][i];	
                 System.out.print(" "+t[i][j]);				 
				}
				System.out.println("");
           }
		   

		
		
	}
}