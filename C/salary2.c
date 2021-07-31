#include<stdio.h>
void main()
{
    int yos,sal,qual;
    char g;
    printf("Enter gender('M'or'F') years of service and qualification (0=G,1=PG):\n");
    scanf("%2c%2d%2d",&g,&yos,&qual);
    if (g=='m'&&yos>=10&&qual==1)
        sal=15000;
    else if ((g=='m'&&yos>=10&&qual==0)||(g=='m'&&yos<10&&qual==1))
        sal=10000;
    else if (g=='m'&&yos<10&&qual==0)
        sal=7000;
    else if (g=='f'&&yos>=10&&qual==1)
        sal=12000;
    else if (g=='f'&&yos>=10&&qual==0)
        sal=9000;
    else if (g=='f'&&yos<10&&qual==1)
        sal=10000;
    else if (g=='f'&&yos<10&&qual==0)
        sal=6000;
          printf(" Salary of employee=%2d\n",sal);


}
