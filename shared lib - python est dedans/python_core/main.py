#imports
import ctypes as ct 
from ctypes import *
from pandas import *
import pandas as pd
import csv
import os


#----------------------------------------------- DEF FUNCTIONS ---------------------------------------------------------- 

def creerhoraires():
    if int(input("Voulez vous utiliser le mode par défaut? Répondez 0 pour Non, 1 pour Oui\n"))==1:
      #Le mode par défaut contient 4 mois, 2 de 30 jours et 2 de 31 jours.
      hor=1464*[0]  #4*30.5*12
      profil=[hor,31,30,31,30]

      print("\nvous avez 1464 créneaux à votre disposition")

    else:
      m1=int(input("Entrer durée du premier mois\n"))
      m2=int(input("Entrer durée du second mois\n"))
      m3=int(input("Entrer durée du troisième mois\n"))
      m4=int(input("Entrer durée du quatrième mois\n"))

      hor=(m1+m2+m3+m4)*12*[0]
      profil=[hor,m1,m2,m3,m4]

      print("\n","vous avez ",len(hor)," créneaux à votre disposition")


    return profil
  

def creerportes(nbportes):

    portes=[]*nbportes

    if (int(input("les portes ont-elles une taille spécifique? Si oui, entrer 1, 0 sinon\n"))==1):
      

      for i in range(nbportes):

        tailleporte=int(input("entrer la taille de la porte: 0 pour petite, 1 pour moyenne, 2 pour grande\n"))
        
        if tailleporte==0:
          portes.append({"numero":i+1,"taille":0})
        elif tailleporte==1:
          portes.append({"numero":i+1,"taille":1})
        elif tailleporte==2:
          portes.append({"numero":i+1,"taille":2})
      
      print("\nBilan des portes:\n")
      print(len(portes))

      for i in range(len(portes)):
        
        print("\n","Porte ",portes[i]["numero"],", de ", portes[i]["taille"]," taille")

    else:
      print("vous avez",len(portes),"portes de taille standard dans votre aéroport")
    
    return portes
  

def creercompagnies():
  n=int(input("combien de compagnies?"))

  compagnies=[]

  for i in range(n):

    #NOM

    nom=str(input("Entrer le nom de la compagnie"))

    #MINIMUM DE VOLS

    min=int(input("combien de vols minimum par jour?"))

    #FLOTTE

    nbmodeles=int(input("Combien de modèles d'avions différents?"))
    flotte=[]

    for j in range(nbmodeles):

      modele=str(input("entrer le nom du modele"))

      nombre=int(input("Combien d'avions de ce modèle sont dispo pour notre aéroport?"))

      capaMin=int(input("Combien de passagers au minimum dans cet avion?"))

      capaMax=int(input("Combien de passagers au maximum dans cet avion?"))


      flotte.append({"modele":modele,"nombre":nombre,"capaMin":capaMin,"capaMax":capaMax})

    compagnies.append({"nom":nom,"min":min,"flotte":flotte})
  
  print("Fin de l'enregistrement! Voici les informations sur les compagnies:\n\n")

  for i in range(len(compagnies)):

    print("Compagnie n°", i+1, ": ",compagnies[i]["nom"])

    for j in range(len(compagnies[i]["flotte"])):
      print("\n   Modèle 1:",compagnies[i]["flotte"][j]["modele"])
      print("   ",compagnies[i]["flotte"][j]["nombre"]," appareils dispos\n")
  
  return compagnies


def recupcompagnies():  #FONCTION QUI VA CHERCHER LES OBJETS COMPAGNIES (nom - min - flotte) DANS UN FICHIER OU UN CSV
    compagnies=[]
    # partie excel 

    # name = input(str("entrer nom du fichier csv contenant les compagnies : "))
    
    xls = pd.ExcelFile('testcompagnie.xlsx')
    df = pd.read_excel(xls, 'Compagnies')
    
    nb = (df.ndim)+1      #nombre de compagnies
    
    cd = df.to_dict('records') #cd = dictionnaire des compagnies
    
    
    for i in range(1, nb+1):
      
      nom="Flotte"+str(i)
      df = pd.read_excel(xls, nom)
      
      flotted = df.to_dict('records') #flotted = dictionnaire des flottes 
      
      dict0={"flotte":flotted}
        
      cd[i-1].update(dict0) #on combine la valeur de dict0 et de cd au niveau de leur clé similaire
      
    compagnies.append(cd)
    
    return cd


def data_to_excel(data): #pour envoyer un dictionnaire ou une liste vers excel et l'afficher 
  df = pd.DataFrame(data)
  df.to_excel('excel.xlsx', index = False)
  print(df)


def creerrequetes(compagnies):

  requetes=[]
  for i in range(len(compagnies)):
    
    nbrequetes=int(input("Combien de requetes de la part de la compagnie",compagnies[i]["nom"]))

    for j in range(nbrequetes):
      num=str(input("Entrer le nom du vol (2 lettre 4 chiffres)"))
      appareil=str(input("Entrer le nom de l'appareil qui effectuera ce trajet"))
      dep=str(input("Entrer l'aéroport de Départ"))
      arr=str(input("Entrer l'aéroport d'Arrivée"))
      freq=str(input("Entrer la fréquence: journaliere(1), hebdomadaire(2), mensuelle(3)"))

      requetes.append({"compagnie":compagnies[i]["nom"],"num":num,"appareil":appareil,"depart":dep,"arrivee":arr,"freq":freq})

  return requetes


