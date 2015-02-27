### UDACITY cs101 problem sets
##
##def bigger(a,b):
##    if a > b:
##        return a
##    else:
##        return b
##
##def biggest(a,b,c):
##    return bigger(a, bigger(b,c))
##
##
##
##def median(a,b,c):
##    big = biggest(a,b,c)
##    if big == a:
##        return bigger(b,c)
##    if big == b:
##        return bigger(a,c)
##    else:
##        return bigger(a,b)
##
##        
##def set_range(a,b,c):
##    top = biggest(a,b,c)
##    if top == a:
##        if bigger(b,c) == b:
##            bottom = c
##        else:
##            bottom = b
##    if top == b:
##        if bigger(a, c) == a:
##            bottom = c
##        else:
##            bottom = a
##    if top == c:
##        if bigger(a,b) == a:
##            bottom = b
##        else:
##            bottom = a
##    return top - bottom
##
##
##print set_range(10, 4, 7)
#####>>> 6  # since 10 - 4 = 6
####
##print set_range(1.1, 7.4, 18.7)
#####>>> 17.6 # since 18.7 - 1.1 = 17.
##
##
##

def fix_machine(debris, product):
    d = str(debris)
    p = str(product)
    collector = ""
    ind = 0
    while len(collector) < len(product):
        if d.find(p[ind]) != -1:
            collector = collector + p[ind]
            ind += 1
        else:
            return "Give me something that's not useless next time."
    return collector

print fix_machine('testdebrislegin','nigel')

##print "Test case 1: ", fix_machine('UdaciousUdacitee', 'Udacity') == "Give me something that's not useless next time."
##print "Test case 2: ", fix_machine('buy me dat Unicorn', 'Udacity') == 'Udacity'
##print "Test case 3: ", fix_machine('AEIOU and sometimes y... c', 'Udacity') == 'Udacity'
##print "Test case 4: ", fix_machine('wsx0-=mttrhix', 't-shirt') == 't-shirt'

        
