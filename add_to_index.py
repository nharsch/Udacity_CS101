# Define a procedure, add_to_index,
# that takes 3 inputs:

# - an index: [[<keyword>,[<url>,...]],...]
# - a keyword: String
# - a url: String

# If the keyword is already
# in the index, add the url
# to the list of urls associated
# with that keyword.

# If the keyword is not in the index,
# add an entry to the index: [keyword,[url]]

index = []
tester = [['udacity', ['http://udacity.com', 'http://npr.org']],  ['computing', ['http://acm.org']]]

def add_to_index(index,keyword,url):
    for e in index:
        if e[0] == keyword:
            e[1].append(url)
            return
    index.append([keyword, [url]])

def index_tester(tester):
    for e in tester:
        if type(e[0]) == str:
            return True


add_to_index(index,'udacity','http://udacity.com')
add_to_index(index,'computing','http://acm.org')
add_to_index(index,'udacity','http://npr.org')
print index
        
##print tester
##print index_tester(tester)
##add_to_index(tester,'udacity','http://npr.org')
##print tester

#>>> [['udacity', ['http://udacity.com', 'http://npr.org']], 
#>>> ['computing', ['http://acm.org']]]


