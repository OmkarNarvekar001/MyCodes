import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JTextField;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import java.awt.FlowLayout;

public class FirstGUI
{
	public static void main(String [] args)
	{
		obj abc=new obj();
	}
} 

class obj extends JFrame implements ActionListener
{
	JTextField t1,t2,l;
	JButton b;
	obj()
	{
		t1=new JTextField(20);
		t2=new JTextField(20);
		b=new JButton("Proceed");
		l=new JTextField(20);
		add(t1);
		add(t2);
		add(b);
		add(l);
		this.setTitle("Addition");
		l.setLayout(new FlowLayout());
        b.addActionListener(this);
		setLayout(new FlowLayout());
		setSize(600,600);
		setVisible(true);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		l.setSize(100,200);
	}
	public void actionPerformed(ActionEvent ae)
	{
		int n1=Integer.parseInt(t1.getText());
		int n2=Integer.parseInt(t2.getText());
		int val=n1+n2;
		l.setText(val+"");
	}
}