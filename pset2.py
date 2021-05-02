# Problem Set 2 — Saif Khawaja

def my_sort(lst):
    result = lst[::]

    for i in range(len(result)):
        for j in range(len(result) - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]

    return result


def sort_dict(d):
    result = []

    for key in d:
        result.append((key, d[key]))
    for i in range(len(result)):
        for j in range(len(result) - 1):
            if result[j][1] > result[j + 1][1]:
                result[j], result[j + 1] = result[j + 1], result[j]

    return result


def prefixes(seq):
    for i in range(1, len(seq) + 1):
        yield seq[:i]


def suffixes(seq):
    for i in range(len(seq) - 1, -1, -1):
        yield seq[i:]


def slices(seq):
    for i in range(len(seq) - 1):
        for j in range(i + 1, len(seq)):
            yield seq[i:j]


# Halfway


def extract_and_apply(l, p, f):
    return [f(x) for x in l if p(x)]


def my_reduce(function, l, initializer=None):
    if initializer == None:

        result = l[0]

        for i in range(1, len(l)):
            result = function(result, l[i])

        return result

    else:
        result = initializer

        for i in range(len(l)):
            result = function(result, l[i])

        return result


class BSTree(object):
    def __init__(self):
        self.root = None

    def __str__(self):
        if self.root != None:
            return str(self.root)
        else:
            return "_"

    def __len__(self):
        if self.root != None:
            return len(self.root)
        else:
            return 0

    def __contains__(self, element):
        if self.root != None:
            return element in self.root
        else:
            return False

    def insert(self, element):
        if self.root != None:
            self.root.insert(element)
        else:
            self.root = Node(element)

    def elements(self):
        if self.root != None:
            return self.root.elements()
        else:
            return []


class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        result = "("
        if self.left == None:
            result += "_"
        else:
            result += str(self.left)
        result += ", " + str(self.value) + ", "
        if self.left == None:
            result += "_"
        else:
            result += str(self.right)
        result += ")"
        return result

    def __len__(self):
        result = 1
        if self.left != None:
            result += len(self.left)
        if self.right != None:
            result += len(self.right)
        return result

    def __contains__(self, element):
        if element == self.value:
            return True
        elif element < self.value:
            if self.left == None:
                return False
            else:
                return element in self.left
        else:
            if self.right == None:
                return False
            else:
                return element in self.right

    def insert(self, element):
        if element <= self.value:
            if self.left == None:
                self.left = Node(element)
            else:
                self.left.insert(element)
        else:
            if self.right == None:
                self.right = Node(element)
            else:
                self.right.insert(element)

    def elements(self):
        result = []
        if self.left != None:
            result += self.left.elements()
        result.append(self.value)
        if self.right != None:
            result += self.right.elements()
        return result
