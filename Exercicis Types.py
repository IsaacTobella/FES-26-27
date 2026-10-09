import os
import subprocess

clear_command = ["cmd", "/c", "cls"] if os.name == "nt" else ["clear"]
subprocess.run(clear_command, check=False)  # Neteja la consola per facilitar la visualització

# Exercici 1
# Imprimeix el tipus del número 25

print(type(25))     # Ens dona com a resultat el tipus del numero, en aquest cas 'int' que significa enter.

# Exercici 2
# Imprimeix el tipus del text "Hola món"

print(type("Hola Món"))     # Ens dona que es un 'str'

# Exercici 3
# Imprimeix el tipus del resultat de la comparació 10 > 5

print(type(10>5))   # Ens dona que la resposta podria ser del tipus 'int' 'str' o 'bool'


