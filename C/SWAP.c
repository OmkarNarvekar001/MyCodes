#include<stdio.h>
void main()
{
    int a,b,temp;
    printf("\n ENTER NUMBERS a and b");
    scanf("%d%d",&a,&b);
     temp=a;
     a=b;
     b=temp;
    printf("\n Swapped numbers are a=%d, b=%d",a,b);

   }
