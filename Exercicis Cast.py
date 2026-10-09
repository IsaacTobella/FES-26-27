import os
import subprocess

clear_command = ["cmd", "/c", "cls"] if os.name == "nt" else ["clear"]
subprocess.run(clear_command, check=False)  # Neteja la consola per facilitar la visualització

# Exercici 1
# Demana a l'usuari quants paquets ha rebut un encaminador. Converteix el valor
# introduït a un nombre enter, suma-hi 1200 paquets i mostra el total.)))
paquets_rebuts = int(input("Quants paquets ha rebut l'encaminador? "))
total_paquets = paquets_rebuts + 1200
print(f"Total de paquets: {total_paquets}")


# Exercici 2
# Demana a l'usuari la velocitat d'una connexió en Mbps. Converteix el valor
# introduït a un nombre decimal i calcula la velocitat equivalent en MB/s
# dividint-la per 8. Mostra el resultat.

velocitat_rebuda = float(input("Quina velocitat de connexió tens? "))
velocitat_rebuda = velocitat_rebuda/8
print (f"La teva velocitat en MB/s és de {velocitat_rebuda:.2f}MB/s")


