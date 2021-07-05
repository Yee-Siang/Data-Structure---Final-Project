from user_and_pair import *
import random
from avltree import *


ref_gender = ['male', 'female']
ref_interest = ['sprots', 'read', 'dance', 'travel', 'write', 'draw', 'movie', 'music', 'game']
ls = []
import time
import matplotlib.pyplot as plt

for j in range(5000):
    interest_generating = random.choices(list(range(0,9)), k=3)
    name = 'x'
    age = random.randint(18,35)
    gender = ref_gender[j%2]
    interest = [ref_interest[j%9],ref_interest[(j+1)%9], ref_interest[(j+2)%9]]
    user_created = user(name, age, gender, interest, random.randint(18,35),
                        ref_gender[(j+1+int(bool(j%40 == 0)))%2])
    ls.append(user_created)

sampling_n = []
for r in range(1,5001):
    if r% 50 == 0:
        sampling_n.append(r)

test_avl_tree = AVLTree()
new_incremental_complexity = []
new_start = time.time()
for k in range(5000):
    test_avl_tree.insert_node(test_avl_tree.root, ls[k])
    if k % 50 == 49:
        sample = time.time()
        new_incremental_complexity.append(sample - new_start)

plt.plot(sampling_n, new_incremental_complexity)
plt.title('AVL tree n_insertion complexity')
plt.xlabel('number of nodes')
plt.ylabel('time')

plt.plot(sampling_n, new_incremental_complexity)
plt.show()
