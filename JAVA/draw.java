import java.awt.*;
import java.applet.*;
public class draw extends Applet
{
	/*
	<applet code="draw.class" width="300" height="300">
	</applet>
   */
public void paint(Graphics p)
{
	p.drawString("Omkar Narvekar",30,30);
	setBackground(Color.black);
	setForeground(Color.cyan);
	p.drawOval(90,30,20,20);
	p.drawLine(100,80,100,120);
	p.drawLine(100,100,80,100);
	p.drawLine(100,100,120,75);
	p.drawLine(100,120,85,135);
	p.drawLine(100,120,115,135);
}
}   

