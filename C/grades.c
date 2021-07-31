#include<stdio.h>
void main()
{
    float perc;
    printf("Enter percentage:\n");
    scanf("%f",&perc);
    if(perc>=70)
       printf("Grade=O\n");
    else if (perc>=60 && perc<70)
        printf("Grade=A\n");
    else if (perc>=50 && perc<60)
        printf("Grade=B\n");
    else if (perc>=40 && perc<50)
        printf("Grade=C\n");
    else
        printf("Grade =FAIL\n");
}
