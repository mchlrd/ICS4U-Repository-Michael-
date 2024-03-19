def mean(a_list):
    #some code
    return sum(a_list) / len(a_list)


print(mean([3,1,4,1,5,9]))


def median(a_list):
    a_list.sort()

    if len(a_list) % 2 == 0:
        mid - len(a_list) // 2
        answer = (a_list[mid] + a_list[mid+1]) / 2
    else:
        answer = a_list[mid]

    return answer