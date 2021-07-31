import java.util.Scanner;
class Prime
{
	public static void main(String[] args)
	{
		int r,c,i;
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the dimensions of an array:");
		r = sc.nextInt();
		c = sc.nextInt();
		int A[][] = new int[r][c];
		int B[] = new int[r*c];
		int k=2,cnt=0,y=0,j=0;
		while(j<r*c)
		{
			for(i=1; i<=k; i++)
			{
				if(k%i==0)
				{
					cnt++;
				}
			}
			if(cnt==2)
			{
				B[j] = k;
				j++;
			}
			cnt = 0;
			k++;
			//y++;
		}
		
		int x=0;
		for(i=0; i<r; i++)
		{
			for(j=0; j<c; j++)
			{
				A[i][j] = B[x];
				x++;
			}
		}
		
		System.out.println("Prime Array:");
		for(i=0; i<r; i++)
		{
			for(j=0; j<c; j++)
			{
				System.out.print(A[i][j]+"\t");
			}
			System.out.println();
		}
	}
}