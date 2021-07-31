#include<stdio.h>

void main()
{
    float u,b;
    printf("Enter units\n");
    scanf("%f",&u);
     if(u<=200)
        b=0.5*u;
     else if(u<=400)
        b=100+0.65*(u-200);
     else if(u<=600)
        b=230+0.85*(u-400);
     else
        b=390+1*(u-600);
    printf("Bill=%f\n",b);

}
