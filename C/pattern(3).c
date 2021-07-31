#include<stdio.h>
void main()
{
    int i=0,j,k,n,sum;
    printf("Enter n:");
    scanf("%d",&n);
     for (k=1;k<=n;k++)
     {
         sum=0;
         printf("\n");
         for(j=1;j<=k;j++)
         {
             printf("%4d",++i);
             sum=sum+i;
         }
         for(j=1;j<=40-4*k;j++)
           printf(" ");
         printf("%20d",sum);
     }
}
