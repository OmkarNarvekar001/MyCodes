import java.util.Scanner;
public class MatMult
{
	public static void main(String []args)
	{
		int i,j,k;
		Scanner sc=new Scanner(System.in);
		System.out.println("Enter the dimentions of Matrix A:");
		int m1=sc.nextInt();
		int n1=sc.nextInt();
		System.out.println("Enter the dimention of Matrix B:");
		int m2=sc.nextInt();
		int n2=sc.nextInt();
		
		int a[][]=new int[m1][n1];
		int b[][]=new int[m2][n2];
		int c[][]=new int[m2][n1];
		
		
		if(n1==m2)
		{
			System.out.println("Enter the Elements of Matrix A:");
			for(i=0;i<m1;i++)
			{
				for(j=0;j<n1;j++)
				{
					a[i][j]=sc.nextInt();
				}
			}
			
			System.out.println("Enter the Elements of Matrix B:");
			for(i=0;i<m2;i++)
			{
				for(j=0;j<n2;j++)
				{
					b[i][j]=sc.nextInt();
				}
			}
			
			System.out.println("Elements of Matrix A:");
			for(i=0;i<m1;i++)
			{
				for(j=0;j<n1;j++)
				{
					System.out.print(" "+a[i][j]);
				}
				System.out.println("");
			}
			
			System.out.println("Elements of Matrix B:");
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
				for(j=0;j<n2;j++)
				{
					c[i][j]=0;
					{
					   for(k=0;k<m2;k++)
					  {
						c[i][j]+=a[i][k]*b[k][j];
					  }
					}
				}
			}
			
			System.out.println("Multiplication of Matrix A and B is:");
			{
				for(i=0;i<m1;i++)
			{
				for(j=0;j<n2;j++)
				{
					System.out.print("   "+c[i][j]);
				}
				System.out.println("");
			}
			}			
		}
		else
		{
			System.out.println("Multiplication not possible");
		}
	}
}