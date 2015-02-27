# def bad_hash_string(keyword, buckets):
# 	'''bad hasher'''
# 	return ord(keyword[0])%buckets
# 	print keyword[0]
# 
# def better_hash_string(keyword, buckets):
# 	keytot = 0
# 	for i in keyword:
# 		keytot += ord(i)
# 	return keytot % buckets
# 
# print better_hash_string('tester',26)

def hashtable_update(htable, key, value):
	bucket = hashtable_get_bucket(htable, key)
	for e in bucket:
		if e[0] == key:
			e[1] = value
			return htable
	bucket.append([key, value])
	return htable	 
				 
def hashtable_lookup(htable, key):
	bucket = hashtable_get_bucket(htable, key)
	for entry in bucket:
		if entry[0] == key:
			return entry[1]
	return None


def hashtable_add(htable, key, value):
	hashtable_get_bucket(htable, key).append([key, value])
	return htable

def hashtable_get_bucket(htable,keyword):
    return htable[hash_string(keyword, len(htable))]

#this works faster, smaller computations each time
def hash_string(keyword, buckets):
	h = 0
	for c in keyword:
		h = (h + ord(c)) % buckets
	return h

def make_hashtable(nbuckets):
    table = []
    for unused in range(0,nbuckets):
        table.append([])
    return table
    
table = [[['Ellis', 11], ['Francis', 13]], [], [['Bill', 17], ['Zoe', 14]],
[['Coach', 4]], [['Louis', 29], ['Nick', 2], ['Rochelle', 4]]]

hashtable_update(table, 'Bill', 42)
hashtable_update(table, 'Rochelle', 94)
hashtable_update(table, 'Zed', 68)
hashtable_update(table, 'Zed', 68)
print table



#>>> [[['Ellis', 11], ['Francis', 13]], [['Zed', 68]], [['Bill', 42], 
#>>> ['Zoe', 14]], [['Coach', 4]], [['Louis', 29], ['Nick', 2], 
#>>> ['Rochelle', 94]]]

test_table = [[['Francis', 13], ['Ellis', 11]], [['Andy', 5]], [['Bill', 17],
['Zoe', 14]], [['Coach', 4]], [['Louis', 29], ['Rochelle', 4], ['Nick', 2]]]

test_table2 = [[['search', 'verb']], [], [['Peter', 'proper noun']], [['Udacity',
'super noun']], [['with', 'preposition']]]

print hashtable_update(test_table, 'Francis', 7)
print hashtable_update(test_table2, 'Udacity', 'proper noun')

