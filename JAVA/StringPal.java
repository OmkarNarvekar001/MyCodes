import java.util.Scanner;
class StringPal
{
	public static void main(String [] args)
	{
		
		String reverse="";
		Scanner sc=new Scanner(System.in);
		System.out.println("Enter the string: ");
		String s1=sc.nextLine();		
		int length=s1.length();
		System.out.println("Length of string is:"+s1.length());
		for(int i=s1.length()-1;i>=0;i--)
		{
			reverse = reverse + s1.charAt(i);
		}
			if(s1.equals(reverse))
			{
				System.out.println("String is pallindrome");
			}	
            else
            System.out.println("String is not pallindrome");				
	}
}