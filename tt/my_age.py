import datetime
def main ():
	DOB=input("Enter your Year Birth: ")
	YearNow=datetime.datetime.now().year
	MyAge=YearNow-int(DOB)
	print("Your age is {} Year".format(MyAge))


if __name__ == '__main__':main();
