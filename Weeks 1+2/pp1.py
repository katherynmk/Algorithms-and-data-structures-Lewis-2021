#Write a Python program that inputs a list of words, separated by whitespace,and outputs
#how many times each word appears in the list. Youneed not worry about efficiency at this point, however, as this topic issomething that will be addressed later in this book.

counter = {}
#creates a dictionary to display the words with the amount of times they are seen

wordlist = input( "Enter a list of words:   " )
#user puts in list seperated by white space 

wordlist = wordlist.split(" ")
#seperates the words by the space between them 

words = (wordlist)
#creats a list of the words to search through in the for loop

for word in words:
#searches through the list of words one word at a time 

    if word != "":
#if the word does not equal nothing

        counter[word] = wordlist.count(word)
#add the word to the dictionary while counting how many times it is in the list

print(counter)
#prints the final dictionary with the words and their counter 


