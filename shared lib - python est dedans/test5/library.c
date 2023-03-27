#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int calcul(int a, int b){
    return a+b;
}


int* planification(int* c, int* hor ,int* mois ,int nbportes, char*freq){
    int k,d;
    int* dates; //LISTE DE DATES QU'ON VA RENVOYER

    d=0; //d est le nombre de dates

    // affectation vol mensuel
    if (freq[0]=='m' || freq[0]=='2')
    {
        dates=malloc(4*sizeof(int));

        for (int i=0;i<4;i++) //Premier mois, second mois, etc...
        {

            k=0;//temoin d'affectation

            int m=0;

            for (int x=0; x<i;x++)
            {
                m+=mois[x]*12; //Combien d'horaires sont passés avant d'arriver à ce mois ?
            }

            for(int j=m ; j<m+(mois[i]*12) ; j++) //j est l'indicateur de l'horaire
            {

                if (hor[j]<nbportes && k==0 && c[j]<4)
                {

                    dates[d]=j;
                    d++;

                    k=1; //Si la date est valide, k=1, on sort de la boucle. Sinon k=0
                    hor[j]++;
                    c[j]++;
                }

            }
            if (k==0)
            {
                dates[d]=-1; //date=-1 -> montre l'échec à affecter la date. Par la suite, les vols avec la date -1 seront éligibles pour une replanification
            }
        }
    }
    if (freq[0]=='h' || freq[0]=='1')
    {

        int nbsem=((mois[0]+mois[1]+mois[2]+mois[3]))/7; //nombre de semaines. On part du principe que les 4 mois commencent par un lundi.
        dates=malloc(nbsem*sizeof(int));
        for(int i=0;i<nbsem+1;i++) // On parcourt les semaines
        {
            k=0;//t�moin d'affectation

            int s=0; //Combien d'horaires sont passés avant d'arriver à cette semaines

            for (int x=0; x<i;x++)
            {
                s+=7*12;
            }

            for(int j=s ; j<s+7*12 ; j++) //j est l'indicateur de l'horaire
            {

                if (hor[j]<nbportes && k==0 && c[j]<=4)
                {
                    dates[d]=j;
                    d++;

                    k=1; //Si la date est valide, k=1, on sort de la boucle. Sinon k=0
                    hor[j]++;
                    c[j]++;
                }

            }

            if (k==0)
            {
                dates[d]=-1;
            }
        }


    }
    if (freq[0]=='j' || freq[0]=='0')
    {
        int nbjours=mois[0]+mois[1]+mois[2]+mois[3]; //cb de jours
        dates=calloc(nbjours,sizeof(int));
        int jour;
        for (jour=0;jour<nbjours;jour++) //on parcourt les jours
        {
            k=0; //temoin d'affectation
            for (int j=12*(jour); j<(jour+1)*12; j++) //on scanne les horaires
            {
                if (hor[j]<nbportes && k==0 && c[j]<4)
                {

                    dates[d]=j;
                    d++;

                    k=1; //Si la date est valide, k=1, on sort de la boucle. Sinon k=0
                    hor[j]++;
                    c[j]++;

                }
            }
            if (k==0)
            {
                dates[d]=-1;
            }
        }
    }
    return dates;//ON RETURN UNE LISTE DE DATES
}

int affectation(int nbportes, int* statutportes, int* tailleportes, int capaMax)
{
    int i;
    for (i=0;i<nbportes;i++) //On vérifie qu'il n'y ait pas une porte déjà libre
    {
        if (statutportes[i]==0 && tailleportes[i]>=capaMax)
        {
            return i+1;
        }
    }
    return -1;
}

