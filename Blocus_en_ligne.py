#Initialisation des librairies
import asyncio
import time
import colored

#creation des pieces
piece=[
      [[1]],
      [[1],[1]],
      [[1],[1],[1]],
      [[1,0],[1,1]],
      [[1],[1],[1],[1]],
      [[0,1],[0,1],[1,1]],
      [[1,0],[1,1],[1,0]],
      [[1,1],[1,1]],
      [[1,1,0],[0,1,1]],
      [[1],[1],[1],[1],[1]],
      [[0,1],[0,1],[0,1],[1,1]],
      [[0,1],[0,1],[1,1],[1,0]],
      [[0,1],[1,1],[1,1]],
      [[1,1],[0,1],[1,1]],
      [[1,0],[1,1],[1,0],[1,0]],
      [[0,1,0],[0,1,0],[1,1,1]],
      [[1,0,0],[1,0,0],[1,1,1]],
      [[1,1,0],[0,1,1],[0,0,1]],
      [[1,0,0],[1,1,1],[0,0,1]],
      [[1,0,0],[1,1,1],[0,1,0]],
      [[0,1,0],[1,1,1],[0,1,0]]
      ]

#Initialisation du message d'erreur et des couleurs
erreur = ""
couleur = {"#": 'sky_blue_3', "%": 'gold_3b', "&": 'light_green_2', "$": 'light_pink_3'}

def effaceEcran ():
    """Vide l'affichage de la console"""
    for i in range (1,100) :
        print("\n")

def initGrille (grille) :
    """Initialise la grille"""       
    for colonne in range (22) :
        grille[0][colonne]='*'
        grille[21][colonne]='*'

    for ligne in range (22) :
        grille [ligne][0]='*'
        grille [ligne][21]='*'


       
def affiche_piece(dispo, lejoueur):
    """Affiche les pieces disponibles du joueur actuel"""
    print()
    n = len(dispo)//7
    if len(dispo)%7 != 0:
        n += 1
    for ligneA in range (n):
        for ligne in range(5):
            for p in dispo[ligneA*7:7*(ligneA+1)]:
                if ligne == 0:
                    print(p, end=":")
                else:
                    if p <10:
                        print(end="  ")
                    else:
                        print(end="   ")
               
                try:
                    for colonne in piece[p][ligne]:
                        if colonne==1:
                            print(colored.fore(couleur[lejoueur]) + lejoueur + colored.fore('white'), end = " ")
                        else:
                            print(end="  ")
                except:
                    print(end="  "*len(piece[p][0]))
               
                print(end="  ")
            print()
        print()
                   


def get_indice(xy):
    """transforme les lettres en indice."""
    lettreM=" ABCDEFGHIJKLMNOPQRSTU"
    lettrem=" abcdefghijklmnopqrstu"
   
    return lettrem.index(xy[1]), lettreM.index(xy[0])


def test_position(y,x,lapiece, grille, lejoueur, tour):
    """Verifie si la piece peut etre positionner à cet endroit"""
    global erreur
    coin = False
    contact=False

    for ligne in lapiece:
        for i, colonne in enumerate(ligne):
            if colonne==1:
                if grille[y][x+i]!=" ":
                    erreur = "Espace insufisant."
                    return False
                if tour == 1 :
                    if x+i==1 and y==1:
                        coin = True
                    elif x+i==1 and y==20:
                        coin = True
                    elif x+i==20 and y==1:
                        coin = True
                    elif x+i==20 and y==20:
                        coin = True
                else:
                    if grille[y-1][x+i]==lejoueur or grille[y+1][x+i]==lejoueur or grille[y][x+i+1]==lejoueur or grille[y][x+i-1]==lejoueur:
                        erreur = "Vous ne pouvez pas poser des pieces du meme joueur cote à cote."
                        return False
                    if contact==False and (grille[y-1][x+i-1]==lejoueur or grille[y+1][x+i-1]==lejoueur or grille[y-1][x+i+1]==lejoueur or grille[y+1][x+i+1]==lejoueur):
                        contact=True              
                           
        y=y+1

    if tour==1 and coin==False:
        erreur = "La piece doit être placée dans un coin."
        return False
    elif tour>1 and contact==False:
        erreur = "La piece n'est pas en contact avec une autre."
        return False
    return True



