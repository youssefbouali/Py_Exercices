ch = str(input("Entrer un text"))
c=0

for i in range(0, len(ch)):
  if (ch[i]=="p"):
	  print("Le caractere existe en position : ", i)
	  c+=1

print ("Les fois : ",c)