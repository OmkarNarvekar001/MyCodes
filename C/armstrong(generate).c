#include<stdio.h>
#include<math.h>
void main()
{
    int n,temp,r,c,sum;
    printf("Armstrong numbers between 0 to 500 are...\n");

     for(n=1;n<=500;n++)
     {
         temp=n;
         sum=0;
         while(n>0)
         {
             r=n%10;
             c=r*r*r;
             sum=sum+c;
             n=n/10;
         }
         n=temp;
         if(n==sum)
            printf("%d\n",n);

     }

}
