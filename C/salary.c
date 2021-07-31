#include<stdio.h>
#include<math.h>
void main()
{
    float da,hra,grpay,bs;
    printf("ENTER BASIC SALARY OF RAMESH\n");
    scanf("%f",&bs);
    da=0.4*bs;
    hra=0.2*bs;
    grpay=bs+da+hra;
    printf("BASIC SALARY OF RAMESH=%f\n",bs);
    printf("DEARNESS ALLOWNESS OF RAMESH=%f\n",da);
    printf("HOUSED RENT OF RAMESH=%f\n",hra);
    printf("GROSSS PAY OF RAMESH=%f\n",grpay);
}
