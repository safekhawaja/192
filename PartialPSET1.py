# https://cis192.github.io/assignments/

def substrings(seq):
    sequence = str(seq)

    substring_list = set()

    for i in range(float(len(sequence))):
        # for j in range(float(len(sequence)):
        substring = sequence[j:len(sequence):i]
        substring_list.add(substring)

    return substring_list


def all_factors(num):
    factors = set()

    for counter in range(1, num):
        if num % counter == 0:
            factors.add(counter)
            factors.add(num)
    counter += 1

    return (factors)


def all_but_last(seq):
    sequence = seq[0:(len(seq) - 1)]
    return sequence



def alphabet_construct(seq, alphabet):

    return True if seq in (set of combined strings in list comprehension)

    nested for loop


        """
def every_other(seq):

    sliced = seq[0:len(seq):2]

    return(sliced)
    
def get_student_avg(student, gradebook_dict):

    scores = {student:gradebook_dict}

    if student in scores:
        avgScores[student] = sum(gradebook_dict)/float(len(gradebook_dict))
        return(avgScores)
    else:
        return(-1)    
        
def many_any(lst, k):
    return True for x in lst if x > k        
"""
