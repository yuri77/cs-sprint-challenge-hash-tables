# Your code here


def finder(files, queries):
    """
    YOUR CODE HERE
    """
    keywords = {}
    for file in files:
        keyword = file.rsplit('/', 1)[1]
        if keyword not in keywords:
            keywords[keyword] = []
        keywords[keyword].append(file)
    # print(keywords)
    result = []
    for item in queries:
        if item in keywords:
            result += keywords[item]

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/foa/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
