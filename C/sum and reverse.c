#include<stdio.h>
#include<conio.h>
void main()
{
  int n,sum,r,temp;
  sum=0;
  printf("Enter n:");
  scanf("%d",&n);
  temp=n;

       while(n>0)
    {
        r=n%10;
        sum=sum+r;
        n=n/10;
    }
   printf("\n Sum of digits=%d",sum);
   n=temp;
   sum=0;
      while(n>0)
      {
          r=n%10;
          sum=sum*10+r;
          n=n/10;
      }
   printf("\n Reverse of number is %d",sum);

}
