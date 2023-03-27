#ifndef TEST5_LIBRARY_H
#define TEST5_LIBRARY_H

int calcul(int a, int b);


/**
 * @brief la fonction planification permet d'affecter une requete vol vers un créneau horaire en fonction du détail de la requete 
 * 
 * @param c 
 * @param hor 
 * @param mois 
 * @param nbportes = nombre de portes dans l'aéroport
 * @param freq = fréquence des requetes de vols (mensuel, hebdomadaire, journalier)
 * @return int* dates = liste de dates qu'on va renvoyer
 */
int* planification(int* c, int* hor ,int* mois ,int nbportes, char*freq);

int affectation(int nbportes,int* statutportes,int* tailleportes,int capaMax);


#endif //TEST5_LIBRARY_H
