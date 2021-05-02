# Problem Set 3 — Saif Khawaja

import pandas as pd

# Section 1

import numpy as np
import pandas as pd
from collections import defaultdict
import pprint
import re


def scavenger_hunt() -> dict:
    df = pd.read_csv('./wine.csv')
    # df = pd.read_csv('/Users/saif/Downloads/wine.csv')

    res = dict()
    res['shape'] = df.shape

    res['average_alcohol'] = df['alcohol'].mean()

    res['std_magnesium'] = df['magnesium'].std()

    alcohol_groups = df.groupby(['target'], as_index=False).agg({'alcohol': 'mean'})
    res['mean_alcohol_by_target'] = alcohol_groups.alcohol.tolist()

    res['proline_min_max'] = [df['proline'].min(), df['proline'].max()]

    res['num_malic_2.5'] = df[df['malic_acid'] > 2.5].shape[0]

    res['idx_lowest_flav'] = df[['flavanoids']].idxmin()[0]

    res['num_unique_hue'] = len(df['hue'].unique())

    return res


# Section 2


def get_words(file_path) -> list:
    res = []

    for line in open(file_path).readlines():
        line = re.sub(r'[^\w\s]', '', line.replace('\n', '').lower())

        words = line.split(' ')

        if '' in words:
            words.remove('')

        res.extend(words)
    return res


def get_ngrams(words, size) -> list:
    res = []
    n = len(words)

    for i in range(size - 1, n):
        t = tuple(words[i - size + 1:i + 1])
        res.append(t)
    return res


def get_counts(n_grams) -> dict:
    d = defaultdict(lambda: defaultdict(lambda: 1))

    for p, q in zip(n_grams, n_grams[1:]):
        d[p][q] += 1
    res = dict()

    for k, v in d.items():
        res[k] = dict()
        for innerk, innerv in v.items():
            res[k][innerk] = innerv
    return res


def generate_gram(counts, context) -> tuple:
    d = counts[context]
    pool = np.array(list(d.keys())).ravel()
    p = np.array(list(d.values())).ravel()
    norm_p = p / np.sum(p)
    return tuple(np.random.choice(pool, size=1, replace=False, p=norm_p).tolist())


def generate_sentence(counts, context, length=10) -> list:
    res = [context]
    for i in range(length):
        current = res[-1]
        next_word = generate_gram(counts, current)
        res.append(next_word)
    return res


def stringify(sentence) -> list:
    return " ".join("".join(gram[0]) for gram in sentence)


if __name__ == '__main__':
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(scavenger_hunt())

    words = get_words('corpus.txt')
    n_grams = get_ngrams(words, 1)
    counts = get_counts(n_grams)

    context = n_grams[np.random.choice(len(n_grams))]
    print(context)
    for i in range(5):
        print(generate_gram(counts, context))
    sentence = generate_sentence(counts, context, length=50)
    print(stringify(sentence))
