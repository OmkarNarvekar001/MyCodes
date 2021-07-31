import java.util.Scanner;
class StringOcc
{
   public static void main(String [] args)
   {
	 int i;
	 String temp="";
    Scanner sc=new Scanner(System.in);
	System.out.println("Enter the string:");
	String s1=sc.nextLine();
	System.out.println("");
	String s=s1.toLowerCase();
	System.out.println("String in lower case: "+s);
	System.out.println("");
	int length=s.length();
	System.out.println("Enter the character to be deleted from String:");
	char c=sc.next().charAt(0);
	for(i=0;i<s.length();i++)
	{
		if(s.charAt(i)==c)
		{
			temp=s.replace(s.charAt(i),' ');
		}
	}
	System.out.println("String after removal of character "+c+": "+temp);
   }
}