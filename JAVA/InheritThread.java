class A extends Thread
{
    public void run()
    {
        System.out.println("Thread A ");
    }
}
class B extends Thread
{
    public void run()
    {
        System.out.println("Thread B ");
    }
}
class C extends Thread
{
    public void run()
    {
        System.out.println("Thread C ");
    }
}
public class InheritThread
 {
    public static void main(String args[]) throws Exception
    {
        A a=new A();
        B b=new B();
        C c=new C();
        a.start();
        b.start();
        c.start();
    }
}