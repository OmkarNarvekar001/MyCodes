import java.util.Vector;
public class Vectorop
{ 
    public static void main(String args[]) 
    { 
  
        
        Vector<Integer> vc =new Vector<Integer>();
       
        vc.add(1); 
        vc.add(12); 
        vc.add(23); 
        vc.add(10); 
        vc.add(20); 
        vc.add(30); 
        vc.add(40); 
        vc.add(50); 
        vc.add(60); 
        vc.add(70); 
       
        System.out.println("The vector is: " + vc);

        System.out.println("Size of vector is :"+vc.size());		
     
		
		vc.add(4,32);
		vc.add(8,44);
		vc.add(9,78);
		
		System.out.println("The vector is: " + vc); 
		
		System.out.println("Size of vector is :"+vc.size());
		
		System.out.println("The element at index 5: "+vc.get(5)); 
		System.out.println("The element at index 8: "+vc.get(8)); 
		System.out.println("The element at index 10: "+vc.get(10)); 
		
		System.out.println("Element at 1st position: "+vc.firstElement());
		System.out.println("Element at last position: "+vc.lastElement());
        
		System.out.println("Is vector Empty ?: "+vc.isEmpty());
		
		System.out.println("Removing 12: "+vc.remove((Integer)12));
		System.out.println("Removing 20: "+vc.remove((Integer)20));
		System.out.println("Removing 32: "+vc.remove((Integer)32));
		System.out.println("Removing 40: "+vc.remove((Integer)40));
		System.out.println("Removing 60: "+vc.remove((Integer)60));
		
		System.out.println("The vector is: " + vc); 
		System.out.println("The size of the Vector is: "+vc.size());
    } 
} 