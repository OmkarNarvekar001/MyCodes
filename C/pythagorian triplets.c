#include<stdio.h>
#include<math.h>
void main()
{
    int i,j,k,t,count;
    count=0;
    for(i=1;i<=20;i++)
    {
        for(j=i;j<=20;j++)
        {
            t=i*i+j*j;
            k=sqrt(t);
            if(k*k==t)
            {
                printf("\n%4d%4d%4d",i,j,k);
                count++;
            }
            if (count==20)
            break;
        }
    }
}
