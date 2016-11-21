oNom = input("entrer votre nom : ")
oMontant = input("entrer le montant : ")
oMontant = int(oMontant)
class Banque:

    def __init__(self):
        self.nom = ""
        self.balance = 0

    def ajouter_argent(self, oMontant):
        self.balance += oMontant
        print("vous avez ajouter {0} euro au compte en banque {1}".format(
            oMontant, self.nom))

    def retirer_argent(self, oMontant):
        self.balance -= oMontant
        print("vous avez retirer {0} euro au compte en banque {1}".format(
            oMontant, self.nom))
client_01 = Banque()
client_01.nom = oNom
client_01.retirer_argent(oMontant)
client_02 = Banque()
client_02.nom = "toto"
client_02.balance = 600
print("le nouveau client s\'appele {0} et a dans son compte {1} euro".format(client_02.nom,client_02.balance))

