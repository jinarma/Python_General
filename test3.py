#Program to capitalize the specific word

def highlight_word(sentence, word):
	output = sentence.replace(word, word.upper())
	return output
print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))