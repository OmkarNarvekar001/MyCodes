import java.io.*;

public class DataTrans 
{
	public static void main(String[] args) throws IOException
	{
		FileInputStream fin=new FileInputStream("input.txt");
		FileOutputStream fo=new FileOutputStream("op.txt");
		
		int i;
		
		while((i=fin.read())!=-1)
		{
		   fo.write(i);
		   System.out.print(i);
		   System.out.print((char)i);
		}
	}
}