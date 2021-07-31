#include<stdio.h>
void main()
{
    int n,r,sum,temp;
    sum=0;
    printf("Enter n:");
    scanf("%d",&n);
    temp=n;
      while(n>0)
      {
          r=n%10;
          sum=sum*10+r;
          n=n/10;
      }
     n=temp;
     if(n==sum)
        printf("%d is palindrome",sum);
     else
     printf("%d is not palindrome",sum);
}
