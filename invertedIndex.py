while True:
    print("What file needs te be searched?")
    requiredFile = str(input("Path to file: "))
    print("What word needs to be searched?")
    word = str(input("Word that needs to be searched: "))

    occurances = 0
    wordArray = []

    with (open(requiredFile, 'r')) as f:
        x = f.read().splitlines()
        for lindex, l in enumerate(x):
            wArray = l.split(' ')
            for windex, w in enumerate(wArray):
                if w == word:
                    occurances += 1
                    wordArray.append(str(lindex) + ", " + str(windex))

    print("'{}' occured {} times".format(word, occurances))
    for w in wordArray:
        array = w.split(", ")
        print("Line {}, word {}".format(int(array[0]) + 1, int(array[1]) + 1))
