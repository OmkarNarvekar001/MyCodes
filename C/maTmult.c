#include<stdio.h>

void accept(int x[10][10],int m1,int n1)
{
    int i,j;
    printf("Enter array elements:");
    for(i=0;i<m1;i++)
    {
        for(j=0;j<n1;j++)
        {
            scanf("%d",&x[i][j]);
        }
    }
}

void mult(int a[10][10],int b[10][10],int c[10][10],int m1, int n1,int m2, int n2)
{
    int i,j,k;
    for(i=0;i<m1;i++)
    {
        for(j=0;j<n2;j++)
        {
            c[i][j]=0;
            {
                for(k=0;k<n1;k++)
                {
                    c[i][j]+=a[i][j]*b[i][j];
                }
            }
        }
    }
}


void display(int c[10][10],int m1,int n2)
{
    int i,j;
    printf("Multiplication=\n");
    for(i=0;i<m1;i++)
    {
        for(j=0;j<n2;j++)
        {
            printf("%3d",c[i][j]);
        }
        printf("\n");
    }
}
int main()
{
    int a[10][10],b[10][10],c[10][10],m1,n1,m2,n2;
    printf("Enter  degree of matrix 1:");
    scanf("%d%d",&m1,&n1);
    printf("\n");
    printf("Enter degree of matrix 2:");
    scanf("%d%d",&m2,&n2);
    printf("\n");
    {
        if(n1==m2)
        {
            accept(a,m1,n1);
            accept(b,m2,n2);
            mult(a,b,c,m1,n1,m2,n2);
            display(c,m1,n2);
        }
        else
        {
            printf("Multiplication impossible");
        }
    }
    return 0;

}
