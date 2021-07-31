import java.util.Scanner;
class Main 
{
    int age;
    Main(int age)
	{
        this.age = age;
    }
}

public class This1
{
	public static void main(String[] args) 
	{
		Scanner sc=new Scanner(System.in);
		System.out.println("Enter the age of object:");
		int a=sc.nextInt();
        Main obj = new Main(a);
        System.out.println("object age = " + obj.age);
    }
}