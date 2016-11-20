
oContinuer=""
while  oContinuer!='n':

	oInput = input("entre le chiffre de la table de multiplication : ")
		
	i=1
	oBool = oInput.isdigit()

	if oBool == True:
	    oInput = int(oInput)
	    for i in range (1,11):
	        print(oInput,"*",i,"=",oInput*i)
	    i+=16
	  
	    oContinuer = input("voulez vous continuer ? o/n ")
	    if oContinuer == 'n' :
	    	print("au revoir !")
	elif oBool == False:
		print("erreure n est pas  un nombre")
		