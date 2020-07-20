def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    pairs = []
    positive = set([n for n in a if n > 0])
    # print(positive)

    for num in a:
        if -num in positive:
            pairs.append(-num)

    return pairs


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
