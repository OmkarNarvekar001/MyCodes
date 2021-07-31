#include<stdio.h>
void main()
{
    int a[20],i,n,j,temp;
    printf("Enter the size array:\n");
    scanf("%d",&n);
     printf("Enter elements of array:\n");
    {
    for(i=0;i<n;i++)
    scanf("%d",&a[i]);
    }
    i=0;
    j=n-1;
    while(i<j)
    {
        temp=a[i];
        a[i]=a[j];
        a[j]=temp;
        i++;
        j--;
    }
    printf("Reverse of array:\n");
    {
        for(i=0;i<n;i++)
        printf("%3d\n",a[i]);
    }
}



