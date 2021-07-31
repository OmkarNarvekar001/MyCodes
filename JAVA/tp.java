import java.util.*;

class bike
{
	Scanner sc=new Scanner(System.in);
	double rate;
	void inp()
	{
		System.out.println("Choose a model");
		System.out.println("1\n2\n3\n4\n");
	}
	void op()
	{
		int opt=sc.nextInt();
		switch(opt)
        {
			case 1: System.out.println("Rate of model 1=100000");
			        break;
			case 2: System.out.println("Rate of model 2=700301");
			           break;
			case 3: System.out.println("Rate of model 3=239876");
			         break;
			case 4: System.out.println("Rate of model 4=2390000");
			        break;
		}

	}
}

class car 
{
	Scanner sc=new Scanner(System.in);
	double rate;
	void inp()
	{
		System.out.println("Choose a model");
		System.out.println("1\n2\n3\n4\n");
	}
	void op()
	{
		int opt=sc.nextInt();
		switch(opt)
        {
			case 1: System.out.println("Rate of model 1=20000");
			        break;
			case 2: System.out.println("Rate of model 2=300000");
			           break;
			case 3: System.out.println("Rate of model 3=600000");
			         break;
			case 4: System.out.println("Rate of model 4=AUkat ke bahar");
			        break;
		}

	}
}

public class tp
{
	public static void main(String [] args)
	{
		Scanner sc=new Scanner(System.in);
		System.out.println("What would you like\n1.BIKE\n2.CAR");
		System.out.println("Enter ur choice:");
		int ch=sc.nextInt();
		switch(ch)
		{
			case 1: bike b=new bike();
			             b.inp();
						 b.op();
						break;
			
			 case 2: car r=new car();
			             r.inp();
						 r.op();
						 break;
						  
		}	
	}
}