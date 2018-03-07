print("Simple Taschenrechner")
zahl1 = int(input("Bitte erste Zahl eingeben: "))
zahl2 = int(input("Bitte erste Zahl eingeben: "))
operation = input("+, -, / oder * rechnen?")

if (operation == "+"):
    summe = zahl1 + zahl2
    print("Summe = ", summe)
if(operation == "-"):
    differenz = zahl1 - zahl2
    print("Differenz = ", differenz)
if(operation == "/"):
    if(zahl2 != 0):
      quotient = zahl1 / zahl2
      print("Quotient = ", quotient)
    else: print("Error kann nicht durch 0 dividieren!")
else:
  produkt = zahl1 * zahl2
  print("Produkt = ", produkt)
