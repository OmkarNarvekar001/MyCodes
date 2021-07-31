#include<stdio.h>
#include<string.h>
void main()
{
    char guntype[30],AR,SMG,SNIPER,LMG,MARKSMAN,PISTOL,SHOTGUN,CROSSBOW;
    char ammo[30],black,grey,green,brown,blue,red,yellow;
    char guns[30],M416,M16A4,SCARL,M249,MINI14,AUG,AKM,BERRYL,GROZA,M24,KAR98,MK14,SKS,SLR,MK47MUTANT,P18C,P92,VECTOR,MICROUZI,PPBIZON,VSS,SKORPION,P1911,TOMMYGUN,UMP45,S686,S12K,S1897,AWM;
    printf("Welcome to Training ground\n");
    printf("Which gun would you like to pick:\n1.AR\n2.SMG\n3.SNIPER\n4.LMG\n5.MARKSMAN\n6.PISTOL\n7.SHOTGUN\n8.CROSSBOW\n\n\n");
    gets(guntype);
    printf("Your choice:%s\n",guntype);
    printf("Enter ammo color\n");
    gets(ammo);
    printf("Selected ammo:%s\n",ammo);
    puts(ammo);
    if(blue)
        printf("Guns are\n1.P1911\n2.TOMMYGUN\n3.UMP45\n");
    else if(red)
        printf("Guns are\n1.S686\n2.S12K\n3.S1897\n");
    else if(yellow)
        printf("Guns are\n1.P18C\n2.P92\n3.VECTOR\n4.MICROUZI\n5.PPBIZON\n6.VSS\n7.SKORPION\n");

    else if(black)
        printf("Gun is AWM\n");
   else if(grey)
        printf("Gun is CROSSBOW\n");

}
