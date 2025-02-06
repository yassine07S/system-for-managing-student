from datetime import datetime
groupes = []
moyene=[]



def ajouter_un_groupe(n):
    for i in range(n):
        numero = int(input("Entrez le numéro unique de groupe : "))
        groupes.append({"numero": numero, "etudiants": []})



def modifier(numero_mod, nouveau):
    for i in groupes:
        if i["numero"] == numero_mod:
            i["numero"] = nouveau



def supprimer(numero_sup):
    for i in groupes:
        if i["numero"] == numero_sup:
            groupes.remove(i)



def ajouter_un_etudiant(numero_groupe, nombre_etudiants):
    if nombre_etudiants<15 :
        for i in groupes:
            if i["numero"] == numero_groupe:
                module=[]
                for x in range(nombre_etudiants):
                    information = {
                        "matricule":int(input("Saisir matricule de l'étudiant : ")),
                        "nom": input("Saisir le nom de l'étudiant : "),
                        "prenom": input("Saisir le prénom de l'étudiant : "),
                        "adresse":input("Saisir l'adresse de l'étudiant : "),
                        "tel":int(input("Saisir le numero de telephon de l'étudiant : ")),
                        "j":int(input("Saisir le jour naissance de l'étudiant : ")),
                        "m":int(input("Saisir le mois naissance de l'étudiant : ")),
                        "a":int(input("Saisir la annee naissance de l'étudiant : ")),
                        "module":[],
                        "moyenne":moyene
                    }
                    i["etudiants"].append(information)
    else:
        print("Le nombre d'étudiantes doit être inférieur à 15")


def calcmoy():
    for i in groupes:
        for x in i["etudiants"]:
            moyene=[]
            for j in x["module"]:
                v={
                    "moyy":(j["analyse"]*4+j["programmation"]*4+j["algorithmique"]*5+j["francais"]*5+j["anglais"]*3+j["arabe"]*3)/24
                }
                moyene.append(v)
            x["moyenne"]=moyene




def modifier_info_etudiants(gr,er):
    for i in groupes:
        if i["numero"]==gr:
            for x in i["etudiants"]:
                if x["matricule"]==er:
                    x["matricule"]=int(input("Saisir matricule de l'étudiant : "))
                    x["nom"]=input("Saisir le nom de l'étudiant : ")
                    x["prenom"]= input("Saisir le prénom de l'étudiant : ")
                    x["adresse"]=input("Saisir l'adresse de l'étudiant : ")
                    x["tel"]=int(input("Saisir le numero de telephon de l'étudiant : "))
                    x["j"]=int(input("Saisir le jour naissance de l'étudiant : "))
                    x["m"]=int(input("Saisir le mois naissance de l'étudiant : "))
                    x["a"]=int(input("Saisir la annee naissance de l'étudiant : "))






def sup_etudiantes(gsupp,esupp):
    for i in groupes:
        if i["numero"]==gsupp:
            for x in i["etudiants"]:
                if x["matricule"]==esupp:
                    i["etudiants"].remove(x)




def afficher(cg,ce):
    for i in groupes:
        if i["numero"]==cg:
            for x in i["etudiants"]:
                if x["matricule"]==ce:
                    print("matricule: ",x["matricule"])
                    print("nom: ",x["nom"])
                    print("prenom: ",x["prenom"])
                    print("adresse: ",x["adresse"])
                    print("telephone: ",x["tel"])
                    print("la date naissance: ",x["j"],"/",x["m"],"/",x["a"])
                    print("le moyenne est :",x["moyenne"])
                    for j in x["module"]:
                        print("la note d'analyse",j["analyse"])
                        print("la note de programmation",j["programmation"])
                        print("la note d'algorithmique",j["algorithmique"])
                        print("la note de francais",j["francais"])
                        print("la note d'anglais",j["anglais"])
                        print("la note d'arabe",j["arabe"])





def afficher_notes(zzg,zze):
    for i in groupes:
        if i["numero"]==zzg:
            for x in i["etudiants"]:
                if x["matricule"]==zze:
                    for j in x["module"]:
                        print("la note d'analyse",j["analyse"])
                        print("la note de programmation",j["programmation"])
                        print("la note d'algorithmique",j["algorithmique"])
                        print("la note de francais",j["francais"])
                        print("la note d'anglais",j["anglais"])
                        print("la note d'arabe",j["arabe"])

                    

