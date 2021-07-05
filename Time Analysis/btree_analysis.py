from user_and_pair import *
import random
from btree import *
import time
import matplotlib.pyplot as plt

ref_gender = ['male', 'female']
ref_interest = ['sprots', 'read', 'dance', 'travel', 'write', 'draw', 'movie', 'music', 'game']
ls = []

for j in range(5000):
    interest_generating = random.choices(list(range(0,9)), k=3)
    name = 'x'
    age = random.randint(18,35)
    gender = ref_gender[j%2]
    interest = [ref_interest[j%9],ref_interest[(j+1)%9], ref_interest[(j+2)%9]]
    user_created = user(name, age, gender, interest, random.randint(18,35),
                        ref_gender[(j+1+int(bool(j%40 == 0)))%2])
    ls.append(user_created)

test_binary_tree = tree()
sampling_n = []
incremental_complexity = []

for r in range(1,5001):
    if r% 50 == 0:
        sampling_n.append(r)
start = time.time()
for k in range(5000):
    
    test_binary_tree.insert(ls[k])
    if k % 50 == 49:
        sample = time.time()
        incremental_complexity.append((sample - start))

plt.plot(sampling_n, incremental_complexity)
plt.title('binary tree n_insertion complexity')
plt.xlabel('number of nodes')
plt.ylabel('time')
plt.show()
