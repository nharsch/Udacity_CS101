# Write a procedure, count_words, which takes as input a string
# and returns the number of words in the string. You may consider words
# as strings of characters separated by spaces.

def count_words(string):
    word = ""
    word_list = []
    for char in string:
        if char != ' ':
            word += char
        else:
            if word:
                word_list.append(word)
                word = ''
    if word:
        word_list.append(word)
        word = ''
    return len(word_list)

def count_words1(string):
    words = string.split()
    return len(words)
passage =("The number of orderings of the 52 cards in a deck of cards "
"is so great that if every one of the almost 7 billion people alive "
"today dealt one ordering of the cards per second, it would take "
"2.5 * 10**40 times the age of the universe to order the cards in every "
"possible way.")
count_words(passage)
print count_words(passage)
print count_words1(passage)
#>>>56

