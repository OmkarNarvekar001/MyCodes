public class Datatype
{ 
    public static void main(String args[]) 
    {               
        int i = 89;        
        byte b = 4;       
        short s = 56;        
        double d = 4.35545d;         
        float f = 9.73f; 
		boolean c=false;
		long e=56654l;
  
        System.out.println("integer: " + i); 
        System.out.println("byte: " + b); 
        System.out.println("short: " + s); 
        System.out.println("float: " + f); 
        System.out.println("double: " + d);
        System.out.println("boolean: " + c);		
    } 
} 


/* OUTPUT:
D:\java>javac Datatype.java
D:\java>java Datatype
integer: 89
byte: 4
short: 56
float: 9.73
double: 4.35545
boolean: false 
*/