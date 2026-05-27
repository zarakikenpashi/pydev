"""Convertisseur de devises"""
taux = {"EUR": 655.96, "USD": 605.00, "GBP": 760.00}
try:
    montant = float(input("Montant en FCFA : "))
    
except ValueError:
    print("Veillez entrez un montant valide")
else:
    print(f"{montant} = {(montant / taux['EUR']):.2f} EUR, {(montant / taux['GBP']):.2f} GBP, {(montant / taux['USD']):.2f} USD")

        
    
    

    
