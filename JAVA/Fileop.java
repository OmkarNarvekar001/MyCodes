import java.io.*;

public class Fileop
{
  public static void main(String [] args) throws IOException
  {
	  FileOutputStream fo=new FileOutputStream("op.txt");
	  fo.write(98);
	  fo.write(104);
	  fo.write(80);
	  fo.close();
	  System.out.println(".....");
  }
}