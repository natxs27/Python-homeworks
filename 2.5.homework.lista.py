numer=["1","2","3","4","5","6","7","8","9","10"]
nazwa=["Hydrogen","Helium","Lithium","Beryllium","Borium","Carbon","Nitrogen","Oxygen","Fluorine","Neon"]
skrot=["H","He","Li","Be","B","C","N","O","F","Ne"]
masa=["1","4","7","9","11","12","14","16","19","20"]
b='+---+--------------------+------+----------+'
print(b)
print("|No.|Name (en)           |Symbol|Weight (u)|")
print(b)
for x in range(0,10):
    print("|" + "|".join([(numer[x]).rjust(3),nazwa[x].ljust(20),skrot[x].center(6),masa[x].rjust(10)]) + "|")
    print(b)
    