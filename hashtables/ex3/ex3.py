def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    num_intersection = {x: 1 for x in arrays[0]}
    result = []
    for i in range(1, len(arrays)):
        for num in arrays[i]:
            if num in num_intersection:
                num_intersection[num] += 1
    for key, value in num_intersection.items():
        if value == len(arrays):
            result.append(key)
    print(num_intersection)
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
