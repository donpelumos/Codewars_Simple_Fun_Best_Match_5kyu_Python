__author__ = 'Don Pelumos'
'''URL FOR THE KATA - https://www.codewars.com/kata/simple-fun-number-166-best-match/train/python'''
def best_match(goals1, goals2):
    goal_diff = []
    result = []
    min_positions = []
    indexes = []
    final_indexes = []
    min_goal_diff = 10000
    final_ans = 0
    for i in range(0,len(goals1),1):
        goal_diff.append(goals1[i]-goals2[i])
    for i in range(0,len(goals2),1):
        result.append(int(goals2[i]/goal_diff[i]))
    for i in range(0,len(goal_diff),1):
        if(goal_diff[i] < min_goal_diff):
            min_goal_diff = goal_diff[i]
    for i in range(0,len(goals2),1):
        indexes.append(int(goals2[i]/goal_diff[i]))
    for i in range(0,len(goal_diff),1):
        if(min_goal_diff == goal_diff[i]):
            min_positions.append(i)
            final_indexes.append(indexes[i])
    if(len(min_positions) == 1):
        final_ans = min_positions[0]
    else:
        for i in range(0,len(min_positions),1):
            pos = final_indexes.index(max(final_indexes))
            final_ans = min_positions[pos]
    return final_ans
print(best_match([4,3,4],
                 [1,1,1]))