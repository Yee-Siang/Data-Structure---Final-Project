import json
from user_and_pair import *
from btree import *

def btree_reload(file):
    f = open(file,)
    x = tree()
    data = json.load(f)
    for element in data:
        reborn = user(element['name'], element['age'], element['gender'], element['interest'], element['ideal_age'],
                      element['ideal_gender'], identity = element['id'])
        x.insert(reborn)
       # print(reborn.id)
    f.close()
    return x

def btree_search(identity, binary_tree):
    return binary_tree.search(identity) 

#reborn_tree = btree_reload('storage.json')
#btree_search(794055, reborn_tree)





