#include<stdio.h>
#include<math.h>
void main()
{
    int quantity,discount=0;
    float rate,total;
    printf("\n Enter quantity and rate");
    scanf("%d%f",&quantity,&rate);
     if(quantity>1000)
        discount=10;
     total=(rate*quantity)-(rate*quantity*discount/100);
    printf("\n Total expense=Rs%f",total);
}
