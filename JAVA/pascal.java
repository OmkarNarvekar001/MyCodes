import java.util.Scanner;
public class pascal{

  public static void main(String[] args)
{
    int row,c=1,k,i,j;
    System.out.println("Input number of rows: ");
    Scanner in = new Scanner(System.in);
		    row = in.nextInt();
	System.out.println("Pascals Triangle:");		
    for(i=0;i<row;i++)
    {
        for(k=1;k<=row-i;k++)
        System.out.print(" ");
        for(j=0;j<=i;j++)
        {
            if (j==0||i==0)
                c=1;
            else
               c=c*(i-j+1)/j;
            System.out.print(" "+c);
        }
        System.out.println(" ");
    }
}
}

// D:\java>javac pascal.java
// D:\java>java pascal
// Enter the number of rows:
// 5
// Pascals Triangle:
                         // 1
                      // 1    1
                     // 1  2   1
                   // 1  3   3   1
                 // 1  4   6   4   1
               // 1  5  10  10  5  1

