from nltk.stem import WordNetLemmatizer
import numpy as np
import re
import nltk
from sklearn.datasets import load_files
nltk.download('stopwords')
import pickle
from nltk.corpus import stopwords

#bdd d'insultes doit être importée
file1 = open('bdd_insulte.txt', 'r') 
Lines_bdd = file1.readlines()
file2 = open('bdd_mot_court.txt', 'r') 
Lines_mot_court = file2.readlines() 
def normalisation_txt(txt):
    txt.lower()

def transfoliste(mot): #prend un mot et le transforme en liste de str
    a=mot
    M=[]
    for i in range(len(a)):
        M.append(a[i])
    return(M)

def supprdoublon(mot):
    a=mot
    M=[]
    for i in range(len(a)):
        if i==0:
            M.append(a[i])
        else:
            if a[i]!=M[-1]:
                M.append(a[i])
    return(M)

def diff(M1,M2): #prend en compte des listes de string
    a=0
    for i in range (len(M1)): #M1 et M2 meme longueur, test erreur d ortographe
        if M1[i]!=M2[i]:
            a+=1
    return(a)

def test1(M1,M2):#M1 est l'insulte, M2 est ce qu'on test
    if diff(M1,M2)==0:
        return(True)
    if diff(M1,M2)==1 and len(M1)>4 and len(M2)>4:
        return(True)
    elif diff(M1,M2)==1:
        for line in Lines_mot_court:
            K=transfoliste(line)
            if len(K)==len(M2) and diff(K,M2)==0:
                return(False)
            else:
                return(True)
    return(False)

def test2(M1,M2):
    for i in range (len(M2)): #M1 et M2 meme longuer, test permutation deux lettres consecutives
        if i+1<len(M1):
            if M1[i]==M2[i+1]and M1[i+1]==M2[i]:
                return(True)
    return(False)

def test3(M1,M2):#Test de faute de frappe, lettre en plus ou en moins
    m1=0
    m2=0
    diff=0 #on réinitialise diff à 0 pour ce test
    while m1<len(M1) and m2<len(M2) and diff<=1:
        if M1[m1]!=M2[m2]:
            diff+=1
            if m1+1<len(M1) and M1[m1+1]==M2[m2]:
                m1+=1
            if m2+1<len(M2) and M1[m1]==M2[m2+1]:
                m2+=1
    if len(M1)==m1 and len(M2)==m2 and diff<=1:
        return(True)
    return(False)

def test4(L1,L2): #ne tient pas compte des differences dues aux caractères spéciaux: ex shit et sh*t ont diff de 0
    for i in range(len(L2)):#on réduit le mot à sa chaine de caractères
        if L2[i]=='a' or L2[i]=='b' or L2[i]=='c' or L2[i]=='d' or L2[i]=='e' or L2[i]=='f' or L2[i]=='g':
            if L2[i]!=L1[i]:
                b+=1
        elif L2[i]=='h' or L2[i]=='i' or L2[i]=='j' or L2[i]=='k' or L2[i]=='l' or L2[i]=='m' or L2[i]=='n':
            if L2[i]!=L1[i]:
                b+=1
        elif L2[i]=='o' or L2[i]=='p'or L2[i]=='q' or L2[i]=='r' or L2[i]=='s' or L2[i]=='t':
            if L2[i]!=L1[i]:
                b+=1
        elif L2[i]=='u' or L2[i]=='v' or L2[i]=='w' or L2[i]=='x' or L2[i]=='y' or L2[i]=='z':
            if L2[i]!=L1[i]:
                b+=1
    if b==0:
        return(True)
    else:
        return(False)

def test5(M1,lignetwt): #Le test des espaces, où on espace les bouts de mots entre-eux. M1 est l'insulte de la bdd
    Mtwt=[]
    for mot in lignetwt:
        Mtwt+=transfoliste(mot) #on colle la liste de mots les uns aux autres, en supprimant les espaces
    if len(Mtwt)>=len(M1):
        a=0
        while len(M1)+a<=len(Mtwt):
            dif=0
            for i in range(len(M1)):
                if M1[i]!=M1[i+a]:
                    dif+=1
            if dif==0:
                for mot2 in lignetwt:
                    if diff(transfoliste(mot2),M1)==0: #importance de la première lettre dans un mot, test va jusqu'à len(tranforliste(mot2))
                        #on essaye de limiter le hasard
                        return(True)
    return(False)

def mot_proche(mot1,mot2):
    L1=transfoliste(mot1)
    L2=transfoliste(mot2)
    M1=supprdoublon(mot1)
    M2=supprdoublon(mot2)
    if M1!=[] or M1!=[' ']:# pour éviter des comparaisons qui n'ont aucun sens
        if M2!=[] or M2!=[' ']:
            if test1(mot1,mot2)==True:
                return(True)
            elif diff(M1,M2)==2:
                if test2(M1,M2)==True:
                    return(True)
            elif len(M1)==len(M2)+1 or len(M2)==len(M1)+1: #M1 et M2 ont une lettre de difference, oubli ou ajout d'une lettre
                if test3==True:
                    return(True)
            elif len(L1)==len(L2):#cas de caracteres speciaux pour M2. On suppose que mot1 est bien ecrit
                if test4==True:
                    return(True)
    return(False)#pour eviter d'avoir errurs
    
def lignes_proches(l1,l2):#prend en argument deux lignes de text, pas mis sous forme de tweet
    L=[]
    for mot_l1 in l1:
        L+=transfoliste(mot_l1)#permet de coller les deux mots qui composent l'insulte
        if test5(L,l2)==True:
            return(True)
    return(False)

def insulte_test(ligne_tweet):# détecte une insulte dans un tweet déjà standardisé
    for line in Lines_bdd:
        for mot in ligne_tweet:
            if mot_proche(line,mot):
                return(True)
            elif lignes_proches(line, mot):
                return(True)
    return(False)

def detec_insulte(ligne_tweet):
    for mot_tweet in ligne_tweet:
        for line_bdd in Lines_bdd:
            if mot_proche(line_bdd, mot_tweet):
                return(True)

def taux_insulte_twt(twt):
    file3 = open(twt, 'r') 
    Lines_twt = file3.readlines()
    a=0
    b=0
    for line in Lines_twt:
        a+=1
        if insulte_test(line)==True:
            b+=1
    return(b/a)

def taux_insulte_liste_twt(liste_tweet):
    M=[]
    for i in liste_tweet:
        M = [taux_insulte_twt(i)]
    return(M)
