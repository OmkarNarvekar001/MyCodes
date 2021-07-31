import javax.swing.*;
import java.awt.event.*;
public class Form3 extends JFrame
{
	JLabel l1, l2, l3,l4,l5;
	JCheckBox cb1,cb2,cb3;
	JButton b1;
	JComboBox cb;
	JRadioButton rb1, rb2;
	JTextField tf1, tf2;
	JTextArea area;

	Form3()
	{
		JFrame f = new JFrame("STUDENT FORM");
		
		JLabel ll = new JLabel("Name :");
		l1.setBounds(20,20,80,30);
		tf1 = new JTextField();
		tf1.setBounds(100,20,150,30);
		f.add(l1);
		f.add(tf1);
		
		JLabel l2 = new JLabel("Mobile No :");
		l2.setBounds(20,70,80,30);
		tf2 = new JTextField();
		tf2.setBounds(100,70,150,30);
		f.add(l2);
		f.add(tf2);
		
		JLabel l3 = new JLabel("Gender :");
		l3.setBounds(20,120,80,30);
		rb1 = new JRadioButton("Male");
		rb1.setBounds(100,120,60,30);
		rb2 = new JRadioButton("Female");
		rb2.setBounds(100,120,100,30);
		
		ButtonGroup bg = new ButtonGroup();
		bg.add(rb1);
		bg.add(rb2);
		f.add(rb1);
		f.add(rb2);
		f.add(l3);
		
		JLabel l4=new JLabel("Age");
		l4.setBounds(20,165,80,30);
		
		String age[]={"18","19","20","21","22"};
		JComboBox cb=new JComboBox(age);
		cb.setBounds(100,170,90,20);
		f.add(l4);
		f.add(cb);
		
		JLabel l5=new JLabel("Year");
		l4.setBounds(20,215,50,30);
		f.add(l5);
		
		cb1=new JCheckBox("First");
		cb1.setBounds(80,220,80,20);
		cb2=new JCheckBox("Second");
		cb2.setBounds(160,220,80,20);
		cb3=new JCheckBox("Third");
		cb3.setBounds(250,220,100,20);
		f.add(cb1);
		f.add(cb2);
		f.add(cb3);
		
		
		JButton b1 = new JButton("SUBMIT");
        b1.setBounds(140,280,75,20);
		f.add(b1);
		
		JTextArea area = new JTextArea();
        area.setBounds(30,320,320,100);
		f.add(area);
		
		setDefaultCloseOperation(EXIT_ON_CLOSE);
		f.setSize(400,500);
		f.setLayout(null);
		f.setVisible(true);
	}
		public static void main(String[] args)
	{
		Form3 f=new Form3();
	}
}

