import java.util.Scanner;
class StringCount
{
	public static void main(String [] args)
	{	
		int count=0,i;
		Scanner sc=new Scanner(System.in);
		System.out.println("Enter the string: ");
		String s1=sc.nextLine();		
		int length=s1.length();
		for(i=0;i<s1.length()-1;i++)
		{
			if(s1.charAt(i)==' ' && s1.charAt(i+1)!=' ')
			{
				count++;
			}
		}
		System.out.println("Number of words in the string:"+(count+1));
	}
}