def placement_piece(y,x,lapiece, grille, lejoueur, tour):
    """Place la piece aux coordonnées x et y en fonction du joueur."""
    if lapiece[0][0]==0:
        i=0
        while lapiece[0][i]==0:
            x-=1
            i+=1
    if test_position(y,x,lapiece, grille, lejoueur, tour):
        for j, ligne in enumerate(lapiece):
            for i, colonne in enumerate(ligne):
                if colonne==1:
                    grille[y+j][x+i]=lejoueur
        return True
   
   
def rotation_piece(num_piece, Rotation):
    """Tourne la piece"""
    if Rotation == 'G':
        piece[num_piece] = [[piece[num_piece][j][i] for j in range(len(piece[num_piece]))] for i in range(len(piece[num_piece][0])-1,-1,-1)]
    if Rotation == 'D':
        piece[num_piece] = [[piece[num_piece][j][i] for j in range(len(piece[num_piece])-1,-1,-1)] for i in range(len(piece[num_piece][0]))]
   
       
def calcul_resutat(pieces):
    """Calcul le résultat si il reste des pieces"""
    points = 0
    for i in pieces:
        P = piece[i]
        for ligne in P:
            for colonne in ligne:
                points -= colonne
    return points
   

def fin_de_partie(resultat, moi):
    """Affiche le résultat de la partie"""
    print("\nRésultat : ")
    vainqueur = '#'
    for key, value in resultat.items():
        print(f"Joueur {key} : {value} points")
        if value > resultat[vainqueur]:
            vainqueur = key
            
    if vainqueur == moi:
        print("\n Vous avez gagner !\n")
    else:
        print(f"\n Le joueur {vainqueur} à gagner !\n")
   


def afficheGrille (grille) :
    """Affiche la grille"""
    lettreM=" ABCDEFGHIJKLMNOPQRSTU"
    lettrem=" abcdefghijklmnopqrstu"
    print(end="  ")
    for i in lettreM:
        print(i,end=" ")
    print()
    for ligne in range (22) :
        print(lettrem[ligne],end=" ")
        for colonne in range (22) :
            if grille[ligne][colonne] in couleur.keys():
                print (colored.fore(couleur[grille[ligne][colonne]]) + grille[ligne][colonne] + colored.fore('white'),end=" ")
            else:
                print (grille[ligne][colonne],end=" ")
        print(" ")
        
        
##################################
# programme principal :
##################################   
     
role = ""   
        
