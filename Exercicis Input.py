###
# Exercicis - input()
# Practica l'entrada de dades i la conversió de tipus amb exemples de telecomunicacions.
###

# Exercici 1
# Demana el nom d'un tècnic i el nom de la xarxa que està instal·lant.
# Després, mostra un missatge amb aquesta informació.

nom = input("Nom Tècnic: ")
xarxa = input("\nNom Xarxa: ")
print(
    f"\n\nIdentificació del Tècnic: {nom}\n"
    f"Identificació de la Xarxa: {xarxa}"
    )

# Exercici 2
# Demana la longitud d'un enllaç de fibra en quilòmetres i la velocitat de transmissió
# en Gbps. Mostra quants segons caldrien per transmetre 1 GB de dades.
# Suposa que 1 GB = 8 Gb i que la velocitat es manté constant.

lon = input("\n\nLongitud (km): ")
vel = input("\nVelocitat (Gbps): ")

temps_trans = float(vel)/8

print(
    f"\n\nPer transmetre 1GB de dades trigaria {temps_trans}s."
)

# Exercici 3
# Demana el nombre d'hores de feina i el preu per hora d'una instal·lació de xarxa.
# Demana també el preu del material.
# Mostra el cost total de la instal·lació.

hores = input("\nHores de feina: ")
preu_hora = input("\nQuant es paga per hora d'instalació: ")
preu_mat = input("\nPreu del material: ")

print(
    f"\n\nEl preu total serà de {float(hores)*float(preu_hora)+float(preu_mat)}€"
)