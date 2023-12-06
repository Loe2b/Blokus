import Blocus_en_ligne as Br
import Blocus_local as Bl

choix = input("Voulez-vous jouez en local (L) ou en reseau (R)? ")

if choix == "L":
    Bl.main()

elif choix == "R":
    Br.main()