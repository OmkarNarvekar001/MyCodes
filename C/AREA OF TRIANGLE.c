#include<stdio.h>
#include<math.h>
void main()
{
    int a,b,c;
    float s,area;
 printf("\n ENTER VALUES OF a,b,c");
 scanf("%d%d%d",&a,&b,&c);
 s=(a+b+c)/2;
 printf("\n s=%f",s);
 area=sqrt(s*(s-a)*(s-b)*(s-c));
 printf("\n area=%f",area);
}