def recuprequetes(): #FONCTION QUI VA CHERCHER LES OBJETS REQUETES DANS UN FICHIER OU UN CSV
  
  requetes=[]

  xls = pd.ExcelFile('testrequetes2.xlsx')
  df = pd.read_excel(xls)
  
  requetescompagnie = df.to_dict('records') # = dictionnaire des requetes 
  
  return requetescompagnie


def trackcompagnie(compagnie,listevols, hor): #examine pour chaque jour le nombre de vols de cette compagnie

  c=[0]*(len(hor)//12)
  listevols = []

  for i in listevols:
    if i["compagnie"]==compagnie:
      c[i["date"]//12]+=1
      
      print(c)
  return c










#------------------------------------------------ MAIN ------------------------------------------------------------ 


if __name__ == '__main__':
  c_lib = ct.CDLL('test5\cmake-build-debug\libtest5.dll')


  # on teste si le ctype marche bien avec un appel vers the dummy function
  a=c_int(3)
  b=c_int(6)
  print(c_lib.calcul(a, b))

  aero="CDG"

    #INITIALISATION DU MODELE HORAIRE

  format=creerhoraires() 
  hor=format[0]#Les horaires sont une liste de N créneaux. L'entier stocké dans chaque créneau représente le nombre d'avions présents à l'aéroport sur ce créneau.
  mois=format[1:5]#Longueur de chaque mois

  
    #INITIALISATION DU NOMBRE ET DE LA TAILLE DES PORTES

  nbportes=int(input("Combien de portes dispos dans l'aéroport?\n"))

  portes=creerportes(nbportes)

    #INITIALISATION DES COMPAGNIES

  choix=int(input("\nComment voulez-vous entrer les compagnies?\nPour les entrer manuellement, taper 0\nPour les extraire depuis un fichier, taper 1"))

    #Si utilisateur:
  if choix==0:
    compagnies=creercompagnies()


    #Si fichier
  if choix==1:
    compagnies=recupcompagnies()
    print(compagnies)

    
    
    #INITIALISATION DES REQUETES DE VOL
  choix=int(input("\nComment voulez-vous entrer les requetes?\nPour les entrer manuellement, taper 0\nPour les extraire depuis un fichier, taper 1"))
    
    #Si utilisateur:
  if choix==0:
    requetes=creerrequetes(compagnies)


    #Si fichier
  if choix==1:
    requetes=recuprequetes()
    print(requetes)




    #INITIALISATION DE LISTEVOLS: LISTEVOLS NOUS DONNE LA LISTE COMPLETE DES VOLS A AFFECTER AVEC TOUTES LES INFOS SAUF LA DATE, L'HEURE ET LA PORTE



    #LANCEMENT DE "PLANIFICATION"
    
  xls = pd.ExcelFile('testcompagnie.xlsx')
  df = pd.read_excel(xls, 'Compagnies')
  nb_compagnies = (df.ndim)+1   
  
  vols=[]

  for requete in requetes:
    c=trackcompagnie(requete["compagnie"], vols, hor)
    

  print(c)
  print(hor)
  print(mois)
  print(requete["freq"])
  print(len(requete["freq"]))
  


  dates=[]
  
  dates = c_lib.planification((c_int*len(c))(*c), (c_int*len(hor))(*hor), (c_int*len(mois))(*mois), c_int(len(portes)), (c_char*len(requete["freq"]))(*requete["freq"]))
  
  
 
  for i in range(len(dates)):
    vols.append({"compagnie":requete["compagnie"],"num":requete["num"],"appareil":requete["appareil"],"depart":requete["depart"],"arrivee":requete["arrivee"],"freq":requete["freq"],"date":dates[i],"porte":0}) #On garde la frequence au cas où on doit replanifier
   
    
    
   #LANCEMENT DE "REPLANIFICATION"



  #LANCEMENT DE "AFFECTATION"
    
  dispoportes=len(hor)*[nbportes*[0]] #Liste de l'occupation des portes. Se lit ainsi: portes[date][porte] donne le statut d'occupation de la porte à ce moment (0 pour libre, 1 pour occupé)
  
  tailleportes=[]

  for i in range(len(portes)): 
    tailleportes.append(portes["taille"])

  for v in vols:
    #ON VEUT CAPAMAX (compagnie->flotte->capaMax)
    for i in compagnies:
      if v["compagnie"]==i["nom"]:
        for j in len(i["flotte"]):
          if i["flotte"]["modele"]==v["modele"]:
            capaMax=i["flotte"]["capaMax"]

    v["porte"]=c_lib.affectation(ct.c_int(nbportes),  ct.c_int*len(dispoportes[v["date"]])(*dispoportes[v["date"]]),  ct.c_int*len(tailleportes)(*tailleportes), ct.c_int(capaMax))
    
    #-1 est renvoyé si pas de portes dispo

    # if v["porte"]==-1:
    #   reaffect()
    
    if v["porte"]!=-1:
      dispoportes[v["date"]][v["porte"]]=1 #La porte est désormais occupée

  #CONVERTIR NOS HORAIRES EN DATE (HEURE JOUR SEMAINE MOIS)
  
  datesoutput=[] #datesoutput de la forme datesoutput[mois][semaine][jour][heure]=dates[créneau]
  heure=0
  for i in range(len(mois)):
    datesoutput.append([])
    for j in range(len((mois[i]//7)+1)):
      datesoutput[i].append([])
      for k in range(len(hor//12)):
        datesoutput[i][j].append([])
        for l in range(12):
          datesoutput[i][j][k].append(dates[heure])
          heure+=1

  

#RENVOYER TOUT "VOLS" VERS UN CSV
with open('listevols.csv', 'w') as fichiervols:
    writer = csv.DictWriter(fichiervols, fieldnames = vols[0].keys)
    writer.writeheader()
    writer.writerows()

