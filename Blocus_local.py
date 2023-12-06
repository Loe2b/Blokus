import time
import colored

#creer des pieces
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

erreur = ""

couleur = {"#": 'sky_blue_3', "%": 'gold_3b', "&": 'light_green_2', "$": 'light_pink_3'}


def effaceEcran ():
    for i in range (1,100) :
        print("\n")


# Initialise la grille

def initGrille (grille) :
           
    for colonne in range (22) :
        grille[0][colonne]='*'
        grille[21][colonne]='*'

    for ligne in range (22) :
        grille [ligne][0]='*'
        grille [ligne][21]='*'


       
def affiche_piece(dispo, lejoueur):
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
   

def fin_de_partie(resultat):
    print("\nRésultat : ")
    vainqueur = '#'
    for key, value in resultat.items():
        print(f"Joueur {key} : {value} points")
        if value > resultat[vainqueur]:
            vainqueur = key
    print(f"\n Le joueur {vainqueur} à gagner !\n")
   


def afficheGrille (grille) :
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

def main():
       
    #Initialise le plateau, les joueurs, leurs pieces et le tour
    grille= [[' ' for i in range(22)] for j in range(22)]
    # grille qui pourra contenir
    # 3 sortes de caractères : '*' ou 'O' ou le caractere espace ' '
    
    motifs = "#%&$"
    
    initGrille (grille)
    
    #Les listes de piece des 4 joueurs
    joueurs = [[i for i in range(21)] for i in range(4)]
    resultat = {}
    
    #Joueur et tour actuel
    J = 0
    tour = 1
    
    coordonnee=""
    choix="/"
    while True :
        erreur = ""
    
        if choix.isdigit():
            choix = int(choix)
    
            if choix in joueurs[J]:
                rotation_piece(choix, coordonnee)
    
                if len(coordonnee) == 2:
                    lettreM="ABCDEFGHIJKLMNOPQRSTU"
                    lettrem="abcdefghijklmnopqrstu"
                    if coordonnee[0] in lettreM and coordonnee[1] in lettrem:
                        y, x = get_indice(coordonnee)
                        if placement_piece(y, x, piece[choix], grille, motifs[J], tour):
                            joueurs[J].remove(choix)
                                 
                            if tour == 21:
                                if choix == 0:
                                    resultat[motifs[J]] = 20
                                else:
                                    resultat[motifs[J]] = 15
                                joueurs.pop(J)
                                motifs = motifs[:J] + motifs[J+1:]
                                if len(joueurs) == 0:
                                    fin_de_partie(resultat)
                                    break
                           
                            else:
                                if J >=len(joueurs)-1:
                                    tour+=1
                                    J=0
                                else:
                                    J+=1
                    else:
                        erreur = "coordonnées invalides !"
            else:
                erreur = "La piece n'est pas disponible."
    
    
    
        #Affichage et input
    
        effaceEcran()
        afficheGrille(grille)
        print(erreur)
        affiche_piece(joueurs[J], motifs[J])
    
        choix=input("choississez votre pièce ou finissez (F): ")
        if choix == 'F':
            points = calcul_resutat(joueurs[J])
            resultat[motifs[J]] = points
           
            motifs = motifs[:J] + motifs[J+1:]
            joueurs.pop(J)
            if len(joueurs) == 0:
                fin_de_partie(resultat)
                break
            elif J >= len(joueurs):
                tour+=1
                J=0
        else:
            coordonnee=input("Donnez vos coordonnées (ex:Ab) ou tourner la piece (G :gauche, D :droite) ")
            
if __name__ == "__main__":
    main()