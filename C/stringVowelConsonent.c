#include<stdio.h>
#include<ctype.h>
#include<string.h>
int main()
{
   char s1[20];
   int c1=0,c2=0,c3=0,i;
   printf("Enter the string:");
   gets(s1);
   for(i=0;i<strlen(s1);i++)
   {
       s1[i]=toupper(s1[i]);
   }
   for(i=0;i<strlen(s1);i++)
    {
        if(s1[i]=='A'||s1[i]=='E'||s1[i]=='I'||s1[i]=='O'||s1[i]=='U')
        {
            c1++;
        }
        else if(isalpha(s1[i]))
        {
            c2++;
        }
        else
        {
            c3++;
        }
    }
    printf("\nVowels=%d",c1);
    printf("\nConsonents=%d",c2);
    printf("\nOther=%d",c3);
   return 0;
}
