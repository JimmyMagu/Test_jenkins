words = set()


def check(word):
    if word in words:
        return True
    else:
        return False


def load(dictionary):
    file = open(dictionary, "r")
    for line in file:
        words.add(line.rsplit())
    close(file)
    return True
