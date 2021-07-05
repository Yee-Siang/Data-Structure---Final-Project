from hungarian import *
from user_and_pair import *
def pairing_process(user_ls, file2, file_user):
    cost = []
    for k in range(len(user_ls)):
        each_cost = []
        for m in range(len(user_ls)):
            each_cost.append(user_ls[k].difference(user_ls[m]))
        cost.append(each_cost)
    
    hungarian = Hungarian(cost)
    hungarian.calculate()
    pairs = hungarian.get_results()
    '''
    with open(file2, 'w', newline='') as jsonfile:
        json.dump(pairs, jsonfile, cls = NpEncoder)
    '''
    for i in range(len(pairs)):
    #    user_ls[pairs[i][0]].paired.append(user_ls[pairs[i][1]])
        user_ls[pairs[i][0]].paired_id.append(user_ls[pairs[i][1].id])
    '''
    with open(file_user, 'w', newline = '') as user_json:
        json.dump(user_ls_out, user_json, cls = NpEncoder)
    '''
    return pairs
