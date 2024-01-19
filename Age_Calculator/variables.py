
def main ():
	Amount=30
	data="{} is high or {} is low".format(Amount,20)
	#data="%s is high"% Amount
	print(data,type(data))
	datalen="is good"
	print(len(datalen))
	print(datalen[0:2])

if __name__ == '__main__':main();