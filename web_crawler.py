### Udacity CS101 Web Crawler Unit 3





# urllib.urlopen('http://www.udacity.com/cs101x/index.html').read()

def get_page(url):
    try:
        import urllib
        return urllib.urlopen(url).read()
    except:
        return ""



def find_second(a,b):
    """
    a = target string
    b = search string
    """
    first = a.find(b) 
    return a.find(b, first+1)

##danton = "De l'audace, encore de l'audace, toujours de l'audace"
##print find_second(danton, 'audace')
###>>> 25
##
##twister = "she sells seashells by the seashore"
##print find_second(twister,'she')
###>>> 13
##


    
def get_next_target(page):
    start_link = page.find('<a href=')

    #Insert your code below here
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)

def print_all_links(page):
    '''prints links as long as they are on page'''
    while True:
        url, endpos = get_next_target(page)
        if url:
            print url
            page = page[endpos:]
        else:
            break

def get_all_links(page):
    '''prints links as long as they are on page'''
    links = []
    while True:
        url, endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links

def find_last(a,b):
  last_pos = -1
  while True:
      pos = a.find(b, last_pos+1)
      #print pos
      if pos == -1:
          return last_pos
      last_pos = pos

##def crawl_web(seed, max_pages):
##    tocrawl = [seed]
##    crawled = []
##    while tocrawl:
##        page = tocrawl.pop()
##        if page not in crawled and len(crawled) <= max_pages:
##            #update value of crawl
##            union(tocrawl, get_all_links(get_page(page)))
##            #update value of crawled
##            crawled.append(page)
##    return crawled

### Max Depth Problem
### 



def lookup(index,keyword):
    if keyword in index:
		return index[keyword]
	return None


def add_to_index(index,keyword,url):
    if keyword in index:
        index[keyword].append(url)
    else
    	index[keyword] = [url]


def add_page_to_index(index,url,content):
    '''content = entire text of page,
    returns nothing'''
    words = str(content).split()
    for word in words:
        add_to_index(index,word,url)


##def crawl_web(seed, max_depth):
##    '''web_crawler with maximum depth'''
##    tocrawl = [seed]
##    crawled = []
##    next_depth = []
##    depth = 0
##    while tocrawl and depth <= max_depth:
##        page = tocrawl.pop()
##        if page not in crawled:
##            union(next_depth, get_all_links(get_page(page)))
##            crawled.append(page)
##        if not tocrawl:
##            tocrawl, next_depth = next_depth, []
##            depth += 1
##    return crawled, depth



def crawl_web(seed):
    '''web_crawler with maximum depth'''
    tocrawl = [seed] #inputs url into tocrawl index
    crawled = [] #collects crawled urls
    index = {}  # [[
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            content = get_page(page)
            add_page_to_index(index, page, content)
            union(tocrawl, get_all_links(content))
            crawled.append(page)
    return index

#page = 'http://www.udacity.com/cs101x/index.html'
#seed = get_page(page)
#print get_next_target("There is no link")

#print crawl_web("http://www.udacity.com/cs101x/index.html",1) 
#>>> ['http://www.udacity.com/cs101x/index.html']

#print crawl_web("http://www.udacity.com/cs101x/index.html",3) 
#>>> ['http://www.udacity.com/cs101x/index.html', 
#>>> 'http://www.udacity.com/cs101x/flying.html', 
#>>> 'http://www.udacity.com/cs101x/walking.html']

#print crawl_web("http://www.udacity.com/cs101x/index.html",500) 



