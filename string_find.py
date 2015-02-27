a = "testerttttt"
b= "t"


#print a.find(b)
##
##inc = 0
##while True:
##    if inc != -1:
##        index = [1,2]
##        inc = a.find(b, inc+1)
##        index.append(1)
##print index            
 

##def find_last(a,b):
##    a, b = str(a), str(b)
##    last_pos = -1
##    while True:
##        pos = a.find(b, last_pos)
##        if pos == -1:
##            return last_pos
##        last_pos = pos

def find_last(a,b):
    last_pos = -1
    while True:
        pos = a.find(b, last_pos+1)
        #print pos
        if pos == -1:
            return last_pos
        last_pos = pos

#print a.find(b, -1)
print find_last(a,b)
