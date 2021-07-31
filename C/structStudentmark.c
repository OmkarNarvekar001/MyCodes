#include<stdio.h>
struct student
{
    int roll;
    char name[30];
    struct marks
    {
        int p,c,m;
    }mk;
};
int main()
{
    int t1,t2;
    struct student s1,s2;
    printf("Enter roll no,name and marks of pcm for student1:");
    scanf("%d%s%d%d%d",&s1.roll,&s1.name,&s1.mk.p,&s1.mk.c,&s1.mk.m);

     printf("Enter roll no,name and marks of pcm for student2:");
    scanf("%d%s%d%d%d",&s2.roll,&s2.name,&s2.mk.p,&s2.mk.c,&s2.mk.m);

    t1=s1.mk.p+s1.mk.c+s1.mk.m;
    t2=s2.mk.p+s2.mk.c+s2.mk.m;

    if(t1>t2)
    {
        printf("\n Name of student having highest total marks=%s",s1.name);
    }
    else
    {
         printf("\n Name of student having highest total marks=%s",s2.name);
    }
    return 0;

}
