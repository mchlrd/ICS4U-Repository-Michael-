def targeting(list1, list2, target):
    list1 = [1,2,3]
    list2 = [3,2,1]
    answer1 = []
    answer2 =[]
    target = 3

    for i, item in enumerate(list1):
        if item == target:
            answer1.append(i)
    
    for i in range(len(list2)):
        if list2[i] == target:
            answer2.append(i)

    result = []
    result = answer1 + answer2
    return result