### Algorithm analysis

import time

def add_to_index(index,keyword,url):
    for e in index:
        if e[0] == keyword:
            e[1].append(url)
            return
    index.append([keyword, [url]])

def time_execution(code):
	start = time.clock()
	result = eval(code)
	run_time = time.clock() - start
	return result, run_time

def spin_loop(n):
	i = 0
	while i < n:
		i += 1
		
### eval interprets string as python code

# try >>> time_execution('spin_loop(100000)')

def add_to_index(index,keyword,url):
    for e in index:
        if e[0] == keyword:
            e[1].append(url)
            return
    index.append([keyword, [url]])

def make_string(p):
	s = ""
	for e in p:
		s += e
	return s

def make_big_index(size):
	index = []
	letters = ['a','a','a','a','a','a','a','a',]
	while len(index) < size:
		word = make_string(letters)
		add_to_index(index, word, 'fake')
		for i in range(len(letters) - 1, 0, -1):
			if letters[i] < 'z':
				letters[i] = chr(ord(letters[i]) + 1)
				break
		else:
			letters[i] = 'a'
	return index
	

			

