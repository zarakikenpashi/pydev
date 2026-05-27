
prenom = "Lelouche"
annee_en_cours = 2026
prix_xof = 15000
taux = 655.957

prix_euro = prix_xof / taux
print(f"Bonjour {prenom} ! En {annee_en_cours}, {prix_xof} F CFA = {prix_euro:.2f} EUR, {isinstance(prix_euro,int)}")