#include<stdio.h>
void main()
{
    int i,j;
    for (i=1;i<=5;i++)
    {
        printf("\n");
        for (j=1;j<=5;j++)
        printf(" %7d %4d",i,j);
    }
}
