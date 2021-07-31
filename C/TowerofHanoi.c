#include<stdio.h>
#include<stdlib.h>

void hanoi(int n,char from,char to,char temp)
{
    if(n==1)
    {
        printf("\n Move disk 1 from rod %c to rod %c",from,to);
    }
  
    else
    {
    hanoi (n-1,from,temp,to);
    printf("\n Move disk %d from rod %c to rod %c",n,from,to);
    hanoi (n-1,temp,to,from);
    }
    
}

void main()
{
    int n ;
    printf("\nEnter the number of disc:");
    scanf("%d",&n);
    hanoi(n,'a','b','c');
}