def les_notes(ng,ne):
    for i in groupes:
        if i["numero"]==ng:
            for x in i["etudiants"]:
                module=[]
                if x["matricule"]==ne:   
                    v={
                        "analyse":float(input("Entre la note de module d'analyse : ")),
                        "programmation":float(input("Entrez la note de modue de programmation : ")),
                        "algorithmique":float(input("Entrez la note de modue d'algorithme : ")),
                        "francais":float(input("Entrez la note de modue Francais : ")),
                        "anglais":float(input("Entrez la note de modue Anglais : ")),
                        "arabe":float(input("Entrez la note de modue Arabe : ")),
                    }
                    module.append(v)
                    x["module"]=module




def modifier_module(mmg,mme):
    for i in groupes:
        if i["numero"]==mmg:
            for x in i["etudiants"]:
                if x["matricule"]==mme:
                    for j in x["module"]:
                        print("a : pour modifier analyse")
                        print("b : pour modifier programmation")
                        print("c : algorithme")
                        print("d : pour francais")
                        print("e : pour anglais")
                        print("f : pour arabe")
                        x=input("entrez votre choix : ")
                        match x:
                            case "a":
                                j["analyse"]=float(input("Entre la note de module d'analyse : "))
                            case "b":
                                j["programmation"]=float(input("Entrez la note de modue de programmation : "))
                            case "c":
                                j["algorithmique"]=float(input("Entrez la note de modue d'algorithme : "))
                            case "d":
                                j["francais"]=float(input("Entrez la note de modue Francais : "))
                            case "e":
                                j["anglais"]=float(input("Entrez la note de modue Anglais : "))
                            case "f":
                                j["arabe"]=float(input("Entrez la note de modue Arabe : "))
                            case _:
                                print("entrez une lettre entre a et f")



def recuperer():
    a = ""
    b = ""
    m = 0.0
    for i in groupes:
        for x in i["etudiants"]:
            for j in x["module"]:
                s= j["analyse"] +j["programmation"] +j["algorithmique"]+ j["francais"] + j["anglais"] + j["arabe"]
                moyenne = s / 24
                if moyenne > m:
                    m = moyenne
                    a = x["nom"]
                    b = x["prenom"]
    print( a)
    print( b)



def tri():
    for i in groupes:
        i['etudiants'].sort(key=lambda etudiant: etudiant['moyenne'][0]['moyy'], reverse=True)
        print(f"\nle groupe {i['numero']}:\n")
        for x in i['etudiants']:
            print(f"Matricule: {x['matricule']}")
            print(f"Nom: {x['nom']}")
            print(f"Prénom: {x['prenom']}")
            print(f"Adresse: {x['adresse']}")
            print(f"Téléphone: {x['tel']}")
            print(f"Date de naissance: {x['j']}/{x['m']}/{x['a']}")
            print("Tableau de notes:")
            for matiere, note in x['module'][-1].items():
                print(f"La note de {matiere}: {note}")
            print(f"Moyenne: {x['moyenne'][0]['moyy']}")
            print()



def affi_nom(aag,aae):
    for i in groupes:
        if i['numero']==aag:
            for x in i["etudiants"]:
                if x["matricule"]==aae:
                    print("nom : ",x["nom"])
                    print("prnom : ",x["prenom"])





def calc_moyenne(cmg,cme):
    for i in groupes:
        if i["numero"]==cmg:
            for x in i["etudiants"]:
                if x["matricule"]==cme:
                    for j in x["module"]:
                        s=j["analyse"]*4+j["programmation"]*4+j["algorithmique"]*5+j["francais"]*5+j["anglais"]*3+j["arabe"]*3
                        m=s/24
                        return("moyenne of ",x["nom"],x["prenom"],"quel matricule est",cme,"est",m)




def calc_age(cag,cae):
    for i in groupes:
        if i["numero"]==cag:
            for x in i["etudiants"]:
                if x["matricule"]==cae:
                    today=datetime.now()
                    age_year=today.year-x["a"]
                    age_month=today.month-x["m"]
                    age_day=today.day-x["j"]
                    if age_day<0:
                        age_month -= 1
                        age_day=31+age_day
                    if age_month<0:
                        age_year -= 1
                        age_month=12+age_month
                    return("annee:",age_year,"mois:",age_month,"jour:",age_day)



def export(file):
    with open(file,"w") as f:
        for i in groupes:
            for x in i["etudiants"]:
                for j in x["module"]:
                    f.write(f"groupe numero:,{i['numero']},\n")
                    f.write(f"matricule d'etudiant:,{x['matricule']},\n")
                    f.write(f"nom: ,{x['nom']},\n")
                    f.write(f"prenom: ,{x['prenom']},\n")
                    f.write(f"adresse: ,{x['adresse']},\n")
                    f.write(f"tel: ,{x['tel']},\n")
                    f.write(f"date naissanc: ,{x['a']},{x['m']},{x['j']},\n")
                    f.write(f"moyenne : {x['moyenne']}")
                    f.write(f"les notes :\n analyse:{j['analyse']}\n programmation:{j['algorithmique']}\n francais:{j['francais']}\n anglais:{j['anglais']}\n arabe:{j['arabe']}")
    f.close




