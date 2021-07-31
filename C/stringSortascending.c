#include<stdio.h>
#include<string.h>
#include<ctype.h>
int main()
{
    char s[27],temp;
    int i,j;
    printf("Enter string:");
    gets(s);
    for(i=0;i<strlen(s);i++)
    {
        s[i]=toupper(s[i]);
    }
    for(i=1;i<strlen(s);i++)
    {
        for(j=0;j<strlen(s)-i;j++)
        {
            if(s[j]>s[j+1])
            {
            temp=s[j];
            s[j]=s[j+1];
            s[j+1]=temp;
            }
        }

    }
    printf("\n Sorted string=%s",s);
    return 0;

}
