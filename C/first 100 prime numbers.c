#include<stdio.h>
#include<math.h>
 void main()
{
    int k,dv,count=0,no;
     for (no=1;count<100;no++)
     {
         dv=2;
         k=sqrt(no);
      while((no%dv!=0)&&(dv<=k))
          ++dv;
      if (dv>k)
      {
          printf("%4d",no);
          ++count;
         if (count%10==0)
            printf("\n");
      }
     }
}
