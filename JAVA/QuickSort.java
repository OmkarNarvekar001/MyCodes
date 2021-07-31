import java.util.*;
class QuickSort 
{ 
	int partition(int arr[], int low, int high) 
	{ 
		int pivot = arr[high]; 
		int i = (low-1); 
		for (int j=low; j<high; j++) 
		{  
			if (arr[j] < pivot) 
			{ 
				i++; 
				int temp = arr[i]; 
				arr[i] = arr[j]; 
				arr[j] = temp; 
			} 
		} 
		int temp = arr[i+1]; 
		arr[i+1] = arr[high]; 
		arr[high] = temp; 

		return i+1; 
	} 
	void sort(int arr[], int low, int high) 
	{ 
		if (low < high) 
		{ 
			int pi = partition(arr, low, high); 
			sort(arr, low, pi-1); 
			sort(arr, pi+1, high); 
		} 
	} 
	public static void main(String args[]) 
	{ 
		Scanner sc=new Scanner(System.in);
	System.out.println("ENTER Number Elements of ARRAY: ");
    int m=sc.nextInt();
	int i,j;
int arr[]=new int[m];
	System.out.println("ENTER ELEMENTS OF ARRAY : ");
    for(i=0;i<m;i++)
		  { arr[i]=sc.nextInt();}
		int n = arr.length; 
		QuickSort ob = new QuickSort(); 
		ob.sort(arr, 0, n-1); 
		System.out.println(" SORTED ARRAY ");
          for(i=0;i<m;i++)
		  {System.out.print("  "+(arr[i]));
	} 
}
} 
