#include<stdio.h>
void main()
{

    int i,k,n;
    printf("Enter n:");
    scanf("%d",&n);
     for(k=1;k<=n;k++)
     {
         printf("\n");
         for(i=1;i<=40-4*k;i++)
         printf(" ");
         for(i=k;i>=1;i--)
         printf("%4d",i);
         for(i=2;i<=k;i++)
         printf("%4d",i);
     }
for(k=n-1;k>0;k--)
     {
         printf("\n");
         for(i=1;i<=40-4*k;i++)
            printf(" ");
         for(i=k;i>=1;i--)
            printf("%4d",i);
         for(i=2;i<=k;i++)
            printf("%4d",i);
     }
}
