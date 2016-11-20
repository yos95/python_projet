annee = input("année : ")
annee = int(annee)
print (annee)



if annee%400==0 or( annee%4==0 and annee%100 !=0):
  print ("l'année " ,annee, " est bissextile")
else :
  print ("l'annnée ",annee, " n'est pas bissextile")
 

