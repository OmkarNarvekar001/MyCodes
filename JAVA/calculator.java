import java.util.Scanner;
public class calculator
 {
    public static void main(String[] args)
	{
        float num1, num2;
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter first number:");
        num1 = scanner.nextFloat();
        System.out.print("Enter second number:");
        num2 = scanner.nextFloat();
		
        System.out.print("Enter an operator (+, -, *, /): ");
        char operator = scanner.next().charAt(0);
        scanner.close();
        
		double output;   
		scanner.close();
        switch(operator)
        {
            case '+':
            	output = num1 + num2;
                break;

            case '-':
            	output = num1 - num2;
                break;

            case '*':
            	output = num1 * num2;
                break;

            case '/':
            	output = num1 / num2;
                break;

            default:
                System.out.printf("You have entered wrong operator");
                return;
        }

        System.out.println(num1+" "+operator+" "+num2+"= "+output);
    }
}

// OUTPUT:
// D:\java>javac calculator.java
// D:\java>java calculator
// Enter first number:25
// Enter second number:4
// Enter an operator (+, -, *, /): /
// 25.0 / 4.0= 6.25

   
			
	 
  
