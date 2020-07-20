def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Brute Force Solution O(n^2)
    # targets = {}
    # for i in range(0, length-1):
    #     print("i", i)
    #     for j in range(i+1, length):
    #         print("j", j)
    #         target = weights[i]+weights[j]
    #         if target not in targets:
    #             targets[target] = (j, i)
    # print("targets", targets)
    # if limit in targets:
    #     return targets[limit]
    # else:
    #     return None
    targets = {}
    for i in range(length):
        if weights[i] not in targets:
            target = limit - weights[i]
            targets[target] = i
        else:
            return (i, targets[weights[i]])
    return None


weights_4 = [4, 6, 10, 15]
print(get_indices_of_item_weights(weights_4, 4, 21))
