import java.util.Scanner;
class ReverseString
{
	public static void main(String [] args)
	{
		String reverse="";
		Scanner sc=new Scanner(System.in);
		System.out.println("Enter the string: ");
		String s1=sc.nextLine();		
		int length;
                 length = s1.length();
		System.out.println("Length of string is:"+s1.length());
		for(int i=s1.length()-1;i>=0;i--)
		{
			reverse = reverse + s1.charAt(i);
		}
			System.out.println("Reversed string: "+reverse);
	}
}