#include<stdio.h>
 void mathmult(int m,int l,int n,int a[10][10],int b[10][10],int c[10][10])
 {
     int i,j,k;
     for(i=1;i<=m;i++)
      for(j=1;j<=l;j++)
     {
         c[i][j]=0;
          for(k=1;k<=l;k++)
            c[i][j]+=a[i][j]*b[i][j];
     }
 }
  void mathtrans(int m,int n,int a[10][10])
 {
     int temp,i,j;
     if(m>n)
     {
         temp=m;
         m=n;
         n=temp;
     }
     for(i=1;i<=m;i++)
         for(j=1;j<=n;j++)
     {
         temp=a[i][j];
         a[i][j]=a[j][i];
         a[j][i]=temp;

     }
 }
  void main()
 {
     int m,l,n,i,j,flag,a[10][10],b[10][10],c[10][10],d[10][10];
     printf("Enter m l n:\n");
     scanf("%d%d%d",&m,&l,&n);

     printf("Enter elements in A:\n");
     {
     for(i=1;i<=m;i++)
        for(j=1;j<=l;j++)
      {
          scanf("%d",&a[i][j]);
      }
     }

     printf("Enter elements in b:\n");
     {
     for(i=1;i<=l;i++)
        for(j=1;j<=n;j++)
      {
          scanf("%d",&b[i][j]);
      }
     }
    flag=1;
    mathmult(m,l,n,a,b,c);
    mathtrans(m,n,c);
    mathtrans(l,n,b);
    mathtrans(m,l,a);
    mathmult(n,l,m,b,a,d);
     {
         for(i=1;i<=n;i++)
            for(j=1;j<=m;j++)
         {
             if ((c[i][j]!=a[i][j]))
             {
                 flag=0;
                 break;
             }
         }
     }
     if(flag)
        printf("Identity true");
     else
        printf("Identity false");
 }












