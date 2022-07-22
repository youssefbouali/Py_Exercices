ch = str(input("Entrer un text"))
c=0
ch2 = ""

for i in range(0, len(ch)):
  if (ch[i]=="e"):
	  print("Le caractere existe en position : ", i)
	  #ch2 = ch2+"1"
	  c+=1
	  
  if (ch[i]!="e"):
	  ch2 = ch2+ch[i]

print ("Les fois : ",c)
print ("Neveau ch : ",ch2)