import java.util.Scanner;
public class floyd
{
	public static void main(String args[])
	{
		int rows,i,j,num=1;
		Scanner sc=new Scanner(System.in);
		System.out.println("Enter the number of rows:");
		rows=sc.nextInt();
		System.out.println("Floyds triangle:");
		for(i=1;i<=rows;i++)
		{
			for(j=1;j<=i;j++)
			{ 
		System.out.print(num +" ");
		num=num+1;
			}
			System.out.println("");
			
		}
	}
}
// OUTPUT:
// D:\java>javac floyd.java
// D:\java>java floyd
// Enter the number of rows:
// 5
// Floyds triangle:
// 1
// 2 3
// 4 5 6
// 7 8 9 10
// 11 12 13 14 15 


	