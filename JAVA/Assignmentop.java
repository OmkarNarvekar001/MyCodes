public class Assignmentop 
{

   public static void main(String args[]) 
   {
      float a = 20;
      float b = 15;
      float c ;

      c = a + b;
      System.out.println("c = a + b = " + c );

      c += a ;
      System.out.println("c += a  = " + c );

      c -= a ;
      System.out.println("c -= a = " + c );

      c *= a ;
      System.out.println("c *= a = " + c );

      a = 22;
      c = 9;
      c /= a ;
      System.out.println("c /= a = " + c );

      a = 10;
      c = 15;
      c %= a ;
      System.out.println("c %= a  = " + c );
   }
}


/* OUTPUT:
D:\java>javac Assignmentop.java
D:\java>java Assignmentop 
c = a + b = 35.0
c += a  = 55.0
c -= a = 35.0
c *= a = 700.0
c /= a = 0.4090909
c %= a  = 5.0 */













