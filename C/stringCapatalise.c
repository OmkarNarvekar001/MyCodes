#include<stdio.h>
#include<ctype.h>
#include<string.h>
int main()
{
    char  a[50];
    int i;
    printf("Enter string:");
    gets(a);
    for(i=0;i<strlen(a);i++)
    {
        a[i]=tolower(a[i]);
    }
    a[0]=toupper(a[0]);
    for(i=0;i<strlen(a);i++)
        if(a[i]==' ')
    {
        a[i+1]=toupper(a[i+1]);
    }
    printf("String=%s",a);
    return 0;
}
