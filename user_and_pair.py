import pandas as pd
import numpy as np
import json
from hungarian import *
import random
ls = list(range(1000000))
random.shuffle(ls)


class user():
    def __init__(self, name, age, gender, interest, ideal_age, ideal_gender, identity=None):
        if identity == None:
            self.id = ls[0]
            del ls[0]
        self.name = name
        self.age = int(age)
        self.gender = gender
        self.interest = interest
        self.ideal_gender = ideal_gender
        self.ideal_age = ideal_age
        self.left_child = None
        self.right_child = None
        self.paired = []
        self.paired_id = []

    def difference(self, other):

        if self == other:
            return 100000

        if other in self.paired:
            return 100000

        val = 0
        if self.ideal_gender != other.gender:
            val += 25
        count = 0
        for i in self.interest:
            for j in other.interest:
                if i == j:
                    count += 1
        val += 10*(3-count)
        val += 2*abs(self.ideal_age - other.age)
        return val


class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return super(NpEncoder, self).default(obj)


#############這是測試資料使用的數據############################
df = pd.read_excel('data.xlsx')
rows = df.shape[0]
user_ls = []
user_ls_out = []
for j in range(rows):
    individual = user(df.iat[j, 3], int(
        df.iat[j, 2]), df.iat[j, 0], df.iat[j, 1].split(' '), df.iat[j, 4], df.iat[j, 5])
    print(individual.name, individual.id)
    user_ls.append(individual)
    user_ls_out.append({'id': individual.id, 'name': individual.name, 'age': individual.age, 'gender': individual.gender,
                        'interest': individual.interest, 'ideal_age': individual.ideal_age, 'ideal_gender': individual.ideal_gender, 'paired_id': individual.paired_id})

########################################################################


def pairing_process(user_ls, file2, file_user):
    cost = []
    for k in range(len(user_ls)):
        each_cost = []
        for m in range(len(user_ls)):
            each_cost.append(user_ls[k].difference(user_ls[m]))
        cost.append(each_cost)
    print(cost)
    print(len(cost))
    print(len(cost[0]))
    print(len(cost[1]))
  #  print(user_ls_out)
    hungarian = Hungarian(cost)
    print('calculating...')
    hungarian.calculate()
    print("Calculated value:\t", hungarian.get_total_potential())
    pairs = hungarian.get_results()
    print("Results:\n\t", pairs)
    print(len(pairs))
    print("-" * 80)
    with open(file2, 'w', newline='') as jsonfile:
        json.dump(pairs, jsonfile, cls=NpEncoder)
    for i in range(len(pairs)):
        user_ls[pairs[i][0]].paired.append(user_ls[pairs[i][1]])
        user_ls[pairs[i][0]].paired_id.append(user_ls[pairs[i][1].id])
    # with open(file_user, 'w', newline = '') as user_json:
     #   json.dump(user_ls_out, user_json, cls = NpEncoder)

#pairing_process(user_ls,'pairing.json', 'user_data.json')
