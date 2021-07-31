
#include<stdio.h>
void accept(int a[10][10],int m1,int n1);
void add(int a[10][10],int b[10][10],int c[10][10],int m1,int n1);
void subtract(int a[10][10],int b[10][10],int d[10][10],int m1,int n1);

void display(int c[10][10],int d[10][10],int m1,int n1);

int main()
{
    int  a[10][10],b[10][10],c[10][10],d[10][10],m1,n1,m2,n2;
    printf("Enter degree of matrix 1:");
    scanf("%d%d",&m1,&n1);
    printf("\n");
    printf("Enter degree of matrix 2:");
    scanf("%d%d",&m2,&n2);
    printf("\n");
    if(m1==m2 && n1==n2)
    {
        accept(a,m1,n1);
        accept(b,m2,n2);
        add(a,b,c,m1,n1);
        subtract(a,b,d,m1,n1);
        display(c,d,m1,n1);
    }
    else
    {
        printf("Addition not possible\n");
    }
    return 0;
}

 void accept(int a[10][10],int m1,int n1)
 {
     int i,j;
     printf("Enter array elements:\n");
     for(i=0;i<m1;i++)
     {
         for(j=0;j<n1;j++)

     {
         scanf("%d",&a[i][j]);
     }
     }

 }

 void add(int a[10][10],int b[10][10],int c[10][10],int m1,int n1)
 {
     int i,j;
     for(i=0;i<m1;i++)
     {
         for(j=0;j<n1;j++)
         {
             c[i][j]=a[i][j]+b[i][j];
         }
     }
 }

 void subtract(int a[10][10],int b[10][10],int d[10][10],int m1,int n1)
 {
     int i,j;
     for(i=0;i<m1;i++)
     {
         for(j=0;j<n1;j++)
         {
             d[i][j]=a[i][j]-b[i][j];
         }
     }
 }


 void display(int c[10][10],int d[10][10],int m1,int n1)
 {
     int i,j;
     printf("Addition=\n");
     for(i=0;i<m1;i++)
     {
         for(j=0;j<n1;j++)
         {
             printf("%3d",c[i][j]);
         }
         printf("\n");
     }
     printf("Subtraction=\n");
     for(i=0;i<m1;i++)
     {
         for(j=0;j<n1;j++)
         {
             printf("%3d",d[i][j]);
         }
         printf("\n");
     }

 }




