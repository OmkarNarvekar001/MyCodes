#include<stdio.h>
#include<string.h>

void reverse(char a[20])
{
    int i,j;
    char temp;
    i=0;
    j=strlen(a)-1;
    while(i<j)
    {
        temp=a[i];
        a[i]=a[j];
        a[j]=temp;
    }
    i++;
    j--;

}

int main()
{
    char a[20],b[20];
    printf("Enter string:");
    gets(a);

    reverse(a);
    if(strcmp(b,a)==0)
    {
        printf("Pallindrome");
    }
    else
        {
            printf("Not Pallindrome");
        }
        return 0;
}
