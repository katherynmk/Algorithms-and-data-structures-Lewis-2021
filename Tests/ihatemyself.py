cont = input("Would you like to add a word?")
wordlist = [] 

while cont.lower() == "yes":

        words = input("Please enter a words!  ")

        wordlist.append(words)

        cont = input("Would you like to add another word?")

print(wordlist)