async def handle_client(reader, writer):
    global erreur

    #Initialise le plateau, les joueurs, leurs pieces et le tour
    grille= [[' ' for i in range(22)] for j in range(22)]
    initGrille (grille)

    motifs = "#%&$"

    #Les listes de piece des 4 joueurs
    joueurs = [[i for i in range(21)] for i in range(4)]
    resultat = {}

    #Joueur et tour actuel
    J = 0
    tour = 1

    #joueur sur le pc
    if role == "O":
        moi = "#&"
    else:
        moi = "%$"
    nextMoi = moi[0]

    coordonnee=""
    choix="/"
    Info=[";"]

    while True:

        for donnee in Info:
            choix, coordonnee = donnee.split(";")

            erreur = ""

            if choix.isdigit():
                choix = int(choix)

                if choix in joueurs[J]:
                    rotation_piece(choix, coordonnee)

                    if len(coordonnee) == 2:
                        lettreM = "ABCDEFGHIJKLMNOPQRSTU"
                        lettrem = "abcdefghijklmnopqrstu"
                        if coordonnee[0] in lettreM and coordonnee[1] in lettrem:
                            y, x = get_indice(coordonnee)
                            if placement_piece(y, x, piece[choix], grille, motifs[J], tour):
                                joueurs[J].remove(choix)


                                if tour == 21:
                                    #Si on est au dernier tour, change le score du joueur
                                    if choix == 0:
                                        resultat[motifs[J]] = 20
                                    else:
                                        resultat[motifs[J]] = 15

                                    #Passe à la seconde couleur du joueur
                                    if motifs[J] in moi:
                                        if nextMoi == moi[0]:
                                            nextMoi = moi[1]
                                        else:
                                            nextMoi = moi[0]

                                    #Supprime le joueurs de la liste
                                    joueurs.pop(J)
                                    motifs = motifs[:J] + motifs[J + 1:]
                                    if len(joueurs) == 0:
                                        effaceEcran()
                                        print("Joueur " + moi[0] + " et "+ moi[1])
                                        afficheGrille(grille)
                                        fin_de_partie(resultat, moi)
                                        break

                                else:
                                    #Passe à la seconde couleur du joueur
                                    if motifs[J] in moi:
                                        if nextMoi == moi[0] and moi[1] in motifs:
                                            nextMoi = moi[1]
                                        elif nextMoi == moi[1] and moi[0] in motifs:
                                            nextMoi = moi[0]
                                            
                                    if J >= len(joueurs) - 1:
                                        tour += 1
                                        J = 0
                                    else:
                                        J += 1


                        else:
                            erreur = "coordonnées invalides !"
                else:
                    erreur = "La piece n'est pas disponible."

            elif choix == 'F':
                points = calcul_resutat(joueurs[J])
                resultat[motifs[J]] = points

                if motifs[J] in moi:
                    if nextMoi == moi[0]:
                        nextMoi = moi[1]
                    else:
                        nextMoi = moi[0]

                motifs = motifs[:J] + motifs[J + 1:]
                joueurs.pop(J)
                if len(joueurs) == 0:
                    fin_de_partie(resultat, moi)
                    break
                elif J >= len(joueurs):
                    tour += 1
                    J = 0

        #Affichage et input et envoi des données

        effaceEcran()
        print("Tour " + str(tour))
        print("Joueur " + colored.fore(couleur[moi[0]]) + moi[0] + colored.fore('white') + " et " + colored.fore(couleur[moi[1]]) + moi[1] + colored.fore('white') + "\n")
        afficheGrille(grille)
        if motifs[J] in moi:
            print(erreur)
        else:
            print()

        #affiche l'ensemble des pièces du joueur si le joueur peut encore jouer.
        try:
            affiche_piece(joueurs[motifs.index(nextMoi)], nextMoi)
        except:
            print("En attente des autres joueurs.")

        #Si ce n'est pas le tour du joueur, attend les réponses de l'autre joueur.
        if len(joueurs) == 0:
            fin_de_partie(resultat, moi)
            break
        elif not motifs[J] in moi:
            data = await reader.read(1024)
            DATA = data.decode()
            
            Info = DATA.split("|")
            Info.pop()
            
             #choix, coordonnee = Info[-2].split(";")

        else:
            choix=input("choississez votre pièce ou finissez (F): ")
            if choix != 'F':
                coordonnee=input("Donnez vos coordonnées (ex:Ab) ou tourner la piece (G :gauche, D :droite) ")
                
            donnee = choix + ";" + coordonnee + "|"
            writer.write(donnee.encode())
            await writer.drain()

            Info = [choix + ";" + coordonnee]
        


async def main_serveur():
    IP = input("Entrer l'adresse du serveur (Default port : 127.0.0.1): ")
    server = await asyncio.start_server(
        handle_client, IP, 8888)

    addr = server.sockets[0].getsockname()
    print(f'Serveur en attente de connexions sur {addr}')

    async with server:
        await server.serve_forever()



async def main_client():
    IP = input("Entrer l'adresse du serveur (Default port : 127.0.0.1): ")
    reader, writer = await asyncio.open_connection(IP, 8888)

    await handle_client(reader, writer)

    writer.close()
    await writer.wait_closed()

def main():
    global role
    role = input("Etes vous le serveur (O ou N) ? : ")
    
    if role == "O":
        asyncio.run(main_serveur())
    elif role == "N":
        asyncio.run(main_client())
        
if __name__ == "__main__":
    main()
