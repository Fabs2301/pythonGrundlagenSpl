import random
zufallszahl = random.randint(1,1001)

print("Zahlenraten - errate meine Zahl zwischen 1 und 1000")
counter=0
gewonnen = False
while gewonnen == False:
  zahl = int(input("Welche Zahl?"))
  if (zahl == zufallszahl):
    print("Gratuliere! Du hast gewonnen. Und du hast nur",counter,"Versuche gebraucht")
    gewonnen = True
  elif (zahl < zufallszahl):
    print ("Leider nein! Die gesuchte Zahl ist größer")
    counter=counter+1
    
  elif (zahl> zufallszahl):
    print("Leider nein! Die gesuchte Zahl ist kleiner")
    counter=counter+1