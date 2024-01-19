
def main ():
	ages=(30,40,15,32)
	print(ages,type(ages))
	print(ages[0:2])

	ages2=[30,40,15,32]
	ages2.append(100)
	ages2.insert(1,33)
	print(ages2,type(ages2))
	print(ages2[0:2])

if __name__ == '__main__':main();