def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    merged_weight = {}
    # for i in range(len(weights)-1):
    #     print("i", i)
    #     print("weights[i], weights[i+1]", weights[i], weights[i+1])
    #     sum_weight = weights[i]+weights[i+1]
    #     if sum_weight not in merged_weight:
    #         merged_weight[sum_weight] = (i+1, i)

    # if merged_weight[limit]:
    #     return merged_weight[limit]
    # else:
    #     return None

    # for index in range(0,length):
    #     current_wight=weights[index]
    #     target_weight = limit -  current_wight
    #     if target_weight in weights:
    targets = {}
    for i in range(0, length-1):
        print("i", i)
        for j in range(i+1, length):
            print("j", j)
            target = weights[i]+weights[j]
            if target not in targets:
                targets[target] = (j, i)
    print("targets", targets)
    if limit in targets:
        return targets[limit]
    else:
        return None


weights_4 = [4, 6, 10, 15]
print(get_indices_of_item_weights(weights_4, 4, 21))
