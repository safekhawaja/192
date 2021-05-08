# Problem Set 1 — Saif Khawaja

def substrings(seq):
    sequence = set()
    for i in range(len(seq)):
        for j in range(i, len(seq) + 1):
            sequence.add(seq[i:j])
    return sequence


def get_student_avg(student, gradebook_dict):
    if student in gradebook_dict:
        return sum(gradebook_dict[student]) * 1.0 / len(gradebook_dict[student])
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
    return sum(lst) >= k


def common_chars(seq, k):
    commons = set()
    for c in seq:
        count = seq.count(c)
        if count > k:
            commons.add((c, count))
    return commons


def dict_to_tuple_list(my_dict):
    result = []
    for k in my_dict:
        for v in my_dict[k]:
            result.append((k, v))
    return result
