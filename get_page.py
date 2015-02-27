#from urllib import urlopen

def get_page(url):
    from urllib import urlopen
    return urlopen(url).read()

#page = 'http://www.google.com'

