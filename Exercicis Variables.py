###
# Exercicis - variables
# Completa els exercicis següents creant i utilitzant variables.
###

# Exercici 1
# Crea variables per desar el nom d'un encaminador, la seva ubicació,
# el nombre de ports i si està encès. Mostra les dades en una frase
# utilitzant una f-string.

nom = "Router"   # Pels noms es pot utilitzar tant " com '
ubicacio = 'Casa'
nombre_ports = 10
estat_router = True

if estat_router == True: #Provant cosetes
    estat_router = 'ON'

print(
    f" Encaminador: {nom}\n Ubicació: {ubicacio}\n "
    f"Nombre de ports: {nombre_ports}\n Estat del Router: {estat_router}")
# Exercici 2
# Crea variables per desar els GB inclosos en un pla de dades mòbils
# i els GB consumits. Calcula quants GB queden i mostra el resultat.
# Després, actualitza el consum amb un valor nou i torna a calcular
# quants GB queden.

gb_guardats = 100
gb_consumits = 75

gb_restants = gb_guardats - gb_consumits

print(
    f"\n N'has fet ús de {gb_consumits}GB\n"
    f" Et queden {gb_restants}GB\n"
    )

gb_consumits = 98
gb_restants = gb_guardats - gb_consumits

print(
    f" N'has fet ús de {gb_consumits}GB\n"
    f" Et queden {gb_restants}GB\n"
    )