import java.util.Scanner;
public class MatAdd
{
	public static void main(String []args)
	{
		int i,j;
		Scanner sc=new Scanner(System.in);
		System.out.println("Enter the dimention of Matrix 1: ");
		int m1=sc.nextInt();
		int n1=sc.nextInt();
		System.out.println("Enter the dimention of Matrix 2: ");
		int m2=sc.nextInt();
		int n2=sc.nextInt();
		
		int a[][]=new int[m1][n1];
		int b[][]=new int[m2][n2];
		int c[][]=new int [m1][n1];
		
		
		if(m1==m2 && n1==n2)
		{
			System.out.println("Enter elements of Matrix A: ");
		for(i=0;i<m1;i++)
		{
			for(j=0;j<n1;j++)
			{
				a[i][j]=sc.nextInt();
			}
		}
		
		System.out.println("Enter elements of Matrix B: ");
		for(i=0;i<m2;i++)
		{
			for(j=0;j<n2;j++)
			{
				b[i][j]=sc.nextInt();
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
		
		System.out.println("Elements of Matrix B: ");
		for(i=0;i<m2;i++)
		{
			for(j=0;j<n2;j++)
			{
				System.out.print(" "+b[i][j]);
			}
			System.out.println("");
		}
		
		for(i=0;i<m1;i++)
		{
		    for(j=0;j<n1;j++)
			{
				c[i][j]=a[i][j]+b[i][j];
			}
		}
		
		System.out.println("Sum of Matrix A and B is: ");
		for(i=0;i<m1;i++)
		{
		    for(j=0;j<n1;j++)
			{
					System.out.print(" "+c[i][j]);
			}
			System.out.println("");
		}
		
		
		
	    }
		else
		{
			System.out.println("Addition not possible");
		}
	}
		
		
}
