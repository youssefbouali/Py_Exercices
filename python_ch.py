ch = str(input("Entrer un text"))

print ("The lenght is : " , len(ch))

#ch = ch[len(ch)-1] + ch[1:len(ch)-1] + ch[0]

ch = ch[-1] + ch[1:-1] + ch[0]

print (ch)