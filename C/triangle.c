#include<stdio.h>
void main()
{
    float s1,s2,s3,sum,big;
    printf("Enter 3 sides of triangle\n");
    scanf("%f%f%f",&s1,&s2,&s3);
    if (s1>s2)
    {
       if (s1>s3)
        {
        sum=s2+s3;
        big=s1;
        }
        else
        {
            sum=s1+s2;
            big=s3;
        }
    }
    else
    {
        if(s2>s3)
        {
            sum=s1+s3;
            big=s2;
        }
        else
        {
            sum=s1+s2;
            big=s3;
        }
    }
    if(sum>big)
        printf("Valid triangle\n");
    else
        printf("Invalid triangle\n");

    if(sum>big)
    {
        if((s1==s2)&&(s2==s3))
            {
                printf("Equilateral triangle\n");
            }
       if((s1==s2)||(s1==s3)||(s2==s3))
            {
                 printf("Isosceles triangle\n");
            }
        if ( (s1!=s2) && (s2!=s3) && (s3!=s1))
            {
                printf("Scalene triangle\n");
            }
    }
}
