#include<stdio.h>
struct employee
{
    int id,salary;
    char name[20];
};
int main()
{
    int i,j,n;
    struct employee e[20];
    printf("Enter the no of employees:");
    scanf("%d",&n);
    for(i=0;i<n;i++)
    {
        printf("\nEnter ID, NAME, SALARY of Employee:");
        scanf("%d%s%d",&e[i].id,&e[i].name,&e[i].salary);
    }
    for(i=0;i<n;i++)
    {
        if(e[i].salary>20000)
        {
            printf("\n Name=%s",e[i].name);
        }
    }


    return 0;
}
