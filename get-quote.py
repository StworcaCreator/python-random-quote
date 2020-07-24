def primary():
	print("Keep it logically awesome.")

	f = open("D:\\github\\python-random-quote\\quotes.txt")
	quotes = f.readlines()
	f.close()

	print(quotes)

if __name__== "__main__":
 	primary()
