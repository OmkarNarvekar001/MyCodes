#include<stdio.h>
void main()
{
    int m,yr;
    printf("Enter month number:\n");
    scanf("%d",&m);
    if (m>12)
    printf("Invalid\nEnter numbers between 1-12");
    if (m==1||m==3||m==5||m==7||m==8||m==10||m==12)
    {
        printf("Month %d has 31 days\n",m);
    }
    else if (m==4||m==6||m==9||m==11)
    {
        printf("Month number %d has 30 days\n",m);
    }
     else if(m==2)
     {
         printf("Enter year:\n");
         scanf("%d",&yr);
         if ((yr%400==0)||(yr%4==0)&&(yr%100!=0))
         {
             printf("Month number %d has 28 days\n",m);
         }
         else
         {
             printf("Month number %d has 29 days\n",m);
         }
     }

}