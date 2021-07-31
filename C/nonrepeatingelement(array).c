#include<stdio.h>
void main()
{
    int a[30],i,n,j;
    printf("Enter the size of array:\n");
    scanf("%d",&n);
    printf("Enter the elements:\n");
     {
         for(i=0;i<n;i++)
         scanf("%d",&a[i]);
     }
     {
        for(i=0;i<n;i++)
        {
            for(j=0;j<n;j++)
            {
                if(i!=j && a[i]==a[j])
                    break;
            }
            {
                if(j==n)
                    printf("non repeating elements in array:%2d\n",a[i]);
            }

  }
}
