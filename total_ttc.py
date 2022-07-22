def total_ttc ():
  MontantHT = float(input("Entrer Le montant hors taxes d'article HT"));
  
  Taux_TVA = float(input("Entrer Le taux de TVA"));

  Nbarticles = float(input("Entrer Le nombre d'articles"));
  
  TotalTTC = Nbarticles * MontantHT * (1 + Taux_TVA);
  
  print ("Le TotalTTC ", TotalTTC);

while 1==1: 
  total_ttc ()