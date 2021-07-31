import java.util.Scanner;
abstract class Shape
{
	abstract void accept();
	abstract double calculate();
    void display(double area)
	{
		System.out.println("The area is:"+area);
	}
}
class circle extends Shape
{
	Scanner s;
	double r;
	double area;

    circle() {
        this.s = new Scanner(System.in);
    }
        @Override
	public void accept()
	{
		System.out.println("Enter the radius");
		 r=s.nextDouble();
	}
        @Override
	double calculate()
	{
	 area= 3.14*r*r;
	 return area;
	}
}
public class abst1
{
	public static void main(String args[])
	{
		circle c=new circle();
		c.accept();
		double area=c.calculate();
		c.display(area);
	}
}