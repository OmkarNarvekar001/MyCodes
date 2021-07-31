import java.util.Scanner;

interface area 
{
    void getArea(int length);
}

class Rectangle implements area 
{
    public void getArea(int length)
	{
        System.out.println("The area of the square = " + (length * length)+"sq.m");
    }
}

public class Interface2 
{
    public static void main(String[] args) 
	{
        Rectangle rect = new Rectangle();
		Scanner s=new Scanner(System.in);
		System.out.println("Enter the length of Square:");
		int l=s.nextInt();
        rect.getArea(l);
    }
}