# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 17:23:47 2022

@author: raukh
"""

import os, shutil, PIL.Image

def RegroupeAll(dos,dosR):
    s='\ '
    for nom in os.listdir(dos):
        os.chdir(dos)
        if os.path.isdir(nom) and nom != 'Conv':
            RegroupeAll(dos+s[0]+nom,dosR)
        elif dos != dosR:
            source = dos+s[0]+nom
            if nom in os.listdir(dosR):
                nomOk = False
                c = 1
                while nomOk != True:
                    nomM = '('+str(c)+')'+nom
                    if nomM not in os.listdir(dosR):
                        nomOk = True
                        nom = nomM
                    c += 1
            destination = dosR+s[0]+nom
            shutil.copyfile(source, destination)
            os.chdir(dos)
            os.remove(source)

def SuppDoseVide(dos,dosR):
    s='\ '
    os.chdir(dos)
    for nom in os.listdir(dos):
        os.chdir(dos)
        if os.path.isdir(nom) and os.listdir(dos+s[0]+nom) != [] and nom != 'Conv':
            SuppDoseVide(dos+s[0]+nom, dos)
        if os.path.isdir(nom) and os.listdir(dos+s[0]+nom) == [] and nom != 'Conv':
            os.chdir(dosR)
            os.rmdir(dos+s[0]+nom)
            
def Conversion(dos,dosR):
    s='\ '
    os.chdir(dos)
    if 'Conv' not in os.listdir(dosR):
        os.chdir(dosR)
        os.mkdir('Conv')
    for nom in os.listdir(dos):
        os.chdir(dos)
        ext = nom[-3]+nom[-2]+nom[-1]
        if os.path.isdir(nom) and nom != 'Conv':
            Conversion(dos+s[0]+nom, dosR)
        else:
            ext = nom[-3]+nom[-2]+nom[-1]
            if ext == 'JPG' or ext == 'jpg':
                pass
            elif os.path.isdir(nom) == False:
                source = dos+s[0]+nom
                destination = dosR+s[0]+'Conv'+s[0]+nom
                shutil.copyfile(source,destination)
                os.chdir(dos)
                os.remove(dos+s[0]+nom)

def Renom(dos):
    def EXIF(dos,nom):
        os.chdir(dos)
        img = PIL.Image.open(nom) 
        data = img._getexif()
        return data
        
    s='\ '
    os.chdir(dos)
    for nom in os.listdir(dos):
        print(nom)
        os.chdir(dos)
        if os.path.isdir(nom) and nom != 'Conv':
            Renom(dos+s[0]+nom)
        elif os.path.isdir(nom) == False:
            source = dos+s[0]+nom
            data = EXIF(dos,nom)
            if data == None:
                print("non")
                data = '00000000000000000000'
            else:
                data = data[36867]
            annee = data[0]+data[1]+data[2]+data[3]
            mois = data[5]+data[6]
            jour = data[8]+data[9]
            heure= data[11]+data[12]
            minute = data[14]+data[15]
            seconde = data[17]+data[18]
            nomR = annee+'-'+mois+'-'+jour+'_'+heure+'.'+minute+'.'+seconde
            if nomR+'.JPG' != nom:
                nomOk = False
                c = 1
                nomM = nomR
                while nomOk != True:
                    if nomM+'.JPG' not in os.listdir(dos):
                        nomOk = True
                    else:
                        nomM = nomR+' ('+str(c)+') '
                        c+= 1
                print(nomM+'.JPG')
                destination = dos+s[0]+nomM+'.JPG'
                os.chdir(dos)
                shutil.copyfile(source,destination)
                os.chdir(dos)
                os.remove(dos+s[0]+nom)
                
def Tri(dos):
    def EXIF(dos,nom):
        os.chdir(dos)
        img = PIL.Image.open(nom) 
        data = img._getexif()
        return data
    s='\ '
    for nom in os.listdir(dos):
        print(nom)
        print(os.path.isdir(dos+s[0]+nom))
        if os.path.isdir(dos+s[0]+nom):
            print("dossier")
        else:
            print("fichier")
            os.chdir(dos)
            data = EXIF(dos,nom)
            data = data[36867]
            annee = data[0]+data[1]+data[2]+data[3]
            if annee not in os.listdir(dos):
                os.mkdir(annee)
            source = dos+s[0]+nom
            destination = dos+s[0]+annee+s[0]+nom
            shutil.copyfile(source,destination)
            os.chdir(dos)
            os.remove(source)
    



         
dos = input("Chemin complet vers le dossier mère : ")
RegroupeAll(dos,dos)
SuppDoseVide(dos,dos)
Conversion(dos,dos)
Renom(dos)
Tri(dos)
os.chdir(r"C:\Users\Public")     