def aff_groupe(ag):
    for i in groupes:
        if i["numero"]==ag:
            for x in i["etudiants"]:
                print("matricule: ",x["matricule"])
                print("nom: ",x["nom"])
                print("prenom: ",x["prenom"])
                print("adresse: ",x["adresse"])
                print("telephone: ",x["tel"])
                print("la date naissance: ",x["j"],"/",x["m"],"/",x["a"])
                print("le moyenne est :",x["moyenne"])
                for j in x["module"] :
                    print("la note d'analyse",j["analyse"])
                    print("la note de programmation",j["programmation"])
                    print("la note d'algorithmique",j["algorithmique"])
                    print("la note de francais",j["francais"])
                    print("la note d'anglais",j["anglais"])
                    print("la note d'arabe",j["arabe"])
                    print()



while True:
    print("----------menu----------")
    print("1  : pour ajouter un groupe")
    print("2  : pour mdifier un groupe")
    print("3  : pour supprimer un groupe")
    print("4  : pour ajouter un etudiant")
    print("5  : pour modifier informations d'unetudiant")
    print("6  : pour supprimer un etudiant")
    print("7  : pour afficher etudiant")
    print("8  : pour afficher les notes d'un etudiante")
    print("9  : pour saisir les notes d'un etudiante")
    print("10 : pour modifier la note d'un module ")
    print("11 : pour Récupérer le nom et le prénom de l'étudiant ayant la meilleure note")
    print("12 : pour trier")
    print("13 : pour rechercher un etudiant et afficher son nom")
    print("14 : pour calculer la moyenne")
    print("15 : pour calcule age ")
    print("16 : pour exporter les donnees dans un fichier")
    print("17 : pour afficher tout les etudiantes dans un groupe")
    print("18 : pour quitter")
    choix=int(input("saisir un choix : "))
    match choix:
        case 1 :
            n = int(input("Combien de groupes souhaitez-vous ajouter ? : "))
            ajouter_un_groupe(n)
        case 2 :
            numero_mod = int(input("Entrez le numéro du groupe : "))
            nouveau = int(input("Entrez la nouvelle valeur du groupe : "))
            modifier(numero_mod, nouveau)
        case 3:
            numero_sup = int(input("Entrez le numéro du groupe : "))
            supprimer(numero_sup)
        case 4:
            numero_groupe = int(input("Entrez le numéro du groupe auquel vous souhaitez l'ajouter : "))
            nombre_etudiants = int(input("Combien d'étudiants souhaitez-vous ajouter ? : "))
            ajouter_un_etudiant(numero_groupe, nombre_etudiants)
        case 5:
            gr=int(input("Entrez le numéro du groupe : "))
            er=int(input("entrez matricule d'étudiant : "))
            modifier_info_etudiants(gr,er)
        case 6:
            gsupp=int(input("Entrez le numéro du groupe : "))
            esupp=int(input("entrez matricule d'étudiant : "))
            sup_etudiantes(gsupp,esupp)
        case 7:
            cg=int(input("Entrez le numéro du groupe : "))
            ce=int(input("entrez matricule d'étudiant : "))
            afficher(cg,ce)
        case 8:
            zzg=int(input("Entrez le numéro du groupe : "))
            zze=int(input("entrez matricule d'étudiant : "))
            afficher_notes(zzg,zze)
        case 9:
            ng=int(input("Entrez le numéro du groupe : "))
            ne=int(input("entrez matricule d'étudiant : "))
            les_notes(ng,ne)
            calcmoy()
        case 10:
            mmg=int(input("Entrez le numéro du groupe : "))    
            mme=int(input("entrez matricule d'étudiant : "))   
            modifier_module(mmg,mme)
        case 11:
            recuperer()
        case 12:
            tri()
        case 13:
            aag=int(input("Entrez le numéro du groupe : "))
            aae=int(input("entrez matricule d'étudiant : "))
            affi_nom(aag,aae)
        case 14:
            cmg=int(input("Entrez le numéro du groupe : "))
            cme=int(input("entrez matricule d'étudiant : "))
            print(calc_moyenne(cmg,cme))
        case 15:
            cag=int(input("Entrez le numéro du groupe : "))
            cae=int(input("entrez matricule d'étudiant : "))
            print(calc_age(cag,cae))
        case 16:
            file_name=input("Entrez le nom du fichier : ")
            export(file_name)
        case 17:
            ag=int(input("Entrez le numéro du groupe : "))
            aff_groupe(ag)
        case 18:
            break
        case _:
            print("entrez nomber entre 1 et 18")