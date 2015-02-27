# recursive definitions

'''
recursive definition has two parts:
	1. Base case  - a starting point
		not defined in terms of itself
	2. Recursive case
		defined in terms of a "smaller version" of itself

Who are your Ancestors?

factorial(n) = n * (n-1) * (n-2) * ....

	factorial(0) = 1 #Base case
	factorial(n) = n * factorial(n-1) #recursive case

Define factorial:
'''

# Define a procedure, factorial, that takes a natural number as its input, and
# returns the number of ways to arrange the input number of items.

def factorial(n):
	if n ==0:
		return 1
	else:
		return n * factorial(n-1)


# print factorial(0)
# #>>> 1

# print factorial(5)
# #>>> 120

# print factorial(10)
# #>>> 3628800

#Palindromes

def is_palindrome(word):
	if word == '':
		return True
	else:
		if word[0] == word[-1]:
			word = word[1:-1]
			return is_palindrome(word)
		else:
			return False
		

# print is_palindrome('')
# #>>> True
# print is_palindrome('abab')
# #>>> False
# print is_palindrome('abaaba')
# #>>> True


#-----------------------------------

'''
Fibonacci Numbers

n + previous state of n + previous state of n

Base Cases:
	fibonacci(0) = 0
	fibonacci(1) = 1

recursive definition:
	fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)
'''

# Define a procedure, fibonacci, that takes a natural number as its input, and
# returns the value of that fibonacci number.

# Two Base Cases:
#    fibonacci(0) => 0
#    fibonacci(1) => 1

# Recursive Case:
#    n > 1 : fibonacci(n) => fibonacci(n-1) + fibonacci(n-2)

## expensive recursive def
# def fibonacci(n):
# 	if n < 0:
# 		return None, "Value must be positive"
# 	if n == 0:
# 		return 0
# 	elif n == 1:
# 		return 1
# 	return fibonacci(n-1) + fibonacci(n-2)

# cheaper while loop
# my shitty answer
# def fibonacci(n):
# 	fib = [0,1]
# 	if n < 0:
# 		return None
# 	if n <= 1:
# 		return fib[n] 
# 	else:
# 		ind = 2
# 		while ind <= n:
# 			ans = fib[ind-1] + fib[ind-2]
# 			fib.append(ans)
# 			ind += 1
# 		return fib[-1]

def fibonacci(n):
	current = 0
	after = 1
	for i in range(0, n):
		current, after = after, current + after
	return current


# print fibonacci(0)
# #>>> 0
# print fibonacci(1)
# #>>> 1
# print fibonacci(15)
# #>>> 610
# print fibonacci(36)

# #mass of earth vs mass of rabits
# mass_of_earth = 5.9722 * 10**24 #kilograms
# mass_of_rabbit = 2 # 2 kilograms per rabbit

# n = 1
# while fibonacci(n) * mass_of_rabbit < mass_of_earth:
# 	n = n + 1
# print n, fibonacci(n)

#----------------------------------------------------

'''
RANKING WEB PAGES


ranking websites based on popularity
Popularity defined by links to other sites and popularity
of linked sites
'''

# def popularity(p):
# 	score = 0
# 	for f in friends(p):
# 		score=score + popularity(f)
# 	return score

'''Relaxation algorithm

start with a guess
while not done:
	make the guess better
'''


'''
popularity(timestep,p)
popularity(timestep,p) = popularity(t-1, f)
'''
def popularity(t,p):
	if t == 0:
		return 1
	else:
		score = 0
		for f in friends(p):
			score = score + poopularity(t-1,f)
		return score

'''
goal of ranking webpages is to rank popularity of linked PAGES

random websurfer

randomly selects links from randomly selected page
'''

# rank(t,url)
# 	if t == 0:
# 		return 1
# 	else:

'''
damping value
typical value of damping constant is something less than one

Google technology:
	Page Rank algorithm

	Altavista's problem was keyword stuffing span

Implementing PageRank / URank:
'''

'''
Computer Ranks
'''

def compute_ranks(graph):
	d = 0.8 #damping factor
	numloops = 10

	ranks = {}
	npages = len(graph)
	for page in graph:
		ranks[page] = 1.0 / npages

	for i in range(0, numloops):
		newranks = {}
		for page in graph:
			newrank = 



