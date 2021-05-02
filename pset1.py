# Problem Set 1 — Saif Khawaja

def substrings(seq):
    sequence = str(seq)
    substring_list = set()

    for i in range(len(sequence)):
        for j in range(len(sequence)):
            substring = sequence[j:len(sequence):i]
            substring_list.add(substring)
    return substring_list


def get_student_avg(student, gradebook_dict):
    scores = {student: gradebook_dict}

    if student in scores:
        avgScores[student] = sum(gradebook_dict) / float(len(gradebook_dict))
        return avgScores
    else:
        return -1


def every_other(seq):
    sliced = seq[0:len(seq):2]
    return sliced


def all_factors(num):
    factors = set()

    for counter in range(1, num):
        if num % counter == 0:
            factors.add(counter)
            factors.add(num)
    counter += 1
    return factors


def all_but_last(seq):
    sequence = seq[0:(len(seq) - 1)]
    return sequence


def alphabet_construct(seq, alphabet):
    x = 0

    for character in list(seq):
        if character in alphabet:
            x = x + 1

    if x == len(seq):
        return True
    else:
        return False


def many_any(lst, k):
    if len([x for x in lst if True]) >= k:
        return True
    else:
        return False


def common_chars(seq, k):
    lst = []
    counter = 0

    for element in seq:
        for character in list(seq):
            if character == element:
                counter = counter + 1
        if counter >= k:
            lst.extend(element, counter)
        counter = 0
    return lst


def dict_to_tuple_list(my_dict):
    return [(k, v) for k, v in my_dict.items()]