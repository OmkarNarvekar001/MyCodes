import java.util.Scanner;
class Vowel
{
	public static void main(String [] args)
	{	
		int vowel=0;
		int cons=0;
		Scanner sc=new Scanner(System.in);
		System.out.println("Enter the string: ");
		String s1=sc.nextLine().toLowerCase();
        System.out.println("Enetered string:"+s1);		
		int length=s1.length();
		System.out.println("Length of string is:"+s1.length());
		for(int i=0;i<s1.length();i++)
        {
	     char ch = s1.charAt(i);
	      if(ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u')
	      {
		  vowel++;
	      }
	       else 
	      {
			  if(ch ==' ')
			  {
				  cons--;
		      }
			  
		      cons++;
	      }
        }
		System.out.println("In string Vowel= "+vowel+" and consonent= "+cons);
	}
	
}