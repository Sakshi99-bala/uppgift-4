
try:
     tal = int(input("Ange ett tal: "))
     resultat = 100 / tal
     print("100 /" , tal, "=", resultat)
except ZeroDivisionError:
 print("Fel: Kan inte dela med noll!")
except ValueError:
 print("Fel: Skriv ett tal, inte text!")
