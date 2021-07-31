#include<stdio.h>
#include<ctype.h>
#include<string.h>
int main()
{
    char s[20][20],temp[20];
    int n,i,j;
    printf("Enter no of string:");
    scanf("%d",&n);
    for(i=1;i<n;i++)
    {
        printf("Enter name:");
        gets(s[i]);
    }
    for(i=1;i<n;i++)
    {
        for(j=0;j<n-1;j++)
        {
            if(strcmp(s[j],s[j+1])>0)
            {
                strcpy(temp,s[j]);
                strcpy(s[j],s[j+1]);
                strcpy(s[j+1],temp);
            }
        }
    }
    printf("\nSorted list:");
    for(i=0;i<n;i++)
    {
        printf("\n%s",s[i]);
    }
    return 0;
}
