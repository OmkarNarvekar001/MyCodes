import java.util.Scanner;
public class Str
{
	public static void main(String [] args)
	{
		Scanner sc=new Scanner(System.in);
		System.out.println("Enter String 1:");
		String s1=sc.nextLine();
		System.out.println("Enter String 2:");
		String s2=sc.nextLine();
		System.out.println("Enter String 3:");
		String s3=sc.nextLine();
		System.out.println("Enter String 4:");	
		String s4=sc.nextLine();
		
		System.out.println();
		System.out.println("For String 1 Character at index 3 : "+s1.charAt(3)+" and index 5: "+s1.charAt(5));
		System.out.println("For String 2 Character at index 3 : "+s2.charAt(3)+" and index 5: "+s2.charAt(5));
		System.out.println("For String 3 Character at index 3 : "+s3.charAt(3)+" and index 5: "+s3.charAt(5));
		System.out.println("For String 4 Character at index 3 : "+s4.charAt(3)+" and index 5: "+s4.charAt(5));
		System.out.println();

        System.out.println();
		System.out.println("Concatenate String 1 and String 2: "+s1.concat(" "+s2));
		System.out.println("Concatenate String 3 and String 4: "+s3.concat(" "+s4));
		System.out.println();
		
		System.out.println();	
		String s5=s1;	
		String s6=s2;
		System.out.println("String 5 in upper case: "+s5.toUpperCase());
		System.out.println("String 6 in lower case: "+s6.toLowerCase());
		System.out.println();
		
		System.out.println();
		System.out.println("Comparing String 1 and String 5 ignoring the case:"+s1.equalsIgnoreCase(s5));
		System.out.println("Comparing String 2 and String 6 ignoring the case:"+s2.equalsIgnoreCase(s6));
		System.out.println();
		
		System.out.println();
		System.out.println("Length of S1:"+s1.length());
		System.out.println("Length of S2:"+s2.length());
		System.out.println("Length of S3:"+s3.length());
		System.out.println("Length of S4:"+s4.length());
		System.out.println("Length of S5:"+s5.length());
		System.out.println("Length of S6:"+s6.length());
		System.out.println();
		
		System.out.println();
		System.out.println("Replacing String 1 with String 2: "+s1.replace(s1,s2));
		System.out.println("Replacing String 2 with String 3: "+s2.replace(s2,s3));
		System.out.println("Replacing String 3 with String 4: "+s3.replace(s3,s4));
		System.out.println("Replacing String 4 with String 5: "+s4.replace(s4,s5));
		System.out.println("Replacing String 5 with String 6: "+s5.replace(s5,s6));
		System.out.println("Replacing String 6 with String 1: "+s6.replace(s6,s1));
		System.out.println();
		
		System.out.println();
		System.out.println("String 1 in lower case:"+s1.toLowerCase());
		System.out.println("String 2 in lower case:"+s2.toLowerCase());
		System.out.println("String 3 in lower case:"+s3.toLowerCase());
		System.out.println("String 4 in lower case:"+s4.toLowerCase());
		System.out.println();
		System.out.println("String 1 in lower case:"+s1.toUpperCase());
		System.out.println("String 2 in lower case:"+s2.toUpperCase());
		System.out.println("String 3 in lower case:"+s3.toUpperCase());
		System.out.println("String 4 in lower case:"+s4.toUpperCase());
		System.out.println();
		
		System.out.println();
		System.out.println("Substring of s2: "+s2.substring(2,6));
		System.out.println("Substring of s3: "+s3.substring(1,5));
		System.out.println("Substring of s4: "+s4.substring(3));
		System.out.println();
		
       System.out.println();
	   System.out.println("Comparing String 1 and String 2:"+s1.compareTo(s2));
	   System.out.println("Comparing String 2 and String 3:"+s2.compareTo(s3));
       System.out.println();
	   
	   System.out.println();
	   System.out.println("Comparing String 1 and String 2 ignoring case:"+s1.compareToIgnoreCase(s2));
	   System.out.println("Comparing String 3 and String 5 ignoring case:"+s3.compareToIgnoreCase(s5));
	   System.out.println("Comparing String 2 and String 6 ignoring case:"+s2.compareToIgnoreCase(s6));
       System.out.println();
	    
		System.out.println("Trim String 1:"+s1.trim());
	   
	}
	
}